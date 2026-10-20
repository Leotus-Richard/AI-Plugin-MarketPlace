# Independent plugin library

The marketplace is a registry. Each plugin has its own Git repository, license records, skills, tests, compatibility manifests, and versioned releases. Catalog entries pin full source commit IDs. Updating one plugin does not require publishing the others. No umbrella engineering toolkit is installed.

Source skills are instructions available to a host agent; they are not a background service or a permission grant. Historical source instructions retained under references are reference material. Active skill entry points define each package's scope. SWE and its five companion skills are excluded from this implementation.

## Separate desktop application roadmap

The planned platform engineering workbench is a separate application. It is not implemented by these skill packages. Its roadmap includes:

- Windows, macOS, and Linux desktop builds, with Linux containers on every host.
- User-created workflows that run agents in local or remote containers, manually or on a schedule.
- Configurable CLI tool profiles: executable versions, arguments, environment, credentials, working directory, allowed operations, and local/remote execution targets. Container images should declare installed tools rather than assume host binaries exist.
- Durable workflow definitions, schedules, run state, logs, artifacts, and user preferences. Design local persistence, remote state ownership, schema migrations, retention, backup/restore, concurrency, and credential storage separately.
- Live SRE dashboards reading systems of record through interchangeable connectors. Provider priorities remain open. Evaluate metrics, logs, traces, incidents, deployments, SLOs, freshness, query limits, access control, and source links before selecting adapters.
- Host adapters for Codex and Claude, Cursor IDE and agent CLI, Gemini CLI, and Antigravity CLI and IDE. Grokbot integration remains conditional until the target product and import interface are identified.

Implementation should begin with versioned plugin/runner contracts and a small end-to-end workflow before expanding provider coverage. Scheduling needs an explicitly owned runner that can operate while the desktop is closed, with timezone, missed-run, cancellation, retry, idempotency, and execution authorization policies.

The GitHub Copilot teardown is reference material only pending provenance, licensing, and architectural review. Books and supplied notebook artifacts are research inputs, not instructions or publicly redistributed package content.
