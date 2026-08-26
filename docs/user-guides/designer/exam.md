---
title: The exam
description: Configure exam title, exam code, branding, description, instructions, paper flow, and answer visibility in examina.io Designer.
tags: [designer, exam settings, exam code, branding, paper flow]
---

# The exam

Select an exam in Exam Explorer and the editing pane shows everything that
applies to the exam as a whole. Most of it is visible to the examinee, so it is
worth being deliberate here rather than filling it in to get past the screen.

![Exam properties and settings](../../assets/images/designer/exam-properties.png)

## Exam title

The name the examinee sees while sitting the exam. Write it the way you would
print it on a paper: *MTH 201 Fall Examination*, not *mth201-final-v2*.

## Exam code

**Required, and the field most likely to cause trouble later.**

The code identifies the exam when it reaches Manager, so it has to be unique
across every exam your organization imports. Two exams sharing a code cannot
both be imported cleanly.

Two rules the field enforces:

- **No spaces**
- **Letters and numbers only** — no punctuation, dashes or underscores

`MTH201FALL` is fine. `MTH 201` and `MTH-201` are not.

!!! tip "Decide a scheme before your second exam, not your twentieth"
    Something like `SUBJECT` + `YEAR` + `SITTING` stays readable and stays
    unique: `MTH201F26`, `CHM104M26`. Retrofitting a scheme means re-importing
    exams that are already in use.

## Branding banner and colour

Optional. The banner appears to the examinee while they take the exam, and the
colour tints the surrounding interface.

Use these when a single organization delivers exams on behalf of several
departments or clients, and each needs to look like its own. **Clear** removes
either without affecting the other.

## Description

Shown to the examinee before they begin. Say what the exam is and what it
covers — this is the first thing a nervous candidate reads, so plain language
serves better than formal wording.

## General instruction

Also shown before the exam starts, and the right place for rules that apply
across every paper: whether materials are permitted, what happens if the
connection drops, how to raise a problem.

Per-paper instructions belong on [the paper](paper.md) instead. Anything
repeated on every paper belongs here.

## Exam paper flow

For exams with more than one paper, this decides how the next paper arrives.

| Setting | Behaviour |
|---|---|
| **Server Controlled** | The server decides when each paper opens. Everyone moves together |
| **Client Controlled** | The examinee moves on when they finish the current paper |
| **Force Continuous** | Papers run one after another without a break |

Choose **Server Controlled** for a sitting where everyone must be on the same
paper at the same time. Choose **Client Controlled** when candidates should
work at their own pace within an overall time limit.

## Show answers after exam

Whether the examinee sees which answers were right once they submit.

Useful for practice tests and revision. Almost always wrong for a live
assessment, because it hands the answer key to everyone who sits early.

## Allow inter-paper navigation

Whether an examinee can go back to a paper they have already left.

Set to **No** when each paper is meant to be sealed once submitted. Set to
**Yes** when the whole exam is really one long paper split into parts and
candidates should be free to revisit.

## Before you move on

The exam code is the one setting that is genuinely painful to change later,
because it is how Manager recognises the exam. Everything else can be edited and
re-exported without consequence.

Next: [The paper](paper.md).
