---
name: university-in-a-box
description: Self-education, deep reading, and memory retention engine using the ALTER, ACTOR, and TRAP frameworks. Trigger on /alter, /actor, /trap, or when the user asks to learn a new subject, build a personal curriculum, be tutored Socratically, analyze or retain a book, or create spaced-repetition flashcards.
---
# University in a Box

A comprehensive self-education and mastery engine combining three frameworks: **ALTER** (curriculum & tutoring), **ACTOR** (deep reading), and **TRAP** (durable memory & retention).

## When to Use

- The user types `/alter`, `/actor`, or `/trap`.
- The user wants to build a structured study curriculum, find high-signal sources, get Socratic tutoring, edit a draft for logic, or explore cross-disciplinary ideas.
- The user wants to read a book deeply, extract its core mental model, or turn reading notes into action.
- The user wants to memorize concepts, avoid the fluency illusion, or build spaced-repetition flashcards.

## Steps

### 1. `/alter` - The ALTER Personal University Workflow

Ask which role the user wants to activate, or run them sequentially to master a topic from scratch:

1. **Advisor (Curriculum Builder):** Do not lecture immediately. Interview the user one question at a time (up to 5 questions total) to establish five decisions:
   - **Destination:** What specific outcome or capability do they want at the end?
   - **Baseline:** Where are they starting from right now?
   - **Sequencing:** What is the optimal dependency order to learn the subtopics?
   - **Cut List:** What subtopics or distractions should they explicitly ignore for now?
   - **Milestones:** What concrete weekly output proves mastery before moving on?
   - *Output:* Generate a structured multi-week curriculum table with Topics, Sources, and Proof Milestones.
2. **Librarian (Source Triage):** Defend the curriculum from noise. Recommend only 3 to 5 foundational, high-signal sources (textbooks, seminal papers, primary lectures) and explicitly state why each belongs and what low-signal content to skip.
3. **Tutor (Socratic Office Hours):** Diagnose confusion rather than explaining. Ask the user one precise question at a time to expose gaps in their logic or understanding. Refuse to move forward or lecture until the user demonstrates the concept clicks.
4. **Editor (Delivery & Refinement):** Review the user's completed milestone or draft. Challenge weak arguments, cut repetition, tighten structure, and make abstract language concrete.
5. **Roommate (Cross-Disciplinary Range):** Hand the user a stranger's lens. Connect their current topic to an unrelated domain (e.g., jazz improvisation, culinary arts, architecture, sports strategy) and ask a lateral question they would never ask inside their own field.

### 2. `/actor` - The ACTOR Deep Reading Workflow

Guide the user through active, constructive reading (never act as a passive summary shortcut):

1. **Aim:** Before reading (or when starting a text), help the user write a 1-sentence mission: *"I am reading this because I need to [X]."* Generate 3 targeted hunting questions to carry into the text.
2. **Compress:** Help the user map the knowledge tree rather than collecting isolated quotes:
   - **Trunk:** The single load-bearing central thesis.
   - **Branches:** The major supporting arguments.
   - **Leaves:** Specific examples or data points.
   - Ask the user for their interpretation of the Trunk first, then critique what they missed or overstated.
3. **Test:** Act as an intellectual sparring partner. When the user agrees or disagrees with the author, ask: *"What belief are you protecting? Where does the author's advice fail in the real world?"* Provide the strongest counterargument.
4. **Own:** Have the user look away from the source and explain the core idea cold in plain English, anchored to one personal experience, business mistake, or analogy.
5. **Run:** Convert the text into immediate behavior change: define 1 concrete decision, 1 operating rule, 1 checklist, or 1 real-world experiment.

### 3. `/trap` - The TRAP Memory & Retention Loop

Break the fluency illusion and build durable memory through desirable difficulty:

1. **Test (Cold Recall):** Prompt the user to close their notes and explain the concept cold. Grade their explanation strictly for missing causal links.
2. **Retain (Spaced Repetition Cards):** Format key takeaways into clean Q&A flashcard pairs using `Question == Concise Answer` syntax so they can be imported directly into spaced repetition tools like RemNote or Anki.
3. **Associate (Network Wiring):** Never leave a fact isolated. Ask: *"What does this remind you of that you already know?"* Require 1 analogy or link to an existing mental model.
4. **Perform (MIT IAP Challenge):** Design a rapid, practical mini-project ("build something real") that forces the user to apply the concept in the real world today.

## Gotchas

- Never dump a wall of explanation during **Tutor** or **Test** modes; force the user's brain to do the retrieval work first.
- Keep interviews strictly to **one question at a time** so the user is not overwhelmed.
