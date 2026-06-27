# Sensing Up-Hierarchies — From Folder Agents to Distributed Workforce Intelligence

## 1. Opening

You're at a party. Someone asks what you do. You say you're looking for work — in sustainability, or digital transformation, or whatever your field is. It's a vulnerable moment. You're putting something out into a room full of people you barely know, hoping that someone knows something, someone has a connection, someone heard about an opening last week. Most of the time, nothing comes of it. Sometimes something does — and when it does, it feels like luck.

But it's not luck. It's sensing. You put a signal into a network and the network responded. The problem is that most of the time, the network is blind. Nobody in the room knows what to do with what you just said. The information goes nowhere. It doesn't compound.

Now imagine a different kind of network — one that is designed to sense, to remember, and to give back. Not a database. Not a job board. A living system where every conversation adds to a shared intelligence, where patterns emerge from hundreds of individual experiences, and where what the network learns flows back to the people who need it most.

This paper describes an attempt to build such a system — using folder-based AI architecture, a distributed coaching network, and a few ideas borrowed from cybernetics, process philosophy, and wine making.

---

## 2. The DAA and the Coaching Network

### The Organisation

The DAA (Deutsche Angestellten-Akademie) is one of Germany's largest providers of professional training and coaching. Across North Rhine-Westphalia, they run programs for people in career transition — professionals who have lost their jobs, are changing industries, or are re-entering the workforce after a break. The German Federal Employment Agency sends unemployed professionals to attend these programs with stipends, and DAA coaches work with them through a structured set of modules: improving resumes, articulating career paths, identifying strengths, and preparing for interviews.

The DAA's Research and Development department — the FuE team — is a 14-person interdisciplinary group whose mission they describe as "Forschung für Bildung": research for education. Their job is to recognize changes in society and the labor market early enough to develop relevant trainings and services. They focus on sustainability, artificial intelligence, and decent work. They already use AI in their research and have published a governance framework describing how they handle data privacy, the EU AI Act, and the ethical boundaries of AI-assisted research. Their core principle: "Humans decide, AI provides supporting work."

### What Coaches Actually Hear

I have been one of the coachees in this system. In my second session, my coach Martin told me something unexpected: he had coached several of my former colleagues. Through conversations with other coaches in the network, he had learned about a regional technology industry group that could be relevant for my search. He didn't get this from a database. He got it from the informal knowledge that circulates among coaches who talk to each other — the analogue version of compounding intelligence horizontally across an organization.

The coaches hear things every day that no labor market report captures. One of them gave me a tip: match the colors of your resume package to the brand colors of the company you're applying to. It sounded almost too simple. But I did it, and I got an interview invitation — my first in three months. Was it the colors? Maybe. Maybe it was one of a dozen other factors. But the point is: a coach who has seen hundreds of applications develop a feel for what works right now, not what worked last year. When a coach hears that tip confirmed by three different coachees who got interviews, it starts to become intelligence. When it stays in one coach's head, it stays an anecdote.

At any given time, each coach is working with up to twenty coachees in different stages of their process. Multiply that across twenty coaches in one state, and you have a network of four hundred people actively navigating the labor market — experiencing how employers behave, which skills get asked for, where the application process breaks down, what platforms work and which ones waste time. That is an extraordinary sensing apparatus. The question is: can we make it compound?

---

## 3. What If This Could Compound?

### Compound Engineering

One of the most useful ideas I encountered last year came from Kieran Klaassen, writing at Every.to about what he calls compound engineering. His central insight: each unit of work with AI should make subsequent work easier. Instead of starting fresh every time, the system learns from its mistakes and its successes. At the end of each working session, an agent writes down what it learned and saves it so that future sessions can build on that knowledge. This is not a new idea — it is why we have retrospectives in agile teams, after-action reviews in the military, and case conferences in medicine. What is new is making it systematic and machine-readable.

When Martin shared information from his colleagues about my former company, he was doing compound engineering by hand — horizontally, across the organization. What if that could happen at scale?

### ICM: The Folder as Agent Harness

Jake van Clief's Interpretable Context Methodology provides the mechanism. ICM uses the nested structure of folders — folders inside folders — to give AI agents the right information at the right time. Each layer answers a question: Where am I? What do I do here? What rules apply? What am I working with? The agent reads a routing file, understands its role, loads the relevant context, and works within defined boundaries. This minimizes token usage, improves context window management, and leads to more context-aware agent activity.

But here is what makes ICM interesting for organizations: it maps naturally onto how bureaucratic institutions already organize information. The DAA already has folder structures, templates, protocols, and governance documents. ICM doesn't ask them to adopt a new system — it asks them to make the system they already have machine-readable.

