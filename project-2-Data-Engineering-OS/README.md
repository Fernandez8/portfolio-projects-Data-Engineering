# 📦 Projekt 2 – Data Engineering OS (Open Source Plattform)

##  Projektübersicht

Entwicklung eines Systems zur Echtzeit-Datenaufnahme, -verarbeitung und -visualisierung unter Verwendung moderner Open-Source-Technologien.

Ziel des Projekts ist der Aufbau einer modularen und erweiterbaren Data-Engineering-Plattform, die sich flexibel in unterschiedliche Umgebungen integrieren lässt – sowohl lokal (on-premise) als auch in der Cloud.

---

##  Verwendete Technologien

- **Apache Kafka** – Streaming und Messaging
- **Apache Airflow** – Orchestrierung von Datenpipelines
- **Apache Spark** – Verteilte Datenverarbeitung
- **Great Expectations** – Datenvalidierung und Qualitätssicherung
- **PostgreSQL** – Relationale Datenspeicherung & Metadaten
- **Docker / Docker Compose** – Containerisierung
- **Grafana** – Datenvisualisierung
- **dbt** – Transformation & Modellierung (optional)

---

##  Architektur

<p align="center">
  <img src="datenarchitekt_os.png" alt="Data Engineering OS Architektur" width="700"/>
</p>

Die Architektur basiert auf einem **modularen Baukastenprinzip**.  
Jede Komponente (Ingestion, Processing, Storage, Monitoring) ist **entkoppelt**, um Wiederverwendbarkeit und Austauschbarkeit zu ermöglichen.

---

##  Projektziele

- Standardisierte und automatisierte Datenverarbeitung
- Unterstützung von Batch- und Echtzeitverarbeitung
- Reproduzierbare Transformationen mit **dbt**
- Integrierte Datenqualitätssicherung mit **Great Expectations**
- Visualisierung aktueller Daten in **Grafana**
- Einsatz ausschließlich quelloffener Komponenten (Open Source)

---


