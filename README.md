# Olist AI Analytics Platform

## Overview

Olist AI Analytics Platform is an end-to-end analytics engineering project that combines:

- Modern Data Warehouse architecture
- Dimensional modeling best practices
- Data quality validation and governance
- Semantic metric layer
- Conversational Analytics using RAG + LLM

This project uses the Brazilian E-Commerce public dataset (Olist) to simulate a real-world business scenario focused on revenue growth, logistics efficiency, and customer experience.

---

## Project Goals

- Build a production-style analytics architecture locally using Docker
- Implement Bronze / Silver / Gold data layers
- Apply dimensional modeling best practices
- Implement data quality validation and monitoring
- Create a governed semantic metric layer
- Enable AI-powered conversational analytics using RAG
- Log and monitor AI interactions (basic LLMOps layer)

---

## High-Level Architecture

Data Ingestion (Python)  
        ↓  
Postgres (Bronze / Silver)  
        ↓  
dbt (Transformations + Tests + Documentation)  
        ↓  
Gold Layer (Facts + Dimensions + Business Marts)  
        ↓  
Semantic Layer (Metric Definitions)  
        ↓  
Embeddings + Vector Store  
        ↓  
RAG Pipeline  
        ↓  
Streamlit AI Assistant  

---

## Tech Stack

- Python
- PostgreSQL
- dbt Core
- Docker & Docker Compose
- Streamlit
- Vector Store (Chroma or FAISS)
- OpenAI API (LLM Integration)

---

## Project Structure

olist-ai-analytics-platform/

├── README.md  
├── docker-compose.yml  
├── .env.example  
├── requirements.txt  

├── ingestion/              # Raw data ingestion layer  
├── warehouse/              # DDL and warehouse setup  
├── dbt/                    # Transformation layer  
├── semantic_layer/         # Metric definitions + embeddings  
├── ai/                     # RAG pipeline and LLM integration  
├── app/                    # Streamlit conversational interface  
├── monitoring/             # Data quality & AI monitoring  
├── docs/                   # Governance & documentation  
└── tests/                  # Unit & integration tests  

---

## Data Architecture Layers

### Bronze Layer
- Raw ingestion from source
- No structural modification
- Batch control metadata
- Load timestamp tracking

### Silver Layer
- Data cleaning
- Standardization
- Surrogate keys
- Null handling
- Business rule validation
- Data enrichment (date dimensions, derived fields)

### Gold Layer
- Fact tables
- Dimension tables
- Business marts
- Governed metrics
- Optimized query layer

---

## Business Focus Areas

### Revenue & Growth
- Monthly revenue
- Month-over-month growth
- Average ticket
- Revenue by category
- Revenue by state

### Logistics Performance
- Delivery SLA
- Delay percentage
- Average delivery time
- Seller performance
- Region-based performance

### Customer Experience
- Average review score
- Delivery delay vs review impact
- Category satisfaction analysis

### Customer Behavior
- Cohort analysis
- Retention rate
- Repeat purchase behavior

---

## Data Quality & Governance

This project includes:

- dbt built-in tests (not_null, unique, relationships)
- Custom business rule validations
- Data Quality monitoring table
- Naming conventions
- Data dictionary
- Metric definitions
- Lineage documentation
- Version control
- Environment separation (dev)

---

## AI & Conversational Analytics

The project implements a Retrieval-Augmented Generation (RAG) architecture:

1. User submits a business question
2. System retrieves relevant metric definitions
3. SQL is generated dynamically
4. Query result is executed against the warehouse
5. LLM generates contextualized response
6. Interaction is logged for monitoring

The AI layer is constrained to respond only using governed data models to prevent hallucination.

---

## AI Monitoring

The system logs:

- User question
- Generated SQL
- Execution time
- Response
- Success / failure status
- Referenced metric

This enables basic LLMOps practices.

---

## How to Run Locally

### Clone repository

git clone <repo-url>  
cd olist-ai-analytics-platform  

### Configure environment

cp .env.example .env  

Update environment variables if needed.

### Start services

docker compose up -d  

### Access services

- PostgreSQL → localhost:5432  
- pgAdmin → localhost:5050  
- Streamlit → localhost:8501 (future step)

---

## Author

Felipe Mendonça  
Analytics Engineer | Data Engineer | AI-driven Analytics