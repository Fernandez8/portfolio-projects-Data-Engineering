# 📊 AI-Agent für automatische Dashboard-Generierung aus PostgreSQL-Datenbank (Work in Progress)

## 📋 Beschreibung
Entwicklung eines intelligenten AI-Agenten, der SQL-Datenbanken automatisch in interaktive Dashboards umwandelt - ohne manuelle Datenbankabfragen oder SQL-Kenntnisse.
Das Ziel ist die Demokratisierung der Datenanalyse durch Beseitigung der technischen Barriere von SQL-Abfragen

## 🚧 Herausforderungen & Lösungsansatz
**Challenge:** Bei komplexen Datenbanken mit mehr als 1000 Tabellen muss der Agent intelligent die relevanten Tabellenn identifizieren.

**Entwickelte Lösung:** 
- Implementierung eines vorgelagerten Agenten zur Datenbank-Exploration
- Automatische Extraktion von Datensamples aus allen Tabellen
- Beschreibung und Indizierung in einer Vektordatenbank inklusive Spaltenbeschreibungen
- Intelligente Tabellenauswahl vor Query-Ausführung durch Vektorsuche
