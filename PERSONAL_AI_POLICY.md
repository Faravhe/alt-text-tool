# Personal AI Policy

**Owner:** Tauhidul Islam
**Version:** 1.0 — Draft
**Last updated:** July 22, 2026
**Framework reference:** Dakan & Feller, *Framework for AI Fluency* (Delegation, Description, Discernment, Diligence)

---

## 1. Purpose

This document defines how I will work with AI tools (including Claude) across personal projects, professional development, and any work I eventually share or open-source. It exists so that my use of AI is consistent, defensible, and something I can hand to an employer, collaborator, or reviewer without hesitation.

---

## 2. Scope — When and How I Work With AI

| Context | AI's role | My role |
|---|---|---|
| Technical / debugging questions | Diagnose, explain, suggest fixes | Verify fixes actually work before relying on them |
| Feedback on my own projects | Give critical, constructive assessment | Decide what to act on; AI opinion is advisory, not final |
| Connecting local ↔ remote (e.g. GitHub) | Draft commands/config, explain what each step does | Run the commands myself, review before pushing anything public |
| Resume / career materials | Draft, restructure, suggest phrasing | Final wording, all factual claims, all accomplishments must be mine and true |
| Project sharing / portfolio building | Help polish presentation, docs, READMEs | Own the substance; disclose AI involvement (see §6) |

**General rule:** AI is a collaborator for *drafting, explaining, and reviewing* — not a replacement for my own understanding or final sign-off on anything that leaves my hands.

---

## 3. Boundaries — Personal Information & Data Restrictions

- **No real personal data** (mine or anyone else's) goes into prompts, test datasets, or example inputs — this includes real names, addresses, contact info, financial details, health information, or identifying details of real people.
- **No real user data**, even anonymized-in-appearance, is used for testing AI-assisted tools — synthetic/dummy data only.
- **No credentials, API keys, or tokens** are ever pasted into a prompt, even for debugging — I'll redact and describe the error instead.
- If a project eventually needs real data (e.g. a user testing phase), that requires a separate, explicit consent and data-handling process — not covered by this default policy.

---

## 4. Review Standard — My Role as QA

I act as the **system admin / quality control reviewer** for all AI-assisted work. Before anything is used, shared, submitted, or deployed:

1. I read and understand every piece of code, text, or config I'm using — no blind copy-paste.
2. I test/run it myself in a controlled environment before trusting the output.
3. I check factual claims (especially in resumes, project descriptions, or anything citing sources).
4. I confirm nothing violates §3 (no real data) or §5 (ethics) before it goes further.

---

## 5. Ethical Boundaries

- **Attribution:** I will not present AI-assisted or AI-generated work as entirely my own without disclosure (see §6). Sources, datasets, and prior work I build on will be properly cited.
- **Legality:** I will not use AI assistance to plan, build, or execute anything illegal, regardless of framing (educational, hypothetical, etc.).
- **Harm to others:** I will not share information with an AI model that could cause harm if misused (e.g. real personal data, security vulnerabilities in systems I don't own, content that could be repurposed maliciously).
- **Bias & fairness:** For any project involving real users (esp. accessibility-focused work), I will actively check outputs for bias, exclusion, or inaccuracy before relying on them.

---

## 6. Disclosure — How I'll Communicate AI Involvement

Disclosure isn't one-size-fits-all. Here's my working standard, adapted from the Diligence competency (Transparency + Deployment):

| Audience | Default disclosure level | Example |
|---|---|---|
| **Interviewers / employers** | Full, proactive disclosure of AI use in process and output | "I used Claude to help debug and structure this project; all design decisions, testing, and final code review were mine." |
| **Collaborators / teammates** | Full disclosure, in-line where relevant | Comment in code or doc: "AI-assisted draft, reviewed by [name]." |
| **End users (if project is public/open-sourced)** | General disclosure in README or About page, not per-line | A short "AI & Tools Used" section describing what was AI-assisted and what wasn't. |
| **Casual/personal use (notes, brainstorming)** | No disclosure needed | Internal use only, not shared externally. |

### When more detailed disclosure is appropriate
Escalate beyond the general baseline when:
- The work involves **real people's data or wellbeing** (e.g. accessibility tools, anything used by vulnerable users)
- The audience is **evaluating my individual skill/judgment** directly (job interviews, academic submissions)
- The content could be **mistaken for fully human-verified fact** (research summaries, citations, claims of accuracy)
- Local laws, employer policy, or a platform's terms **require it**

---

## 7. Attribution & Transparency Templates

**For a README / project page:**
> This project was built with AI assistance (Claude, Anthropic) for [drafting code / debugging / writing documentation / etc.]. All architecture decisions, testing, and final review were done by Islam. AI-generated content has been reviewed for accuracy and originality.

**For a resume / portfolio blurb:**
> Developed using an AI-assisted workflow (Claude) for [specific task, e.g. "prototyping and technical writing"]; independently designed, tested, and validated all outcomes.

**For inline code/doc comments:**
> <!-- AI-assisted draft (Claude), reviewed and modified by [name], [date] -->

**For citing AI in academic-style or research-adjacent writing:**
> Portions of this document were drafted with assistance from Claude (Anthropic). All claims, sources, and conclusions were independently verified by the author.

---

## 8. Decision-Making Criteria for Ethical Dilemmas

When I hit a gray area not clearly covered above, I'll run it through these questions in order:

1. **Legality** — Is this legal, unambiguously? If no → stop.
2. **Consent** — Does this involve anyone's data or likeness without their knowledge/consent? If yes → stop or get consent first.
3. **Harm potential** — Could this output cause harm if misused, leaked, or taken out of context? If yes → don't proceed without mitigation.
4. **Reversibility** — If I'm wrong about this being okay, can I undo it (unpublish, retract, correct)? If not → higher bar for proceeding.
5. **Transparency test** — Would I be comfortable explaining this decision, in full, to an interviewer, a user, or a journalist? If not → reconsider.
6. **Attribution check** — Am I claiming credit for something I didn't actually do or verify? If yes → fix the disclosure before proceeding.

If a situation fails any of these, I pause and either redesign the approach or don't proceed.

---

## 9. Stakeholder-Specific Statements

Pre-drafted starting points for different audiences — to be adapted per project:

**To an interviewer:**
> I use AI tools like Claude as a collaborator for technical drafting, debugging, and feedback — not as a substitute for understanding my own work. I can walk through any part of this project's logic or decisions without relying on the AI.

**To future employees/collaborators (if I lead a team):**
> AI-assisted work is welcome and expected, but every contributor is responsible for reviewing, testing, and understanding what they submit — "the AI wrote it" is not an acceptable explanation for an error.

**To possible users (if a project goes public/open source):**
> This tool was built with AI assistance under human review at every stage. If you notice an error, bias, or issue, please report it — accessibility and accuracy are actively maintained, not just AI-generated once and left alone.

---

## 10. Review Cadence

This policy is a living document — I'll revisit it:
- Before any project is shared publicly or open-sourced
- Before submitting a job application referencing AI-assisted work
- Any time I encounter a situation this document doesn't clearly cover (and I'll add that case once resolved)
