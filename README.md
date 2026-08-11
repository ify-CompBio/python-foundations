# Python Foundations

This repository documents my structured learning of Python fundamentals,
using a PACER knowledge-sorting framework to prevent overload and ensure
long-term retention.

The goal is not speed, but *correct mental organisation* of programming knowledge,
with a view toward later bioinformatics and data analysis work.

---

## P — Procedural (How to do things)

This repository contains small, focused Python scripts, each implementing
a single procedural concept:

- Variable assignment
- Data types
- Strings and slicing
- Lists and dictionaries
- Conditionals
- Loops
- Functions

Each script is runnable from the command line and designed to be re-executed
as a reference for syntax and patterns.

---

## A — Anecdotal (What I learn by doing)

Throughout development, I will encounter common beginner issues such as:

- Off-by-one errors in loops
- Confusion between mutable and immutable data types
- TypeErrors from mixing strings and numbers

These learning moments should be recorded as:
- comments inside scripts
- informative Git commit messages

This will act as a lightweight debugging log.

---

## C — Conceptual (Why it works)

Conceptual understanding should be captured separately from code, focusing on:
- what loops *represent* (iteration, not repetition)
- why functions improve reuse and clarity
- how data structures affect program design

Conceptual explanations should be short and written in plain language.

---

## E — Evidence (Proof it works)

Each script prints output demonstrating correct behaviour.
Some scripts include example input/output pairs to show expected results.

Running the script = verifying the evidence.

---

## R — Reference (What I don’t memorise)

I do not memorise syntax tables or method lists.
External references are used when needed, including:
- official Python documentation
- standard library references

The repository prioritises *knowing how to find information*, not storing it all mentally.

---

## Structure

Scripts should be ordered numerically to reflect learning progression.
Each file represents one isolated concept, however some roadmap scripts touch multiple ideas.
The file name reflects the PRIMARY concept being trained.


This repository serves as a foundation for later projects in
data analysis and bioinformatics.

## 🔁 Beyond Scripts: How Skill Actually Develops

The script sequence builds structure and understanding.

However, real programming ability comes from applying that structure in three additional ways:

---

## 1️⃣ Weekly Integration Task (Synthesis)

Once per week, combine **3–4 previously completed scripts** into one small problem.

### Example:
- take loops + functions + lists  
- build a simple data processing workflow  

### Purpose:
- connect isolated concepts  
- develop system-level thinking  
- move beyond “one concept per file”  

### Note:
This task should feel slightly unstructured or messy. That is intentional.

---

## 2️⃣ Deliberate Failure Task (Debugging Practice)

Intentionally break working code and repair it.

### Examples:
- remove variables  
- introduce incorrect types  
- break file paths  
- corrupt inputs  

### Purpose:
- build debugging intuition  
- understand error messages deeply  
- improve recovery speed when things fail  

### Key idea:
Programming skill is largely the ability to recover from failure.

---

## 3️⃣ Rewrite Task (Memory + Mastery)

Rebuild a previously completed script from memory, without looking.

Then compare with the original.

### Purpose:
- strengthen retention  
- test true understanding  
- identify gaps in mental models  

### Rule:
If a script cannot be rewritten, it is not yet fully understood.

---

## 🧠 Learning Model Summary

This repository develops skill through four layers:

- **Scripts → structure** (what exists)  
- **Integration → connection** (how it fits together)  
- **Failure → resilience** (what breaks and why)  
- **Rewrite → mastery** (what is internalised)  

---

## ⚠️ Important Principle

Learning is not linear.

Scripts are anchors — not checkpoints.

Understanding develops through cycles of:

**build → test → break → rebuild**