The challenge I set myself for this competition: what happens when ICM scales beyond a single user's workspace? What if we connect folder systems across an organization — coaches with their own workspaces, a shared intelligence layer, and a research team that synthesizes across all of it?

### The Nested Architecture

The system I'm describing has three layers:

**Layer 1 — The Individual Coach.** Each coach has a private workspace on their OneDrive. Their coachee notes, session protocols, and personal coaching style stay private. But at the end of relevant sessions, the coach can write an anonymized observation about what they're seeing in the labor market — not about the person, but about the market behavior the person is experiencing. "Three IT coachees this month report interviews going silent after the second round." No names, no companies, no identifying details. This is a signal.

**Layer 2 — Shared Intelligence.** Anonymized signals from all coaches flow into a shared SharePoint layer. Here, individual observations become organizational knowledge. One coach seeing interview ghosting is an anecdote. Five coaches across three cities seeing the same pattern is intelligence. This layer also holds pattern reports from compound routines and sensing prompts — questions the research team asks coaches to investigate.

**Layer 3 — The Researcher.** This is the competition deliverable: a folder-based AI researcher that synthesizes signals from the coaching network with external research — labor market statistics, policy developments, academic publications. It doesn't just summarize. It investigates: Where do the coaches' observations confirm the statistics? Where do they contradict them? Where are we not sensing at all?

Data protection is built into the architecture, not bolted on as policy. Personal data never leaves Layer 1. Signals are anonymized before sharing. The research team sees patterns, not people. Coaches are professionals contributing to organizational learning — their participation is voluntary, and the system is designed so that no coach should feel they are being monitored.

---

## 4. Up-Hierarchies — Sensing Flows Up, Context Flows Down

### The Body as Sensing System

Bonnitta Roy, a philosopher and educator whose POP-UP School has shaped much of my thinking, uses the term "up-hierarchy" to describe how distributed sensing leads to collective intelligence. The term comes from John Heron's work on participatory meaning-making, and Roy extends it with a powerful metaphor: the body itself is an up-hierarchy. Sensations arise locally — in the fingertips, in the gut, in the muscles — and flow upward to be integrated into awareness. The proximal layers, closest to the action, do the sensing. The distal layers, further from the action, do the integration.

The coaching network works the same way. Coachees are the fingertips — they touch the labor market directly. Coaches are the nervous system — they aggregate and interpret what multiple coachees are experiencing. The research team is the integrative layer — they see patterns across the whole body.

### The Danger: When Up Becomes Down

Roy is very specific about a risk: up-hierarchies can flip into down-hierarchies. This happens when the distal layer — where information becomes generalized and abstract — subsumes the agency at the proximal levels, where the actual sensing happens. Instead of decisions flowing upward as actions taken, they flow downward as instructions to be followed.

In the coaching context, this would mean the research team telling coaches what to look for instead of listening to what coaches are already seeing. It would mean standardized questionnaires replacing open conversation. It would mean the system becoming an extraction tool rather than a learning tool — sensing *from* coaches rather than sensing *with* them.

The DAA FuE team's own governance reflects an awareness of this risk. Their principle — "humans decide, AI provides supporting work" — is a structural defense against the flip. So is their concept of "slow lanes": dedicated time for reading, writing, and discussion as independent cognitive work, not mediated by AI. These are protections for what Roy would call the proximal layer — the place where actual understanding happens.

When the system works correctly, intelligence flows up *and* context flows back down — but as affordances, not instructions. Martin didn't receive a directive to tell me about the tech industry group. He received updated context from his network, and his professional judgment turned it into something useful for me. The coachee who finds that the resume color tip worked doesn't receive a mandate to use it. They receive a suggestion that came from the compounded experience of others who navigated the same terrain. The loop closes through action, not command.

---

## 5. Cybersyn — This Has Been Tried Before

In 1971, the British cybernetician Stafford Beer received an unexpected letter from Chile. Fernando Flores, a young engineer working for Salvador Allende's newly elected government, invited Beer to apply his cybernetic management models to the challenge of running a rapidly growing public sector. What they built together — Project Cybersyn — was a distributed sensing system at national scale.

The architecture was remarkably simple. Four hundred telex machines, found unused in a warehouse, were installed in factories across the country. Workers reported production data daily. The data was fed into a single mainframe computer running statistical software that detected significant deviations from expected patterns. When an anomaly appeared, it was routed to an Operations Room — a purpose-built space where decision-makers could see the state of the economy and act on it.

Three things about Cybersyn matter for what we're building:

First, when a national truckers' strike threatened to shut down the country in October 1972, the government repurposed the telex network — originally built for production monitoring — to coordinate emergency logistics. The sensing infrastructure became the action infrastructure. Two thousand messages a day flowed through the network, routing food, fuel, and transport to where they were needed most. The system that was designed to observe became the system that enabled response.

