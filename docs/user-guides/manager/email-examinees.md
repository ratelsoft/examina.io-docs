---
title: Email Your Examinees
description: Send exam invitations and results from examina.io Manager using personalization placeholders, including sign-in links that log the examinee straight in.
tags: [exam invitation, examinee email, magic link, manager, placeholders]
---

# Email your examinees

Manager can email the people mapped to an exam: an invitation before the
sitting, or their result afterwards. You write the message once, and Manager
personalises it for each recipient before sending.

Select the exam, then use **Send Email to Examinees** from the mapped-examinee
panel. Only examinees with an email address on their record receive anything.

## Personalisation placeholders

Write `#[CODE]` in your message and each examinee receives their own code in its
place. Placeholders work in the subject line as well as the body.

### The examinee

| Placeholder | Becomes |
|---|---|
| `#[FNAME]` | First name |
| `#[MNAME]` | Middle name, or nothing |
| `#[LNAME]` | Last name |
| `#[FLNAME]` | Full name |
| `#[TITLE]` | *Mr.* or *Ms.*, from the gender on the record |
| `#[GEN]` | Gender as text |
| `#[CODE]` | Examinee code or ID |
| `#[PASS]` | Passcode |
| `#[EMAIL]` | Email address |
| `#[PHONE]` | Phone number, or nothing |
| `#[DOB]` | Date of birth |
| `#[PIC]` | The examinee's photograph, as an image |

### The exam

| Placeholder | Becomes |
|---|---|
| `#[EXAM]` | Exam title |
| `#[ECODE]` | Exam code |
| `#[LINK]` | The exam link, as a clickable link |
| `#[MAGICLINK]` | A sign-in link for that one examinee — see below |
| `#[TIME]` | The examinee's mapped start time, or nothing when no time was set |
| `#[PAPERS]` | The papers this examinee is mapped to |

### The result

| Placeholder | Becomes |
|---|---|
| `#[SCORE]` | Score achieved |
| `#[MAX]` | Obtainable score |
| `#[PERCENT]` | Score as a percentage |
| `#[RESULT]` | A formatted result summary |

!!! warning "Result placeholders only belong in a result email"
    These read from a completed attempt. In an invitation sent before anyone has
    sat the exam there is no score to substitute, and `#[PERCENT]` in particular
    has nothing to divide by. Keep them out of invitations.

## Sign-in links

`#[MAGICLINK]` inserts a link that signs that examinee straight into their exam.
They do not type a code or a passcode; the link carries their identity.

This is worth using when passcode distribution is the awkward part of your
process — younger candidates, large cohorts, or anyone likely to mistype a code
on exam morning.

```text
Hello #[FNAME],

Your exam, #[EXAM], starts at #[TIME].

Open it here: #[MAGICLINK]

If the link does not work, sign in at #[LINK] with
code #[CODE] and passcode #[PASS].
```

### What to know before you use it

**Send the code and passcode as well.** Email is the least reliable part of exam
day — filters, delays, a candidate reading mail on a phone they will not sit the
exam on. Treat the link as the convenient path and the credentials as the
fallback, exactly as the example above does.

**The link is personal, and it is a credential.** Anyone holding it can sit that
exam as that examinee. Tell candidates not to forward it. It is no more
shareable than a passcode, but it is easier to forward by accident.

**One examinee cannot sit twice at once.** If the link is opened while that
examinee already has the exam open elsewhere, the second attempt is refused. A
candidate whose browser crashed can reopen the same link and carry on.

**The link stops working when the exam does.** It expires three days after it is
sent, or shortly after the sitting ends when the examinee was mapped with a start
time. It also stops working once they have submitted, if you make the exam
invisible, or if you remove their mapping.

**Resending is safe.** A reminder email reuses the link already in the
examinee's inbox rather than replacing it, so the first email keeps working.

### When a link does not work

The examinee lands on the sign-in page for that exam with a message explaining
why, and can sign in with their code and passcode instead. That covers an
expired link, a link for an exam they are no longer mapped to, and a link opened
before the exam is due to start.

## Before you send

1. Send yourself a test first, using a test examinee mapped to the exam.
2. Check every placeholder resolved — a misspelled one is sent through as
   literal text.
3. Confirm the recipients are the roster you expect, on the exam's mapped list.
4. Check the start time and time zone in the message against the mapping.

## Next step

Continue with [Deliver, monitor, and report](deliver-monitor-report.md).
