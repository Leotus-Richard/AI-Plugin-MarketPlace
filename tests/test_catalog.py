"""Exercise catalog contracts with temporary, network-free registry fixtures."""
from contextlib import redirect_stdout
import importlib.util
from io import StringIO
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "catalog.py"
SPEC = importlib.util.spec_from_file_location("marketplace_catalog_under_test", SCRIPT)
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def package(name="example-plugin", sha="1" * 40, version="0.1.0"):
    return {
        "name": name,
        "repository": f"Leotus-Richard/{name}",
        "sha": sha,
        "version": version,
        "description": f"Synthetic fixture for {name}.",
    }


class CatalogContractTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory(prefix="marketplace-catalog-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        root_patch = patch.object(catalog, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def registry(self, entries):
        path = self.root / "registry" / "plugins.lock.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps({"formatVersion": 1, "plugins": entries}), encoding="utf-8"
        )

    def run_command(self, *args):
        with patch.object(sys, "argv", [str(SCRIPT), *args]), redirect_stdout(StringIO()):
            catalog.main()

    def test_duplicate_package_ids_are_rejected(self):
        self.registry([package(), package(sha="2" * 40)])
        with self.assertRaises(ValueError):
            catalog.render()

    def test_source_pin_must_be_a_full_lowercase_commit_sha(self):
        for invalid in ("", "1" * 39, "1" * 41, "A" * 40, "g" * 40, "main"):
            with self.subTest(sha=invalid):
                self.registry([package(sha=invalid)])
                with self.assertRaises(ValueError):
                    catalog.render()

    def test_excluded_source_family_cannot_be_listed(self):
        for excluded in ("swe", "swe-audit", "swe-debt", "swe-gain", "swe-help", "swe-review"):
            with self.subTest(name=excluded):
                self.registry([package(name=excluded)])
                with self.assertRaises(ValueError):
                    catalog.render()

    def test_both_hosts_select_identical_reviewed_sources(self):
        entries = [package("alpha-plugin"), package("beta-plugin", sha="2" * 40)]
        self.registry(entries)
        rendered = catalog.render()
        codex = rendered[".agents/plugins/marketplace.json"]
        claude = rendered[".claude-plugin/marketplace.json"]
        self.assertEqual(codex["name"], "leorichard-library")
        self.assertEqual(claude["name"], codex["name"])
        self.assertEqual([p["name"] for p in codex["plugins"]], [p["name"] for p in entries])
        self.assertEqual([p["name"] for p in claude["plugins"]], [p["name"] for p in entries])
        for expected, codex_plugin, claude_plugin in zip(entries, codex["plugins"], claude["plugins"]):
            with self.subTest(name=expected["name"]):
                self.assertEqual(codex_plugin["source"], {
                    "source": "url",
                    "url": f"https://github.com/{expected['repository']}.git",
                    "sha": expected["sha"],
                })
                self.assertEqual(claude_plugin["source"], {
                    "source": "github",
                    "repo": expected["repository"],
                    "sha": expected["sha"],
                })
                self.assertEqual(claude_plugin["version"], expected["version"])

    def test_check_accepts_fresh_outputs_and_rejects_either_stale_catalog(self):
        self.registry([package()])
        self.run_command()
        self.run_command("--check")
        for relative in catalog.render():
            with self.subTest(catalog=relative):
                self.run_command()
                path = self.root / relative
                value = json.loads(path.read_text(encoding="utf-8"))
                value["plugins"][0]["source"]["sha"] = "2" * 40
                path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Stale catalog"):
                    self.run_command("--check")
                self.assertEqual(
                    json.loads(path.read_text(encoding="utf-8"))["plugins"][0]["source"]["sha"],
                    "2" * 40,
                    "Check mode must report drift without rewriting the fixture.",
                )


if __name__ == "__main__":
    unittest.main()
