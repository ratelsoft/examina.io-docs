---
title: Create and Review Exam Questions with AI
description: Generate grounded multiple-choice and fill-in-the-blank question drafts from PDF, Word, PowerPoint, text, Markdown, and HTML sources in examina.io Designer.
tags: [AI question generator, assessment authoring, exam questions, Designer, source-grounded questions]
---

# Create and review questions with AI

When this feature is enabled for your organization, Designer can turn source
material into editable question drafts. It does not add or publish questions
automatically: you review every candidate and choose what enters the current
paper.

## Supported sources

Upload one of these file types:

- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)
- plain UTF-8 text (`.txt`)
- Markdown (`.md` or `.markdown`)
- HTML (`.html` or `.htm`)

PDF sources should contain selectable text. Run OCR before uploading a scanned
or image-only PDF. Macro-enabled and encrypted Office files are not supported.
Designer reads HTML as text only; it does not run scripts, submit forms, load
embedded objects, or fetch remote resources.

## Generate question candidates

1. Open an exam project and select the paper that should receive the questions.
2. Choose **Create questions with AI** in the Exam Explorer toolbar.
3. On **Source**, choose a supported file and wait for Designer to show the
   extracted source sections.
4. On **Questions**, set the candidate count, difficulty, marks, and optional
   topic or learning objective.
5. Select one or more question types: **Single select**, **Multiple select**, or
   **Fill in the blank**.
6. Choose **Generate candidates**.

The source-file size limit comes from your organization's plan. Large sources
may also need to be split into shorter, focused files.

## Review before inserting

On **Review**, check and edit each candidate's:

- question text;
- answer choices or accepted fill-in answers;
- correct-answer selection;
- explanation;
- difficulty and marks; and
- source citation.

Clear **Accept** or choose **Discard** for any candidate you do not want. Choose
**Insert selected** only after the remaining questions are ready for normal
Designer editing and preview.

!!! important
    AI output can be incomplete, ambiguous, or incorrect even when it cites a
    source. A subject-matter expert should verify the wording, answer key,
    explanation, difficulty, accessibility, and score before delivery.

## Grounding, duplicates, and credits

Candidates must cite text found at the stated PDF page, Word section,
PowerPoint slide, text line range, Markdown heading, or HTML heading before they
can reach Review.

Duplicate detection is limited to the current generation and the currently
open paper. Designer does not compare questions in other papers, exams, or
organization content.

Only valid candidates are charged. The Questions and Review steps show the
organization's available monthly AI credits.

## If generation does not complete

- Confirm the file is a supported type and contains enough readable text.
- For text, Markdown, and HTML, save the file as UTF-8.
- For PDF, run OCR if you cannot select and copy its text.
- Reduce the source length or candidate count and try again.
- If the feature or credit balance is unavailable, contact your organization
  administrator.

After insertion, use the normal [question preview and quality
check](questions.md#preview-and-quality-check) before saving and exporting the
project.
