# [WORKSPACE-NAME] — Anleitung (Ebene 0)
> Ebene-0-Gerüst. Diese Datei liest die KI (Copilot / ChatGPT / Claude) **zuerst**.
> Sie beantwortet: „Wo bin ich, was enthält dieser Ordner, wohin gehe ich?"
> Platzhalter in [ECKIGEN KLAMMERN] ersetzen, Hinweiszeilen (`>`) am Ende löschen.

## Wo bin ich
Dies ist der Arbeitsbereich **[WORKSPACE-NAME]** für **[ORGANISATION / TEAM]**.
Zweck: [in einem Satz, was hier passiert].

## Wie ist es aufgebaut
- Nummerierte Ordner (`01_…`, `02_…`) = die Schritte, in Reihenfolge.
- In jedem Schritt: `Anleitung.md` (was tun), `Vorlagen/` (Wissen, bleibt stabil),
  `Ergebnisse/` (die Arbeit dieses Falls).
- `Wissen/` = gemeinsame Referenz für alle Schritte.
- `CONTEXT.md` = Routing: welche Aufgabe gehört zu welchem Ordner.

## Regeln für die KI
- Lade pro Schritt **nur** die Dateien dieses Schritts (+ angegebene Referenz). Nicht alles.
- Schlage vor, entscheide nicht. Nach jedem Schritt prüft und korrigiert ein Mensch.
- Schreibe Ergebnisse als saubere Textdateien (Markdown/JSON) in `Ergebnisse/`.
- Erfinde nichts. Fehlende Information benennen, nicht erfinden.
- Sprache: [Deutsch / Englisch / der Quellsprache des Materials folgen].

## Wohin als Nächstes
→ Für die Aufgabenzuordnung siehe `CONTEXT.md`.
