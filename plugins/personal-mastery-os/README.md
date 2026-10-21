# Personal Mastery OS

`personal-mastery-os` is a comprehensive suite of 4 agentic skills and cognitive workflows for self-education, first-principles problem-solving, anti-slop writing, and executive high-performance coaching.

## Included Skills & Slash Triggers

| Skill | Slash Triggers | Description |
| --- | --- | --- |
| **`university-in-a-box`** | `/alter`, `/actor`, `/trap` | Self-education curriculum builder, deep reading engine, and durable memory retention loop. |
| **`first-principles-systems`** | `/dare`, `/dart`, `/aim` | First-principles problem decomposition via AIM constraints and Cynefin-aligned systems diagnostic. |
| **`voice-edge-creator`** | `/voice`, `/edge` | Anti-slop, anti-synthetic writing pipeline and creative concept differentiation. |
| **`high-performance-coach`** | `/brakes`, `/proof`, `/care`, `/lead` | Executive resilience, anti-burnout triage, self-trust calibration, influence, and leadership coaching. |

---

## 1. University in a Box (`/alter`, `/actor`, `/trap`)

Transforms the AI into a personal university faculty, active reading sparring partner, and memory retention engine.

- **`/alter` (The ALTER Workflow):**
  - **Advisor:** Interviews you one question at a time to establish Destination, Baseline, Sequencing, Cut List, and Milestones to produce a custom curriculum.
  - **Librarian:** Curates 3–5 foundational, high-signal primary sources and filters out noise.
  - **Tutor:** Socratic office hours diagnosing conceptual gaps; forces active retrieval instead of lecturing.
  - **Editor:** Logical refinement and sharpening of study outputs and essays.
  - **Roommate:** Cross-disciplinary analogies and lateral perspectives connecting concepts to unrelated domains.
- **`/actor` (The ACTOR Deep Reading Workflow):**
  - **Aim:** Establishes a 1-sentence reading mission and 3 target hunting questions.
  - **Compress:** Constructs the knowledge tree (Trunk = core thesis, Branches = arguments, Leaves = data).
  - **Test:** Intellectual sparring partner challenging protected beliefs and real-world failure modes.
  - **Own:** Cold plain-English recall anchored to a personal experience or analogy.
  - **Run:** Translates reading into 1 immediate decision, rule, checklist, or experiment.
- **`/trap` (The TRAP Memory Loop):**
  - **Test:** Cold recall test strictly graded for causal completeness.
  - **Retain:** Spaced repetition flashcard generator (`Question == Concise Answer`) formatted for Anki/RemNote.
  - **Associate:** Semantic network wiring linking the new concept to an existing mental model.
  - **Perform:** Rapid real-world mini-project ("MIT IAP challenge") forcing immediate application.

---

## 2. First Principles & Systems Thinking (`/dare`, `/dart`, `/aim`)

A dual-engine analytical toolkit for foundational problem decomposition and systems classification.

- **`/dare` (The DARE First Principles Workflow):**
  - **Decompose (AIM):** Deconstructs problems into constituent hierarchies (people, process, steps, time, resources, costs) with a strict ban on premature solutions.
  - **Audit Assumptions:** Challenges inherited conventions, separating hard physical/logical facts from dogma.
  - **Recombine:** Synthesizes 3–5 unconventional combinations from first-principle truths.
  - **Experiment:** Designs rapid, low-cost falsification tests with explicit pass/fail criteria.
- **`/dart` (The DART Systems Diagnostic):**
  - **Deconstruct:** Maps visible parts, hidden feedback loops, delayed impacts, and perverse incentives (Cobra Effects).
  - **Analyze (System Classification):**
    - *Clear:* Prescribes strict checklists and "Brown M&M" fidelity indicators.
    - *Complicated:* Identifies specialized analytical models.
    - *Complex:* Designs small, safe-to-fail probes for emergent human dynamics.
    - *Chaotic:* Immediate stabilization protocol before root cause analysis.
  - **Recognize:** Identifies cross-domain structural patterns.
  - **Test & Platform Perspective:** Establishes 3 external checks (Mentors, Data, Time) to avoid insider bias.

---

## 3. VOICE & EDGE Creator (`/voice`, `/edge`)

Eliminates AI clichés, "synthetic sameness", corporate jargon, and ungrounded claims in writing and creative strategy.

- **`/voice` (The VOICE Anti-Slop Writing Pipeline):**
  - **Verified:** Audits every factual claim, date, statistic, and quote (`[Verified]`, `[Unverified]`, `[Disputed]`).
  - **Owned:** One-question-at-a-time interview extracting lived experience, lessons learned, and mistakes before drafting.
  - **Insightful:** Applies the 3-sentence differentiation test ("Most believe X, I believe Y, difference is Z") and skeptic counterarguments.
  - **Clear:** 9-year-old clarity test and read-aloud audit cutting bloated jargon.
  - **Engaging:** Momentum audit cutting throat-clearing openings and decorative transitions.
- **`/edge` (The EDGE Creative Differentiation Workflow):**
  - **Differentiated:** Explicitly trashes the cliché AI default and generates 5 unconventional angles.
  - **Exacting:** Ruthlessly prunes weak variations with transparent craft trade-offs.
  - **Grounded:** Replaces vague abstractions with sensory, physical, numerical constraints.
  - **Emotional:** Anchors the narrative in authentic human emotional tension.

---

## 4. High-Performance & Resilience Coach (`/brakes`, `/proof`, `/care`, `/lead`)

Executive coaching across internal mindset, failure recovery, influence, and team leadership.

- **`/brakes` (The 4 Mental Brakes - Anti-Burnout Triage):**
  - **Over-Test:** Cuts overthinking loops with the 70% decision rule and smallest test questions.
  - **Over-Price Your Yes:** Classifies commitments as *Gifts* vs. *Taxes* and scripts healthy boundaries.
  - **Over-Ship:** Exposes perfectionism and defines the true Minimum Viable Product (MVP).
  - **Over-Ask:** Overcomes isolation with low-friction, permission-to-refuse requests for support.
- **`/proof` (Self-Trust & Failure Recovery):**
  - **Seligman's 3 Ps Audit:** Strips out *Personal*, *Permanent*, and *Pervasive* cognitive distortions after setbacks.
  - **3 Cheat Codes:** Leverages *Useful Mistakes*, *Portfolio Thinking*, and *Perspective*.
  - **Proof Pyramid:** Calibrates daily micro-actions across Proof of Action, Proof of Integrity, and Proof of Recovery.
- **`/care` & `/lead` (Influence & Team Elevation):**
  - **CARE Selling (`/care`):** Aligns proposals with stakeholders via Curiosity, Alignment, Reliability, and Emotion.
  - **People Builder (`/lead`):** Builds psychological safety and ownership through Attentive 1-on-1s, Specific Credit, and Full Outcome Ownership.

---

## Installation & Setup

In Antigravity or compatible agentic runtimes, skills can be referenced directly or linked into `.agents/skills/`:

```sh
# Example: Symlink into agent skills directory
mkdir -p .agents/skills
ln -s ../../plugins/personal-mastery-os/skills/university-in-a-box .agents/skills/university-in-a-box
ln -s ../../plugins/personal-mastery-os/skills/first-principles-systems .agents/skills/first-principles-systems
ln -s ../../plugins/personal-mastery-os/skills/voice-edge-creator .agents/skills/voice-edge-creator
ln -s ../../plugins/personal-mastery-os/skills/high-performance-coach .agents/skills/high-performance-coach
```
