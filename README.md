# AI-Powered Loan Risk & Customer Intelligence Platform

> End-to-End Data Engineering + Machine Learning + Generative AI Platform

## 🚧 Project Status

**Currently under development**

This repository contains an end-to-end cloud data platform designed around a simulated NBFC/financial-services use case.

The project demonstrates how customer, loan, repayment and credit data can be ingested, transformed, validated, analyzed and used for machine-learning and generative-AI applications.

## 🎯 Project Objective

Build a production-style data platform that demonstrates:

* Data ingestion
* Data Lake / Lakehouse architecture
* PySpark data transformation
* Delta Lake
* Incremental data processing
* Dimensional modeling
* Data quality
* Pipeline monitoring
* Machine learning
* MLflow
* Model explainability
* Generative AI
* RAG
* REST APIs
* React
* Power BI
* Docker
* Azure deployment
* CI/CD

## 🏗️ High-Level Architecture

```text
Data Sources
     │
     ▼
 ADLS Gen2
     │
     ▼
Azure Databricks
     │
     ▼
 Bronze
     │
     ▼
 Silver
     │
     ▼
 Gold
     │
 ┌───┼────────┐
 ▼   ▼        ▼
 BI  ML       DQ
     │
     ▼
   MLflow
     │
     ▼
    SHAP
     │
     ▼
    RAG
     │
     ▼
  FastAPI
     │
     ▼
   React
```

## 🛠️ Technology Stack

| Category         | Technology           |
| ---------------- | -------------------- |
| Cloud            | Microsoft Azure      |
| Storage          | ADLS Gen2            |
| Processing       | Azure Databricks     |
| Programming      | Python, PySpark, SQL |
| Data Format      | Delta Lake           |
| ML               | XGBoost              |
| ML Tracking      | MLflow               |
| Explainability   | SHAP                 |
| AI               | LLM + RAG            |
| API              | FastAPI              |
| Frontend         | React                |
| BI               | Power BI             |
| Containerization | Docker               |
| CI/CD            | GitHub Actions       |

## 📊 Planned Capabilities

### Data Engineering

* Multi-source ingestion
* Bronze/Silver/Gold architecture
* Incremental processing
* Data-quality validation
* Customer 360
* Dimensional modeling

### Machine Learning

* Loan default prediction
* Feature engineering
* Model evaluation
* Experiment tracking
* Model explainability

### Generative AI

* AI Loan Risk Assistant
* RAG-based policy search
* AI Data Engineer Assistant
* Natural-language data interaction

### Application

* Customer 360
* Risk analysis
* AI assistant
* Pipeline monitoring
* Data-quality monitoring

## ⚠️ Disclaimer

This project uses synthetic data and is intended for educational and portfolio purposes only.

It is not intended to make or recommend real-world lending or credit decisions.

## 📌 Project Status

This project is being developed incrementally.

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for the current implementation status.
