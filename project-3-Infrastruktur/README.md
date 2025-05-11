### AWS VPC Multi-Zonen-Architektur

Architekturdiagramm, das ein AWS VPC (10.10.0.0/24) mit öffentlichen und privaten Subnetzen darstellt, konfiguriert nach Sicherheits-Best-Practices.

#### Schlüsselkomponenten
- VPC mit öffentlichem und privatem  Subnetz
- Dedizierte Routing-Tabellen für jedes Subnetz
- EC2-Instanzen, geschützt durch Sicherheitsgruppen
- S3-Zugriff aus dem VPC
- Internet-Gateway für externe Konnektivität

Diese Architektur folgt den Designprinzipien des AWS Well-Architected Frameworks und bietet Sicherheit, hohe Verfügbarkeit und Skalierbarkeit.

---
<figure style="text-align: center;">
  <figcaption style="display: block; margin-bottom: 20px;">AWS-Architekturdiagramm mit einer hybriden Cloud-Umgebung</figcaption>
  <img src="awsarchitektur.png" alt="AWS-Architekturdiagramm mit einer hybriden Cloud-Umgebung" width="700"/>
</figure>


# AWS-Technologien in der Architektur

Diese Liste enthält alle wichtigen AWS-Komponenten, die in dem Architekturdiagramm dargestellt sind:

- VPC (Virtual Private Cloud) 
- Internet Gateway
- Öffentliches Subnetz 
- Privates Subnetz 
- ACL (Access Control Lists)
- Sicherheitsgruppen
- EC2 (Elastic Compute Cloud)
- S3 (Simple Storage Service)
- Gateway-Endpunkt
- Site-to-Site VPN
- SSO (Single Sign-On)
- On-Premises
- Desktop


---


