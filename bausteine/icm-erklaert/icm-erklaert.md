# ICM erklärt — das tiefe Material

> Wiederverwendbarer Erklär-Baustein. Quelle für Briefe, Slides, Gespräche.
> Tiefe nach Publikum dosieren: Führungskräfte → nur „Grundidee" + „Sie arbeiten bereits so".
> F&E / IT / interessierte Coaches → die Anordnung, das Routing und der Ordnerbaum dazu.
> Grundlage: Interpretable Context Methodology (ICM) / Model Workspace Protocol (MWP),
> Jake van Clief & David McDermott, University of Edinburgh. Open Source (MIT).

---

## Die Grundidee in einem Satz

Statt KI-Verhalten in Software zu programmieren, wird es in **Ordnern, nummerierten
Schritten und einfachen Textdateien** festgehalten. Die KI liest die richtige Datei im
richtigen Moment — und weiß dadurch, welche Rolle sie in welchem Schritt spielt.

- Die **Ordnerstruktur** ist die Steuerung.
- Die **Textdateien** sind die Anweisungen.
- Der **Mensch** entscheidet an jedem Schritt.

Was sonst ein Software-Framework im Code regeln würde — welcher Schritt wann kommt, welche
Information die KI bekommt, wo das Ergebnis landet — übernimmt hier die Anordnung der Ordner.
Alles bleibt lesbar und änderbar, von jeder Person mit einem Texteditor.

---

## Warum das für Organisationen besonders gut passt: Sie arbeiten bereits so

Organisationen organisieren ihre Arbeit seit jeher in Ordnern: pro Vorgang eine Akte,
Vorlagen an einem festen Platz, Schritte nach Reihenfolge sortiert. ICM verlangt keine neue
Denkweise und kein Umlernen — es ist **dieselbe Arbeitsweise, nur klüger angeordnet, sodass
eine KI mitlesen kann.** Geringe Hürde beim Einführen: keine Plattform, keine Oberfläche —
Dateien in Ordner legen wie immer, ein Leitfaden im Ordner sagt der KI, was sie damit tun soll.

---

## Vier einfache Prinzipien

