---
id: source-auditable-ai-book-proposal
title: "SOURCE B — Auditable AI: Original O'Reilly Book Proposal (verbatim)"
topic: ai-understanding-layer
type: literature
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [source-material, verbatim, evidence-gated-ai, book-proposal]
source_kind: primary-verbatim
---

> **Verbatim capture — do not edit, correct, or reword.**
> This file preserves Source B exactly as supplied by the author, including the
> full Author Nationality Disclosure Form. It is historical source material for
> the `ai-understanding-layer` topic, not a polished draft. Analysis lives in
> `../notes/`.
>
> **Redaction note (2026-08-23):** This repository is public. The author's
> mailing address, phone number, and email address, originally present in
> the "Preferred email address(es)" / "Mailing address(es)" / "Phone
> number(s)" fields below, were redacted by explicit author instruction
> before this file was first committed. No other content was altered.

---

## SOURCE B — Original Auditable AI Book Proposal

# Book proposal

Proposed book title: Auditable AI: Building Evidence-Based Systems That Can Be Trusted

Subtitle: From Black Box Models to Decision-Level Enforcement in Production AI

Author(s): Monika Dvořáčková

Author title(s) and affiliation(s): ML/AI Engineer focused on NLP, MLOps, and AI Governance, Independent / Startup (GovAI)

Author pronouns: She/her

Mailing address(es): [redacted]

I will be contracting as an individual. No LLC or other entity will be used.

Phone number(s): [redacted]

Preferred email address(es): [redacted]

In light of the above, you hereby declare that you are a national of the following country:

Czech Republic.

---

**About the author(s)**

*Monika Dvořáčková is an AI engineer specializing in NLP, MLOps, and AI governance. She holds degrees in mathematics and law and is currently pursuing advanced legal studies focused on technology and regulation.*

*Her work focuses on bridging the gap between machine learning systems and real-world accountability. She is the creator of GovAI, a system designed to enforce auditability and decision-level control in AI pipelines. Her work combines engineering, regulatory thinking, and system design to address one of the most critical challenges in modern AI: making AI systems controllable, auditable, and deployable in production environments.*

*She also teaches AI and machine learning, helping engineers move from experimental models to production-grade systems.*

*LinkedIn profile:* *https://www.linkedin.com/in/monika-dvorackova/en?originalSubdomain=at*

---

## Marketing description

Most AI systems fail in production not because of poor models, but because they lack a mechanism to control and verify decisions. Model outputs are routinely treated as decisions without enforceable validation, structured evidence, or accountability.

*Auditable AI* introduces the Evidence-Gated AI framework, a system for enforcing decision-level auditability through structured evidence and deterministic CI-based controls. Instead of focusing on model performance alone, this book shows how to design AI systems where every decision is validated, traceable, and enforceable before it is allowed into production.

This book moves beyond abstract discussions of AI ethics and governance and provides concrete, implementable mechanisms for building production-grade AI systems that can withstand real-world scrutiny in regulated and high-stakes environments.

---

## About the topic

The book focuses on decision-level auditability in AI systems—a missing layer in most modern ML architectures. While significant attention has been given to model performance and explainability, there is a critical gap in how decisions made by AI systems are validated, approved, and enforced.

The approach is grounded in system design and supported by controlled failure experiments and an audit of real-world ML repositories, demonstrating systematic gaps in auditability and enforcement.

This topic is increasingly important due to regulatory pressure, enterprise adoption of AI, and the need for accountability in automated systems. Without auditability, AI systems cannot be reliably deployed in regulated or high-risk environments.

---

## Audience

Level. *Please select from this drop-down list of levels:* Intermediate to Advanced

The primary audience consists of:

* AI engineers
* ML engineers
* MLOps engineers
* Technical leads and architects

These readers are already familiar with:

* Python and ML frameworks
* Model training and evaluation
* Basic MLOps concepts

They are transitioning toward:

* production systems
* system reliability
* governance and compliance

They may have read books on MLOps, deep learning, or practical machine learning but lack a framework for auditability and enforcement.

### Market size

AI adoption is rapidly increasing across industries, with enterprise AI spending projected to grow significantly in the coming years. However, most organizations struggle with deploying AI in production due to reliability and governance issues.

