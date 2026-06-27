# Demo Run-Sheet: Step Into More (target 5:00)

> A screen-recording script for the Comp #8 demo. Each scene has: what to show, the line to say, and
> the exact prompt to paste so every take is clean. Open on the landing page, close on it.
> Names on screen match the landing page: Coach, Marketing Maker, Lead-Researcher, Connector.

## Before you record (2-minute prep)
- Open tabs/windows ready: the landing page (`ace-client-finder.lovable.app`), the repo in your editor,
  the cockpit (`business-dev/lead-research/output/pipeline-board.html`) in a browser, `commons/roundtable.md`.
- Set the cockpit to a "mid-motion" state: one card in **Drafted** you will move to **Sent** on camera.
- Have a Claude session open with the repo folder. To run an agent, tell it:
  *"Act as the <agent> defined in <path>. <prompt>."*
- Record at 1080p, one scene per take, stitch after. Pause a beat on the two "wow" moments
  (the Commons pickup, the card moving).

---

## 0:00 to 0:20 · Cold open (landing page)
**Show:** the landing page, slow scroll past "Not a hero. A team that gets you your first client."
**Say:** "This is Step Into More. The promise is simple: not a hero, a team that gets me my first
client. Let me show you that team actually working."

---

## 0:20 to 0:50 · The map
**Show:** `CLAUDE.md`, then a quick pan of the folders (positioning-canon, first-client-coach,
marketing, business-dev/lead-research, business-dev/warm-network, commons).
**Say:** "Behind the page is a folder system. One canon everyone reads, four specialists, a Commons
where they talk, and a human at every gate. All plain text. The intelligence is in the words."

---

## 0:50 to 1:35 · The Coach (the differentiator)
**Show:** the Claude session running the Coach.
**Paste this prompt:**
> Act as the First-Client Coach defined in first-client-coach/identity.md and rules.md.
> Here's my week: big one. I want to hit ten cold leads, finish the flyer, and send three follow-ups. Let's just go, give me the list.

**What to highlight on screen:** the Coach does not dump a list. It does the work, then names a
pattern and offers the warm door, and it references the Terroir read of the practice.
**Say:** "Most first-client coaches are pure tactics. This one watches how I work and meets the human
underneath. It earned that read across sessions; it didn't x-ray me on day one."

---

## 1:35 to 2:20 · Lead-Researcher + the pipeline moving
**Show:** the Claude session running the Lead-Researcher, then the cockpit in the browser.
**Paste this prompt:**
> Act as the Lead-Researcher defined in business-dev/lead-research/CLAUDE.md.
> Qualify this lead and draft a first outreach: a mid-sized AVGS provider in Aachen with an active "KI in der Weiterbildung" page. Score it with the rubric, then draft.

**Then:** switch to the cockpit, move the prepared card from **Drafted** to **Sent**, refresh.
**Say:** "It researches, scores with the rubric, and drafts. I send. Watch the card move. The two
irreversible actions, sending and booking, always wait for me."

---

## 2:20 to 3:05 · The Commons (how they talk)
**Show:** `commons/roundtable.md` on screen the whole time.
**Step 1, paste (as Lead-Researcher):**
> Post your handoff to commons/roundtable.md: you need a one-page ICM explainer for the AVGS segment to attach to warm replies. Add it to Open Handoffs.

**Step 2, paste (as Marketing Maker):**
> Act as the Marketing agent defined in marketing/specialist/identity.md. Read commons/roundtable.md, pick up the open handoff addressed to you, check its box, and start the one-pager.

**What to highlight:** the file changes on screen, the box gets checked, the handoff is picked up.
**Say:** "This is how they learn about each other's work. Not a group chat, a shared round table they
read first and write to last. One agent asks, another picks it up."

---

## 3:05 to 3:50 · The Marketer doing real work
**Show:** the Marketing Maker reviewing the sample Substack draft.
**Paste this prompt:**
> Act as the Marketing agent. Review this Substack draft for SEO and for voice. The title is "How educational providers can use AI tools." Make it take a stand, the boutique way.

**What to highlight:** it flags the safe title, rewrites the opener to lead with a real position
("Die meisten KI-Beratungen verkaufen Ihnen neue Software. Ich nicht."), in a distinct voice.
**Say:** "It won't let me be safe. Boutiques win by taking a position, not by sanding off the edges."

---

## 3:50 to 4:40 · The payoff loop (friend pilot to website quote)
**Say first (honest framing):** "Here's how the loop closes. Say I run a free pilot with a friend and
we build a folder system together."
**Paste this prompt:**
> Act as the Marketing agent. I just finished a free pilot with a friend: we built a small ICM folder system for her coaching practice in an afternoon, and she said it finally made her AI feel like it knew her clients. Turn her experience into a short, honest website testimonial quote (German), no hype, and tell me where it goes on the page.

**Then:** cut to the landing page and drop the quote in.
**Say:** "Warm pilot, real proof, a marketing asset, and it lands on the page I opened with. The loop
closes."

---

## 4:40 to 5:00 · Close
**Show:** the landing page, then a title card with the two URLs.
**Say:** "From a scattered founder to a repeatable path to the first paid yes, with a human at every
gate. That's Step Into More."
**On screen:**
- Repo: github.com/jacksoncalling/step-into-more
- Live: ace-client-finder.lovable.app

---

## Reset between takes
- Cockpit: move the demo card back to **Drafted**.
- Commons: revert `roundtable.md` (keep a clean copy `roundtable.demo-start.md` to restore from).
- Clear the Claude session so the Coach's "first contact" reads fresh.

## If you overrun 5:00
Cut in this order: trim the map (0:20) to 15s, then merge the Marketer scene into the Commons pickup
(the one-pager handoff IS the marketer working). Protect the Coach, the moving pipeline, and the
closing loop. Those three carry the story.
