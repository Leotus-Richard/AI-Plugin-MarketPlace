# Installation and verification

## Codex and Claude Code

Register this GitHub marketplace using your host's marketplace command, then install only the plugins you need:

```sh
codex plugin marketplace add https://github.com/Leotus-Richard/AI-Plugin-MarketPlace.git
codex plugin add systems-thinking@leorichard-library

claude plugin marketplace add Leotus-Richard/AI-Plugin-MarketPlace
claude plugin install systems-thinking@leorichard-library
```

The marketplace ID is `leorichard-library`. If you already registered a local marketplace with that name, inspect its source and installed plugins before changing it. Removing a marketplace can remove installed plugins. Preserve local settings and migrate deliberately; these instructions do not replace existing registrations automatically.

Use the host's plugin list and a fresh session to verify installed skills and behavior. Registration alone does not establish functional readiness.

## Cursor, Gemini CLI, and Antigravity

Download the appropriate host ZIP and SHA256SUMS from the individual plugin's release. Verify the checksum, extract into a new directory named for that plugin, and use the host's native import or plugin-directory mechanism. The archive entries are relative to that package root. Build the same adapters locally with `python scripts/build_release.py` in that plugin's repository.

- Cursor: the Cursor archive uses the portable Agent Plugin manifest. Agent CLI can load the extracted package with `--plugin-dir PATH`; IDE discovery and reload require separate verification.
- Gemini CLI: the Gemini archive contains `gemini-extension.json` and skills; validate and install the extracted directory with the native `gemini extensions` commands.
- Antigravity: the archive uses Antigravity's own `plugin.json` shape; use `agy plugin validate PATH` followed by `agy plugin install PATH`. CLI import and IDE behavior require separate verification.

These are skill-only packages. They do not automatically install CLI binaries, credentials, container runtimes, MCP servers, hooks, or schedulers. Structural validation and successful import do not prove every workflow's behavior. Grokbot is not advertised as supported yet.

## Windows checkout paths

Some preserved reference trees are deeply nested. Prefer a short checkout path
when cloning a plugin repository on Windows. If Git reports filenames or paths
that are too long, Git for Windows may require long-path support for that clone:

```sh
git -c core.longpaths=true clone https://github.com/Leotus-Richard/software-architecture.git C:\src\software-architecture
```

This command enables the Git option for that operation; it does not change global
Git settings. Host-managed clone/cache locations may need their own configuration.
