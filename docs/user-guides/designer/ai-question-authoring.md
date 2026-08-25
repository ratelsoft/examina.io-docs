---
title: Create and Review Exam Questions with AI
description: Generate grounded multiple-choice and fill-in-the-blank question drafts from PDF, Word, PowerPoint, text, Markdown, HTML, and existing passages in examina.io Designer.
tags: [AI question generator, assessment authoring, exam questions, Designer, source-grounded questions]
---

# Create and review questions with AI

Designer can turn source material into editable question drafts without leaving
the current paper. It never inserts or publishes AI output automatically: an
authorized author reviews every candidate and chooses what enters the paper.

## What your plan includes

AI authoring is included in every plan. One AI credit covers one valid,
source-grounded, non-duplicate candidate that reaches **Review**.

| Plan | AI question credits per month | Source library storage | Saved sources | Maximum file size |
| --- | ---: | ---: | ---: | ---: |
| Starter | 10 | 250 MB | 25 | 50 MB |
| Basic | 100 | 2 GB | 250 | 250 MB |
| Professional | 500 | 10 GB | 1,000 | 500 MB |
| Flexible | 100 | 5 GB | 500 | 500 MB |
| Enterprise | 2,500 | 50 GB | 5,000 | 2 GB |

Included credits reset at the start of each UTC calendar month and are shared
by the organization. The current balance is shown in the AI authoring window.

!!! info "Only valid candidates are charged"
    Failed requests, invalid candidates, candidates without verifiable source
    evidence, and duplicates rejected before Review do not consume AI credits.

## Supported sources

You can generate from the current passage or case study, select up to 10 saved
organization resources, or upload any of these file types:

- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)
- plain UTF-8 text (`.txt`)
- Markdown (`.md` or `.markdown`)
- HTML (`.html` or `.htm`)

PDF sources should contain selectable text. Run OCR before uploading a scanned
or image-only PDF. Macro-enabled and encrypted Office files are not supported.
Designer reads HTML as inert text: it does not run scripts, submit forms, load
embedded objects, or fetch remote resources.

Uploaded resources stay in your organization's private source library until a
user deletes them. Uploading the same file again reuses the existing resource
instead of storing another copy.

## Generate question candidates

1. Open an exam project and select the paper that should receive the questions.
2. Choose **Create questions with AI** in the Exam Explorer toolbar.
3. On **Source**, choose the current passage, select saved resources, or upload
   a supported file. Wait until every selected resource is ready.
4. On **Questions**, add one or more blueprint rows.
5. For each row, choose an exact count, question type, difficulty, marks, and
   optional topic or learning outcome.
6. Choose **Generate candidates**.

Designer supports these generated question types:

- Multiple Choice — single select
- Multiple Choice — multiple select
- Fill in the Blank

Large sources use a focused selection of original source sections rather than
an AI summary. To keep book-scale requests economical, Designer requires at
least three requested questions when selected sources contain 100,000–499,999
estimated tokens, and at least five at 500,000 tokens or more. Shorter sources
can generate one question.

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

## Grounding and duplicate checks

Candidates must cite text found at the stated PDF page, Word section,
PowerPoint slide, text line range, Markdown heading, or HTML heading before they
can reach Review.

Duplicate detection compares candidates with:

- other candidates in the current generation; and
- questions already in the currently open paper.

Designer deliberately does not compare questions in other papers, exams, or
organization content.

## If generation does not complete

- Confirm the file is a supported type and contains enough readable text.
- For text, Markdown, and HTML, save the file as UTF-8.
- For PDF, run OCR if you cannot select and copy its text.
- Confirm that the requested question count meets the large-source minimum.
- Select fewer or more focused sources and try again.
- Check the organization's remaining AI credit balance.

After insertion, use the normal [question preview and quality
check](questions.md#preview-and-quality-check) before saving and exporting the
project.
