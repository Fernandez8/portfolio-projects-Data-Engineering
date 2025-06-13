<h1 align="center">📊 AI-Agent für automatische Dashboard-Generierung aus PostgreSQL-Datenbank </h1>

## 📋 Beschreibung
Entwicklung eines intelligenten AI-Agenten, der SQL-Datenbanken automatisch in interaktive Dashboards umwandelt - ohne manuelle Datenbankabfragen oder SQL-Kenntnisse.   
Das Ziel ist es, PostgreSQL sprechen zu lassen - ohne Programmiersprache zu lernen

## 🚧 Herausforderungen & Lösungsansatz
**Challenge:** Bei komplexen Datenbanken mit mehr als 1000 Tabellen muss der Agent intelligent die relevanten Tabellenn identifizieren.

**Entwickelte Lösung:** 
- Implementierung eines vorgelagerten Agenten zur Datenbank-Exploration
- Automatische Extraktion von Datensamples aus allen Tabellen
- Beschreibung und Indizierung in einer Vektordatenbank inklusive Spaltenbeschreibungen
- Intelligente Tabellenauswahl vor Query-Ausführung durch Vektorsuche

**Nachteil dieses Agenten**: 
Erfordert zu viele Ressourcen, um die Datensicherheit zu gewährleisten und die Abfragen zu optimieren. Darüber hinaus kann der Agent nicht in Produktion eingesetzt werden, da geeignete Methoden zur Validierung der Ergebnisse fehlen und somit die Qualität und Zuverlässigkeit der Resultate nicht sichergestellt werden kann.