This book targets a growing segment of engineers working on production AI systems, especially in regulated industries such as finance, healthcare, and government.

---

### Usage scenarios

* Engineers designing production AI systems will use this as a design reference
* Teams implementing governance will use it as a framework guide
* Technical leaders will use it to evaluate system readiness

Readers will likely:

* read it once to understand the framework
* repeatedly return to specific chapters during implementation

---

# What the reader will learn—and how to apply it

By the end of this book, the reader will understand:

* Why most AI systems fail in production despite good model performance
* The difference between model-level and decision-level architecture
* What auditability means in practical, system-level terms
* Why governance without enforcement does not work

And the reader will be able to:

* Design AI systems with a decision layer
* Implement evidence-based validation mechanisms
* Introduce CI-based enforcement into AI pipelines
* Build systems that meet real-world audit and compliance requirements

---

## Keywords

* AI governance
* MLOps
* AI auditability
* decision systems
* machine learning systems
* CI/CD for AI
* AI compliance
* evidence-based AI
* model validation
* AI risk management

---

## Other book features

GitHub: Yes (reference implementation + examples)

### Sandbox: Yes

### Sandbox name: Evidence-Gated AI Lab

### Environment: Python

---

## Software dependencies

*Python*

*ML frameworks (PyTorch, Transformers)*

*CI/CD tools (GitHub Actions)*

---

## Competing titles

### 1. *Atlas of AI*, Kate Crawford, Yale University Press, 2021

Focuses on social and political implications of AI.

Difference: This book is technical and implementation-focused.

---

### 2. *Designing Machine Learning Systems*, Chip Huyen, O'Reilly, 2022

Focuses on ML system design and MLOps.

Difference: Does not address auditability or enforcement mechanisms.

---

### 3. *Machine Learning Engineering*, Andriy Burkov, 2020

Covers ML lifecycle and engineering practices.

Difference: Lacks decision-level control and governance enforcement.

---

## Related O'Reilly titles *What O'Reilly book(s) cover similar topics or related technology?*

* Designing Machine Learning Systems
* Practical MLOps
* Reliable Machine Learning

---

**Book outline**

Chapter 1: Why AI Systems Fail in Production

Understanding the gap between model performance and system reliability

Chapter 2: The Missing Layer — Decision Systems

Defining decision-level architecture

Chapter 3: From Outputs to Decisions

Why model outputs are not decisions

Chapter 4: Evidence as a First-Class Concept

Designing structured evidence in AI systems

Chapter 5: Auditability as a System Property

What it means and how to achieve it

Chapter 6: Enforcement — Making Rules Real

Why policies fail without enforcement

Chapter 7: CI Gates for AI Systems

Implementing enforcement in pipelines

Chapter 8: Approval and Risk Review

Human-in-the-loop as a controlled mechanism

Chapter 9: System Architecture

Putting all components together

Chapter 10: Controlled Failure Experiments

Demonstrating system behavior under failure

Chapter 11: Real-World Use Cases

Finance, compliance, and government

Chapter 12: Future of Auditable AI

Standards, regulation, and industry direction

---

## Specs and schedule

*Estimated length: 250–300 pages*

*Illustrations: Architecture diagrams (important)*

*Schedule (realistic but ambitious):*

* *Two draft chapters: 6–8 weeks*
* *Half manuscript: 4 months*
* *Full draft: 6 months*
* *Final: 8–9 months*

---

Author Nationality Disclosure Form

Certain local laws, rules and regulations in countries where O'Reilly operates as a business or publishes its books require the disclosure of an author's nationality as a part of the fulfillment of copyright registration and other requirements associated with the publication of books and editorial works in those countries.

In light of the above, you hereby declare that you are a national of the following country: Czech Republic.

You acknowledge that your nationality information will be processed in accordance with the O'Reilly Privacy Policy for the exclusive purpose of allowing the publication of the Work in countries where disclosure of an author's nationality is required. Your nationality is necessary for us to give full execution to the contract between you and O'Reilly. The provision of this information is mandatory for the translation and publication of your work in regions and countries where the disclosure of authors' nationalities is a compulsory requirement.

Please note that O'Reilly may disclose it to third parties including local and national authorities, agencies and other public organizations as necessary to comply with applicable legal and regulatory requirements.