1. **Ein Schritt, eine Aufgabe.** Nummerierte Ordner (01, 02, 03 …) sind die Schritte. Jeder
   erledigt genau eine Sache, nicht alles auf einmal. Das macht jeden Schritt überschaubar
   und überprüfbar. *(Unix: „do one thing well" / Parnas: information hiding.)*
2. **Klartext als Sprache.** Anweisungen sind normale Textdateien in verständlichem Deutsch —
   keine Programmierung. Wer einen Text bearbeiten kann, kann das Verhalten der KI anpassen.
3. **Nur der nötige Kontext.** In jedem Schritt sieht die KI nur die Dateien dieses Schritts —
   nicht den ganzen Berg. Das hält die KI fokussiert, die Ergebnisse präziser und schützt
   nebenbei sensible Daten, die woanders liegen. *(„Lost in the middle": weniger irrelevanter
   Kontext = bessere Ergebnisse.)*
4. **Der Mensch entscheidet.** Zwischen zwei Schritten liegt immer eine Kontrollstelle. Die KI
   schlägt vor, der Mensch prüft, korrigiert und gibt frei. Nichts läuft unbeaufsichtigt durch.

---

## Die Anordnung: fünf Ebenen — von „Wo bin ich?" bis „Womit arbeite ich?"

Die obersten Ebenen sind **Wegweiser** (sie lenken), die unteren **Inhalt** (Wissen und
Arbeitsmaterial). Die KI lädt immer nur, was sie gerade braucht.

| Ebene | Datei | Frage | Rolle |
|-------|-------|-------|-------|
| 0 — Identität | `Anleitung.md` / `CLAUDE.md` | „Wo bin ich?" In welchem Ordner stecke ich, was enthält er? | Wegweiser |
| 1 — Routing | `CONTEXT.md` | „Wohin gehe ich?" Für diese Aufgabe ist Schritt X zuständig. | Wegweiser |
| 2 — Der Schritt | `Schritt-Anleitung.md` | „Was tue ich?" Was lese ich, was mache ich, was schreibe ich? | Wegweiser |
| 3 — Wissen | `referenz/ …` | „Welche Regeln gelten?" Vorlagen, Standards, Marktwissen. Bleibt stabil. | Inhalt |
| 4 — Arbeit | `ergebnisse/ …` | „Womit arbeite ich?" Der konkrete Fall. Ändert sich jedes Mal. | Inhalt |

**Das Bild dazu:** Ebene 3 ist die *Fabrik* — die Regeln und Vorlagen, einmal eingerichtet,
immer gültig. Ebene 4 ist das *Produkt* — das, was die Fabrik bei jedem Durchlauf neu
herstellt. Ein gutes Rezept (Ebene 3) plus die jeweiligen Zutaten (Ebene 4) ergibt jedes Mal
ein passendes Ergebnis. So bleibt der Kontext pro Schritt klein (typisch 2.000–8.000 Tokens)
statt eines 40.000-Token-Bergs, in dem die KI das Wesentliche übersieht.

---

## Routing in normaler Sprache: „Ich möchte … → gehe zu …"

Das Herzstück ist eine schlichte Tabelle in einer Textdatei. Sie sagt der KI (und jedem
Menschen), welcher Ordner für welche Aufgabe zuständig ist.

| Ich möchte … | Gehe zu Ordner |
|--------------|----------------|
| Ein Erstgespräch-Protokoll vorbereiten | `01_Erstgespräch/` |
| Einen Lebenslauf strukturiert prüfen | `02_Bewerbungstool/` |
| Auf ein Vorstellungsgespräch vorbereiten | `03_Interview-Coach/` |
| Eine Marktbeobachtung festhalten | `Marktwissen/` |
| Etwas an Teilnehmende übergeben | `Coachee-Ordner/` |

**Strukturierte Daten statt loser Notizen:** Ergebnisse werden als geordnete Textdateien
(Markdown und JSON) abgelegt. Der nächste Schritt verarbeitet sie sauber weiter, ein Mensch
kann jederzeit hineinschauen. Kein verstecktes Format, keine Blackbox, keine Programmbindung.

---

## Anbieter-unabhängig

ICM ist eine **Methode, keine Plattform**. Die Ordner und Leitfäden funktionieren mit jedem
KI-Werkzeug, das Textdateien lesen kann. Ändert sich die Technik, ziehen die Ordner mit.

| Werkzeug | Wie ICM darin läuft |
|----------|---------------------|
| Microsoft 365 | SharePoint / OneDrive + Copilot |
| ChatGPT | Projekte + hochgeladene Dateien |
| Anthropic Claude | Projekte + `CLAUDE.md`-Leitfaden |

---

## Umsetzungs-Skizze mit Microsoft

Eine ganz normale SharePoint- oder OneDrive-Bibliothek, in der jeder Ordner ein Schritt ist
und jeder `.md`-Leitfaden Copilot sagt, was zu tun ist:

```
Talentcenter/                  # SharePoint-Bibliothek
├── 00_Anleitung.md            # Ebene 0 — Copilot liest das zuerst
├── CONTEXT.md                 # Ebene 1 — Routing: „Ich möchte … → gehe zu …"
├── 01_Erstgespräch/
│   ├── Anleitung.md           # Ebene 2 — was tun in diesem Schritt
│   ├── Vorlagen/              # Ebene 3 — Protokoll-Vorlage (bleibt stabil)
│   └── Ergebnisse/            # Ebene 4 — ausgefülltes Protokoll (pro Fall)
├── 02_Bewerbungstool/         # Lebenslauf strukturiert prüfen & verbessern
├── 03_Interview-Coach/        # auf Vorstellungsgespräche vorbereiten
├── Wissen/                    # Bewerbungsstandards, Arbeitsmarkt (Ebene 3)
└── Coachee-Ordner/            # Übergabe an Teilnehmende
```

Eine Coachin öffnet `01_Erstgespräch`, bittet Copilot „bereite das Protokoll vor" — und
Copilot weiß aus dem Leitfaden, welche Vorlage es nimmt, welche Fragen es stellt und wohin
das Ergebnis kommt. Dieselbe Person, dieselbe vertraute Ablage — nur dass jetzt eine KI
mitarbeitet, ohne dass jemand eine neue Software lernen musste.

---

## Im Zentrum stehen Menschen, nicht die Technik

- **Coaches:** behalten die Kontrolle, gewinnen Zeit. KI nimmt die Routine ab; mehr Zeit für
  Zuhören, Ermutigen, Begleiten. Die KI ersetzt das Urteil nie.
- **Mitarbeitende:** keine neue Software, keine Überforderung. Arbeit mit Ordnern wie bisher.
- **Teilnehmende (oft in fragiler Lage):** Würde und Klarheit. Jeder Schritt ist sichtbar,
  nachvollziehbar, korrigierbar — keine Blackbox bei Menschen in sensibler Lebensphase.

Weil jedes Zwischenergebnis eine lesbare Datei ist, ist nichts versteckt. Das deckt sich mit
der Forderung des EU AI Act nach menschlicher Aufsicht bei sensiblen Anwendungen — und mit
dem, was Menschen in Unsicherheit brauchen: das Gefühl, dass jemand mitschaut.
