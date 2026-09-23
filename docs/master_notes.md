---
title: "Digitizing Earth Science Collections Data with AI (Claude Code)"
event: TDWG 2026 – GeoData Workshop
format: 2-hour hands-on workshop
compiled: 2026-09-23
sources:
  - 20260922 Notes.md
  - geodata_workshop_notes.md (handwritten notes transcription, 2026-09-21)
  - media_1790173505622.md (Intro slide)
  - media_1790173505629.md (Slide outline)
  - media_1790173505632.md (Workshop slides – prompting)
  - media_1790173505640.md (Accuracy, model timelines, role of AI)
  - 20260721_ypm_master_data_06_top100.tsv (Peabody sample data)
---

# Digitizing Earth Science Collections Data with AI (Claude Code)

**Goal:** Transform example Earth science datasets into a format compatible with the **compound specimen model** and the **Mineralogy Extension (MinExt)**, using AI (Claude Code) to build **repeatable ETL pipelines**.

---

## Part A — Workshop Outline

1. **Introduction**: scope of the workshop and the presenter's experience using AI.
2. **The Role of AI in Museums**: what problem AI solves, what role it plays, and how accurate it is.
3. **The AI Model Landscape**: the major models, what they do (and don't do), and how their release timelines compare.
4. **Using AI Effectively**: rules of thumb and prompting principles.
5. **Pipelines and ETL Fundamentals**: vocabulary, components, and how to organize a pipeline.
6. **Claude Code**: what it is, how it differs from chat tools, and how to set it up.
7. **Source Datasets and the Target Data Model**: source data, target data and the compound specimen model.
8. **The Standard Process**: the core ETL procedure used for every exercise.
9. **Hands-on Exercises**: German mineral names, French localities, and Peabody records converted to the compound model.
10. **Accuracy, Review, and Wrap-up**: how we know the results are right.

---

## Part B — Detailed Sections

### 1. Introduction

**Scope:** A 2-hour workshop that applies AI to real collection-data transformation problems in the geosciences.

**Presenter's background (intro slide):**

- For the past ~6 months, the presenter has built multiple ETL pipelines for several separate projects using Claude Core
- Determine how to effectively utilize claude code in a collections data workflows
  - Repeatable and transparent
  - Reuse
  - Provenance
- Pipeline components include data transforms, testing, frontend ui, and even custom database abstraction layers.
- *"AI is an entry-level programmer. I can't hire one, so nothing is being lost."*

### 2. The Role of AI in Museums

**The recurring problem:** Every TDWG conference makes the same point:

- There isn't enough time or money.
- There aren't enough people.

This is unlikely to change. **AI addresses the problem if it is used efficiently and strategically.**

Different models suit different tasks. Opus and Flash will both play roles in the biodiversity-informatics tasks.

Questions for this section:

- What problem does AI solve in museums?
- What role does it play in the data workflow?
- How accurate is it? (See Section 10.)

---

### 3. The AI Model Landscape

**Many models, different strengths:** Some models perform specific tasks far better than others.

> **Anecdote: screenshot → Figma mockup.** A plugin built for this task was installed, and it offered multiple models. The task was tried with Opus, Sonnet, GPT, Flash and Flash Lite. **All of them failed completely except Flash.**
> *Lesson:* Match the model to the task, and be prepared to switch.

**Model timelines** (as recorded in the notes; verify dates before presenting):

| Gemini Model | Release Date | Claude Model | Release Date |
| --- | --- | --- | --- |
| Flash 2.0 | 2/2025 | Claude 1 | 3/14/2023 |
| Flash 2.5 | 6/17/2025 | Claude 3 Family | 3/4/2024 |
| Flash 3.5 | 5/19/2026 | Claude 4 Family | 5/22/2025 |
| Flash 3.6 | 7/21/2026 | Sonnet 4.5 | 8/29/2025 |
| Flash 3.7 | 8/13/2026 | Opus 4.5 | 11/24/2025 |
| Flash 3.8 | 9/2/2026 | Sonnet 5 | 6/30/2026 |
| | | Opus 5 | 7/24/2026 |

**Talking point:** Models improve quickly. Judgments about reliability go out of date, as the notes put it: "Gemini Flash 3 is reliable; Flash 1 is not."

Broader Implications

- Organizations are no longer bound to general-purpose software such as Excel.
- Building software is getting easier, and demand for custom solutions keeps rising.

---

### 4. Using AI Effectively — Rules of Thumb

**Core premise:** *Most data is AI-ready with the right prompt.*

**Success depends on three factors:**

1. **The prompt**
2. **The amount of context**
3. **The model**

**Prompting principles:**

- **AI models are dumb, and computers are dumb.** The best results come from giving the model every task, note and guideline. *"Hold their hand."*
- **Have the model review the instructions.** Models can find gaps and ambiguity in a plan before it is run.
- **Wording matters.** On several occasions, a task run with AI gave mediocre results. Someone else then phrased the instructions differently and the task succeeded. *The only difference was the wording.*
- **Process the data ahead of time.** Profile and clean it before asking for transformations.
- **Compare results using varying levels of information.** Ask: *"What if you didn't provide all the context?"*

**Key points for pipeline work:**

- Avoid runaway codebases.
- Make things repeatable with config files and scripts.
- Define metrics.
- Provide examples for context.
- Make a plan, then have Claude review it.
- Use a stepwise architecture.
- Generate reports at each stage in the process
- Preserve source in its verbatim form

Provenance

1. How do we track the usage of AI in a collections workflow?
   1. Store in a standardized GitHub repository
   2. Minimize reliance on AI to perform specific transformations
      1. Script tasks for generalized usage
   3. Generate reports

---

### 5. Pipelines and ETL Fundamentals

**Questions to answer:**

- What is a pipeline?
- What are its main components?
- Which models are best at specific tasks?

**ETL vocabulary:**

| Stage | Meaning |
| --- | --- |
| **Extract** | Pull data from its source (a CMS export, a CSV, a database) in its verbatim form. |
| **Transform** | Clean, split, categorize, translate, reconcile and restructure the data to match the target model. |
| **Load** | Write the transformed data to the target format or system. |

**Organizing a pipeline:**

- Use discrete, stepwise **stages**. Each stage has defined inputs and outputs.
- Drive behavior through **config files** rather than hard-coded logic.
- Keep **scripts** small and repeatable.
- **Always generate a report** that defines what the output contains.

---

### 8. The Standard Process (Core ETL Procedure)

Every exercise uses the same procedure:

1. **Analyze (profile) the dataset.** List its attributes: column count, languages, delimiters, number of unique values, qualifiers, and use of controlled vocabularies.
2. **Define the target.** Decide what the end result should look like.
3. **List the changes** needed to turn the source into the target.
4. **Provide helpful resources**, such as normative documentation, external authorities (GADM) and definitions of terms.
5. **Write a plan.** Using the profile, write a stepwise plan that includes the process structure (stages) and the reports to be generated. **Have Claude review the plan.**
6. **Generate the script.**
7. **Run the process.**
8. **Review the results.** The output must be described by a **report**. Always generate a report.

---

### 9. Hands-on Exercises

The three exercises are described in detail in **Part C — Sample Datasets**:

- **Exercise 1:** Translate German mineral names to English.
- **Exercise 2:** Parse and categorize French locality strings into a place hierarchy.
- **Exercise 3:** Convert Peabody mineralogy records into the compound specimen model.

A further AI example from the notes is **creating a script from a list of human-readable parameters**. This shows that a plain-language specification can be turned directly into working code.

---

## Exercise 1. 

**Dataset: mineral_names_de.csv**

Goal: Create a German-English dictionary for mineral names

Process: 

1. Create project structure
   1. Verbatim File Preservation
2. Clean Source Data
   1. Document transforms
   2. Generate Reports
3. Create Plan
   1. What conditions will be set to translate a name? Exact match?
   2. What resources are available to provide the model context?
   3. List Operations
4. Run German Mineral List through translator using the plan
5. Results: 2 CSV Files: 
   1. English to German Dictionary
   2. List of untranslated outliers

6. Review untranslated outliers

### Example 2. Localities

### Example 3. Compound Specimen Model

**Target data model:** the **compound specimen model**, aligned with the **Mineralogy Extension**. A physical specimen is a *material entity* that can contain component parts (for example, the individual minerals in a specimen). Each part is linked to its parent.

**Compound specimen model procedure:**

1. Find the fields that contain the part names (for example, `mineral_list` or `mineral_qualified_name_1…5`).
2. Define the criteria for assigning material categories (for example, mineral, rock or meteorite).
3. List the changes needed to transpose a list (or repeating columns) into a single column.
4. Create the join ID: **`is_part_of_material_entity_id`**.
5. **Stack** the dataset so each part becomes its own row, linked to its parent specimen.

**Supporting workshop material:** a visualization framework that can display a compound specimen.

### 10. Accuracy, Review, and Wrap-up

**How do we know it's accurate?**

1. **Compare AI errors with human error.** Manual digitization is not error-free either.
2. **Use the latest models.** Reliability improves quickly from one generation to the next.
3. **Build in verification.** Use generated reports, defined metrics, and a review of unresolved values.
4. **Compare runs** made with varying levels of context and instruction.

**Wrap-up:** The goal is a *repeatable* pipeline that participants can take home and apply to their own collections. It should not be a one-off result.

## Appendix — Open Items from the Notes

- [ ] Build or choose the **visualization framework** for displaying compound specimens.
- [ ] Prepare the **generalized example** that participants digitize themselves.
- [ ] Finalize the **German mineral names** and **French localities** CSV files.
- [ ] Verify the dates in the **model timeline** table before presenting.
- [ ] Prepare the **"script from human-readable parameters"** demo.
- [ ] Prepare the demo that answers **"what if you didn't provide all the context?"** by comparing results across levels of context.