Second, Beer insisted that the workers themselves should design the models for their own factories. "Nobody is better qualified to design a factory than the man who has worked in it all his life." This is the same principle that drives our source-weighting rule: direct experience outranks statistical abstraction. The people closest to the action sense things that no report captures.

Third, the Operations Room was not a command center. It was a context layer — a space where decision-grade information was made visible to people who retained the authority to act on it. Beer was explicit: the system should enable freedom, not control. He called his earlier concept for it "the liberty machine."

The lesson for ICM: a flat reporting system — telex messages, or markdown files — becomes powerful only when it is embedded in an architecture that preserves local autonomy while enabling global sensing. The technology was simple. The architecture was what mattered.

*Reference: Eden Medina, Cybernetic Revolutionaries: Technology and Politics in Allende's Chile (MIT Press, 2011)*

---

## 6. The Researcher as Redistribution Orchestrator

### Applied Research Means Redistribution

The DAA FuE team practices applied research. Their purpose is not to produce knowledge for its own sake — it is to produce knowledge that changes practice. This means the researcher cannot just sense and synthesize. It must orchestrate redistribution in four directions.

**Upward:** Compound coach signals into pattern reports. Twenty individual observations about interview ghosting in IT become a documented trend with confidence levels and regional variation. Raw sensing becomes organizational intelligence.

**Outward:** Publish findings as briefings, articles, and policy papers. The FuE team already publishes in practitioner magazines like denk-doch-mal.de. The researcher helps produce different outputs for different audiences — a briefing for DAA leadership reads differently from an article for a policy journal or a post on LinkedIn. The team sits on a wealth of intelligence about workforce transitions, skills demand, and industry dynamics. Publishing this is both a public good and organizational positioning.

**Downward:** Design sensing prompts for coaches, update the tools and resources that coachees receive, propose adaptations to coaching methods, and develop new learning formats. When the research reveals that resume conventions have shifted, that insight needs to flow back to the coaches — and through them, to the coachees who are navigating those changes right now. This is where the up-hierarchy gives back. Not as instructions, but as updated context that coaches can use with their own judgment.

**Inward:** Feed back into the sensing system itself. This is action research — the researcher doesn't just observe, it intervenes. It designs a sensing prompt ("Ask your next five IT coachees specifically about what happens after the second interview round"), sends it to the coaching network, and then observes what comes back. Did the prompt surface new signals? Did it confirm or contradict the existing pattern? What should we ask next? Each cycle makes the sensing system smarter. Each cycle compounds.

Researchers who do more than summarize tend to use systems that help them make unexpected connections — the Zettelkasten method, tools like Obsidian or Roam Research, citation managers like Citavi. These tools work because they create a topology of ideas, not just a collection. One note links to another, and the connections reveal patterns that weren't visible when each note stood alone. The researcher folder system we've built does something similar at the organizational level: individual signals connect to patterns, patterns connect to the five-Ds analytical framework, and the framework connects to sensing prompts that generate new signals.

There is also something important happening at the intersection of complexity science and cognitive research around what some call anthropomorphic complexity — the study of how gathering people with very different perspectives leads to the emergence of genuinely new ideas. This matters because the goal is not to use AI to automate the world we already have, which is broken in many ways. The goal is to create learning systems that help us see differently. The diversity of the coaching network — coaches with different specializations, coachees from different industries and backgrounds — is not a data quality problem. It is the source of the system's intelligence.

---

## 7. The Evaluative Layer — What Makes Intelligence Alive

### The Winemaker

A winemaker is deeply connected with their environment — sometimes over generations. There is a deep co-variance with the fields, the grapes, the climate, the water, and also the press, the barrels, and the taste of the customers. It would be impossible to context-engineer a text file that simulates this connection. The French call it *terroir* — the untransferable intelligence of a place, the combination of soil, slope, microclimate, and accumulated seasons of practice that gives a wine its character. You can describe terroir. You cannot reproduce it from the description.

Intelligence is like this. It arises from an environment and the assemblage of co-interacting parts that creates an awareness of the world — an awareness that leads to movement through it. This is an age-old question, and when we look at stories like Frankenstein we see our collective fascination with creating intelligent beings from assembled parts. I don't have a definitive answer to what intelligence is. But I know it does not live in files.

The practice of context engineering — the work of structuring information so that an AI can respond more usefully — is an attempt to share enough of the situation that the agent can orient itself. ICM does this well. But there is a layer that context engineering struggles to capture: the evaluative layer.

