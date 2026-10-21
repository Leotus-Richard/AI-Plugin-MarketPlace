---
name: first-principles-systems
description: Problem-solving and decision architecture using the DARE First Principles framework (via AIM prompts) and DART Systems Thinking diagnostic. Trigger on /dare, /dart, /aim, or when decomposing complex problems, auditing assumptions, diagnosing system bottlenecks, or designing low-cost experiments.
---
# First Principles & Systems Thinking

A dual-engine analytical skill for deconstructing problems from the ground up (**DARE**) and diagnosing hidden system dynamics (**DART**).

## When to Use

- The user types `/dare`, `/dart`, or `/aim`.
- The user wants to apply first principles thinking, strip away industry conventions, or audit hidden assumptions.
- The user is facing an organizational, technical, or personal bottleneck and needs to diagnose what kind of system they are operating in.

## Steps

### 1. `/dare` - The DARE First Principles Workflow

Execute each step sequentially using the **AIM** (Actor, Intention, Mission) constraint structure. Do not jump ahead to solutions during steps 1 and 2.

1. **Decompose (Actor: First Principles Analyst):**
   - Check if the stated problem hides a deeper question; if so, state it in one sentence and ask the user which problem to decompose before proceeding.
   - Break the problem into its smallest constituent hierarchy across relevant dimensions (people, process, steps, time, resources, costs).
   - *Constraint:* You are penalized for introducing advice, solutions, or standard playbooks in this step.
2. **Audit Assumptions (Actor: Skeptical Red Team Analyst):**
   - Inspect every building block from Step 1. Separate hard physical/logical facts from inherited conventions ("how it's usually done").
   - Challenge each assumption by asking what evidence proves it must exist and what happens if it is deleted completely.
3. **Recombine (Actor: Lateral Architect):**
   - Take only the surviving fundamental truths ("the 12 notes") and synthesize 3 to 5 unconventional combinations that solve the root problem without the discarded assumptions.
4. **Experiment (Actor: Skeptical Scientist):**
   - Design the fastest, cheapest real-world test to validate the top recombination before risking significant time, money, or reputation.
   - Explicitly define: (a) what result rules the solution out, (b) what result keeps it alive, and (c) which building block to revisit if all tests fail.

### 2. `/dart` - The DART Systems Thinking Diagnostic

When analyzing a messy decision, organization, or recurring failure pattern:

1. **Deconstruct:** Identify the visible parts, hidden parts, connections, delayed feedback loops (where benefits arrive in seconds but damage arrives in months/years), and perverse incentives ("Cobra Effects" where people game the reward metric at the expense of the goal).
2. **Analyze (Classify the System):** Determine the cause-and-effect relationship and prescribe the exact matching protocol:
   - **Clear System** (cause & effect obvious/repeatable): Do not improvise. Build a strict checklist and define a "Brown M&M" indicator—a tiny, easily observable signal that reveals whether the whole protocol was followed carefully.
   - **Complicated System** (cause & effect discoverable via analysis): Slow down. Identify the exact domain specialist or analytical model required.
   - **Complex System** (cause & effect only visible in hindsight; involves human behavior/culture): Standard operating procedures will fail. Design small, safe-to-fail experiments to stay directionally right and course-correct in real time.
   - **Chaotic System** (cause & effect broken; active crisis): Stop analyzing. Act immediately to stabilize and create safety first; investigate root causes only after the ground stops moving.
3. **Recognize:** Identify cross-domain patterns or historical analogues that mirror this system structure.
4. **Test & Platform Perspective:** Design the smallest viable system probe, and establish three external "Platform Checks" so the user isn't blinded from inside the moving train:
   - **Mentors:** Who outside the system with zero stake in the narrative can review this?
   - **Data:** What objective metric strips away self-deception?
   - **Time:** How will we compare the system's state 30 days from now against today?

## Gotchas

- Models naturally want to be eager and jump straight to advice. During **Decompose** and **Audit**, strictly withhold solutions until the user validates the parts and assumptions.
- Never apply a Clear checklist to a Complex human problem, or a Complex experiment during a Chaotic crisis.
