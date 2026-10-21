# LeoRichard Plugin Library

A GitHub marketplace of 20 independent engineering and personal mastery plugins. Install a capability on its own; each plugin has a separate repository and versioned release. The marketplace contains catalog metadata and documentation rather than a monolithic toolkit.

## Install

```sh
codex plugin marketplace add https://github.com/Leotus-Richard/AI-Plugin-MarketPlace.git
codex plugin add systems-thinking@leorichard-library

claude plugin marketplace add Leotus-Richard/AI-Plugin-MarketPlace
claude plugin install systems-thinking@leorichard-library
```

See [installation](docs/installation.md) for existing local registrations, native host verification, and Cursor, Gemini CLI, and Antigravity release archives. Choose plugins individually. No host credentials, CLI tools, containers, or background services are installed by these packages.

## Catalog

| Plugin repository | Purpose | License expression |
| --- | --- | --- |
| [agent-instruction-authoring](https://github.com/Leotus-Richard/agent-instruction-authoring) | Focused skill/instruction authoring and portability review, without auto-installing the result. | MIT |
| [agent-role-presets](https://github.com/Leotus-Richard/agent-role-presets) | Configure advisor, researcher, librarian, tutor, editor, and cross-domain perspectives for a task. | MIT |
| [agent-workflow-design](https://github.com/Leotus-Richard/agent-workflow-design) | Workflow graphs, bounded coordination, comparison rubrics, and handoffs; no scheduler/runtime. | MIT |
| [application-verification](https://github.com/Leotus-Richard/application-verification) | Create and maintain application verification harnesses, exercise CLI/UI behavior, and assess performance evidence. | MIT |
| [applied-learning](https://github.com/Leotus-Richard/applied-learning) | Learn technical material through focused explanation, critical questions, recall, and practical exercises. | MIT |
| [code-quality-review](https://github.com/Leotus-Richard/code-quality-review) | Review changes for correctness and design quality, and simplify generated code without changing required behavior. | MIT |
| [frontend-design](https://github.com/Leotus-Richard/frontend-design) | Design, review, and refine frontend interfaces using portable Impeccable craft and platform references. | MIT AND Apache-2.0 |
| [git-delivery](https://github.com/Leotus-Richard/git-delivery) | Optional local Git commit preparation and verification; no automatic publication. | MIT |
| [grounded-communication](https://github.com/Leotus-Richard/grounded-communication) | Draft and review technical communication for evidence, source fidelity, clarity, and audience fit. | MIT |
| [llm-engineering](https://github.com/Leotus-Richard/llm-engineering) | Prompt contracts, LLM evaluation, and RAG design. | MIT |
| [ml-experimentation](https://github.com/Leotus-Richard/ml-experimentation) | Reproducible ML experiment plans and interpretability claim review. | MIT |
| [personal-mastery-os](https://github.com/Leotus-Richard/personal-mastery-os) | A suite of 4 agentic skills and cognitive workflows for self-education, systems thinking, original writing, and executive coaching. | MIT |
| [program-management](https://github.com/Leotus-Richard/program-management) | Draft program charters, delivery plans, risk registers, stakeholder plans, and evidence-grounded status reports. | MIT AND Apache-2.0 |
| [requirements-discovery](https://github.com/Leotus-Richard/requirements-discovery) | Clarify requirements through focused interviews, synthesize specifications, and draft stakeholder questionnaires. | MIT |
| [security-assurance](https://github.com/Leotus-Richard/security-assurance) | Threat modeling, supply-chain findings, and policy-as-code review artifacts. | MIT |
| [software-architecture](https://github.com/Leotus-Richard/software-architecture) | Design domain models, module boundaries, TypeScript contracts, and decision-focused prototypes. | MIT |
| [systems-thinking](https://github.com/Leotus-Richard/systems-thinking) | Analyze uncertain problems through evidence, first principles, system context, and bounded experiments. | MIT |
| [testing-and-debugging](https://github.com/Leotus-Richard/testing-and-debugging) | Develop features test-first, reproduce bugs, and prove regression fixes through observed behavior. | MIT |
| [work-tracking](https://github.com/Leotus-Richard/work-tracking) | Canonical work graphs, ticket drafts, triage, and tracker-neutral local exports. | MIT |
| [workflow-feedback](https://github.com/Leotus-Richard/workflow-feedback) | Connect observations, decisions, authorized actions, and outcomes into useful workflow feedback. | MIT |

## Compatibility and validation

Every plugin includes portable Agent Plugin, Codex, and Claude manifests, plus generated Cursor, Gemini CLI, and Antigravity adapters. Release assets include deterministic ZIPs and SHA-256 checksums. Package CI validates identities, local skill resources, exclusions, export content, and builds on Windows, macOS, and Linux; helper packages also test their Node scripts.

These checks establish packaging and test results, not universal agent behavior. Fresh-session behavior must be verified in each host. Cursor IDE and agent CLI, and Antigravity IDE and CLI, are separate verification targets. Grokbot support is pending identification of a compatible product/import interface.

The [source registry](registry/plugins.lock.json) records full immutable commit pins. Both native catalogs are generated from it with `python scripts/catalog.py`; `--check` verifies parity. Versioned plugin release assets are available from each catalog repository link.

## Boundaries and roadmap

SWE, swe-audit, swe-debt, swe-gain, swe-help, and swe-review are excluded. Optional principles and retained historical source documents are reference material, not a whole-toolkit execution policy. Original licenses/notices are retained; new packaging and owner-designated missing-license files use MIT. Mixed-license packages preserve their Apache notices.

The separate desktop workbench roadmap covers configurable CLI tooling, durable state, local/remote container agent workflows, manual/scheduled triggers, and live SRE dashboards over systems of record. Provider prioritization remains open. See [architecture and roadmap](docs/architecture.md). These runtime features are planned, not implemented by this marketplace.

## Maintaining a release

Change and validate one plugin in its own repository, publish its versioned release, then update that plugin's full commit pin in the registry and regenerate both catalogs. Review changes through a work-item-linked pull request. Do not move an existing release tag or silently replace source pins.

## Initial release evidence

[Validation results](registry/validation.json) record the exact source CI runs, 20 enabled Codex installs in an isolated profile, native adapter checks, and the limits of that evidence. [Release asset checksums](registry/release-assets.sha256) cover all 100 downloaded files. Publication validation does not change existing global host registrations.