Bonnitta Roy's theory of Global State Naturalized View describes evaluative fields not as overlays on top of reality but as causal forces within it. What an organization values, what it fears, what it considers success — these are not soft data. They shape which decisions are made, which knowledge is sought, and which futures remain reachable. Roy points out that Palantir's Foundry — perhaps the most sophisticated organizational ontology system in the world — treats this layer as nonexistent. The system sees structure and executes schema, but the normative, social, political, and purpose-driven forces that actually shape decisions are treated as someone else's problem.

Think about Google Maps for a moment. There is the street map view — roads, addresses, directions. And then there is the topographic view, where you can read the lay of the land — the valleys, the ridges, what is traversable and what is not. An ontology is like the street map: it shows you what exists and how things relate. The evaluative layer is the topography: it shows you what is reachable from where you are, and with what effort, and toward what purpose.

**Applied to workforce intelligence:** When a coach hears "this process worked for me because I did this thing," the evaluative shape is present — what mattered, what enabled action, what constrained it. When that becomes a flat markdown signal entry stripped of context, the evaluative layer is lost. The signal becomes data about the market, not intelligence about what is possible.

The DAA FuE team's own published work identifies this tension precisely. They recognize the risk that outsourcing memory, structuring, and synthesis to AI may narrow attention spans and reduce genuine deliberation. This is the down-hierarchy flip described in evaluative terms — when the distal layer of AI synthesis subsumes the proximal layer of human judgment. Their defense: "slow lanes," dedicated time for reading, writing, and discussion as independent cognitive work. Governance that keeps ethical deliberation and final clearance with humans. These are structural protections for the evaluative layer — for the part of intelligence that cannot be automated without destroying it.

### Terroir: The Topology ICM Needs

This is why I am building Terroir — a software tool that creates ontological knowledge graphs as minimum viable world models. Terroir maps not just the elements and relationships of a domain, but also the evaluative layer: what is valued, what is feared, what is in tension. Agents can traverse the graph to read the topology and the forces shaping it. Like tools such as InfraNodus, it can surface what is missing — what is not connected, what questions have not been asked, where the gaps in sensing lie.

ICM gives the agent a methodology — how to think. Terroir gives it a topology — what is connected to what, and what moves are possible. The researcher folder stays flat and portable: you can drop it into any Claude Project and it works. But through an MCP server, the agent can reach into Terroir for the relationships and evaluative gradients that markdown cannot represent. The folder is the harness. The graph is the landscape the harness lets you navigate.

*References: Roy (2026), GSNV; Ciesinger & Mielke, "KI in der Praxis," denk-doch-mal.de*

---

## 8. What a Folder Can Become

A folder is a surprisingly powerful thing. ICM shows that a well-structured folder can give an AI agent methodology, judgment, and domain expertise. It maps naturally onto how organizations already work — templates, protocols, governance documents, nested structures. It is portable, reproducible, and readable by humans and machines alike.

But the folder is the harness, not the intelligence.

The intelligence lives in the sensing network — in the proximal observations of people navigating the labor market every day, in the professional judgment of coaches who see patterns across hundreds of conversations, in the evaluative fields that shape what is possible and what is foreclosed. No folder captures this fully. But a folder can orchestrate it — channeling sensing upward, routing context downward, compounding what is learned so that each cycle makes the next one smarter.

Stafford Beer showed fifty years ago that simple technology, embedded in the right architecture, can turn a flat reporting system into a living intelligence network. The technology was telex machines. Ours is markdown files and AI agents. The architecture is what matters: preserving autonomy at every layer, weighting experience over abstraction, and ensuring that the system gives back more than it takes.

This is an entry for a folder-building competition. But the folder points at something larger: the possibility that organizations like the DAA — with their distributed coaching networks, their research teams, their commitment to understanding a changing world — could become sensing organisms. Not by installing new technology, but by making the intelligence they already carry visible, connectable, and alive.

---

## Bibliography

- Ciesinger, K.-G. & Mielke, S. "KI in der Praxis: Wie die Abteilung Forschung und Entwicklung der DAA NRW Künstliche Intelligenz im Alltag nutzt." *denk-doch-mal.de*, 2025.
- Heron, J. *Co-operative Inquiry: Research into the Human Condition.* Sage, 1996.
- Klaassen, K. "Compound Engineering." *Every.to*, 2025.
- Medina, E. *Cybernetic Revolutionaries: Technology and Politics in Allende's Chile.* MIT Press, 2011.
- Roy, B. "A New Theory of the Body: Up-hierarchy." *POP-UP School / Substack*, 2022.
- Roy, B. "How to Think About War: Palantir's Foundry Approach is Lacking One Crucial Layer." *GSNV / Substack*, 2026.
- Simon, H. "The Architecture of Complexity." *Proceedings of the American Philosophical Society*, 1962.
- van Clief, J. *Interpretable Context Methodology (ICM).* 2025.
