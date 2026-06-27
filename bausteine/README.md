# Bausteine — Step Into More

Wiederverwendbare Module für Kundenprojekte. Aus diesen Teilen wird pro Kunde ein
konkretes Angebot und ein konkretes ICM-System zusammengesetzt. **Nichts hier ist
kundenspezifisch** — Namen, Branche und Beispiele werden erst beim Kopieren eingesetzt.

## Was hier liegt

| Baustein | Zweck | Form |
|----------|-------|------|
| `icm-erklaert/icm-erklaert.md` | ICM verständlich erklären — Anordnung, Routing, Ordnerbaum, 4 Prinzipien. Quelle für Briefe, Slides, Gespräche. | Markdown |
| `icm-erklaert/icm-erklaert.html` | Dieselben Inhalte als visuelle Seite (DAA-Style als Beispiel). Direkt zeigbar. | HTML |
| `vorlagen/CLAUDE.md-vorlage.md` | Leeres Ebene-0-Gerüst (Identität eines Workspaces) | Vorlage |
| `vorlagen/CONTEXT.md-vorlage.md` | Leeres Ebene-1-Gerüst (Routing-Tabelle) | Vorlage |
| `vorlagen/_werkzeug-ordner/` | Skelette für übergebbare Werkzeuge (Interview-Coach, Bewerbungstool) | Ordner |
| `werkzeuge/interview-coach-skill/` | Echtes, lauffähiges Interview-Coaching-Tool (vollständige Skill) | Tool |
| `builders-paper.md` | ICM-/Wettbewerbs-Schreibe — Hintergrund & Argumentation | Markdown |

## So nutzt man sie

1. **Erklären:** Aus `icm-erklaert.*` die passenden Abschnitte für den Kunden auswählen
   (Führungskräfte → wenig Tiefe; F&E/IT → mehr Tiefe).
2. **Aufsetzen:** `vorlagen/` in den Kundenordner kopieren, CLAUDE.md/CONTEXT.md mit dem
   konkreten Workflow füllen, nicht gebrauchte Werkzeug-Ordner löschen.
3. **Übergeben:** Werkzeug-Ordner laufen für die Mitarbeitenden — oder werden den
   Teilnehmenden in die Hand gegeben.

## Noch nicht hier (bewusst)

- Beratungs-Angebot, Leistungspakete, Preise, Pitch.
- Datenschutz-Baustein (DSGVO / Microsoft-365-EU-Datenresidenz / Auftragsverarbeitung).
