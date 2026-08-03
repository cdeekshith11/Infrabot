# 🤖 InfraBot

<p align="center">
  <b>AI-Powered Cloud Infrastructure Assistant</b><br>
  Built using <b>Python</b>, <b>FastAPI</b>, <b>AWS</b>, and <b>Amazon Bedrock</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![License](https://img.shields.io/badge/License-MIT-blue)

</p>

---

# 📖 Overview

InfraBot is an AI-powered cloud infrastructure assistant that enables engineers to interact with AWS infrastructure using natural language.

Instead of manually navigating multiple AWS services, InfraBot retrieves infrastructure information from AWS APIs, analyzes operational data, and generates intelligent responses using Amazon Bedrock.

The project follows a modular architecture designed for scalability, making it easy to extend with additional AWS services and AI-powered capabilities.

---

# ✨ Features

- Retrieve EC2 instance details
- List IAM users
- Retrieve S3 bucket information
- Fetch CloudWatch CPU metrics
- Analyze EC2 health
- Retrieve AWS Cost Explorer data
- Natural language infrastructure queries
- Modular tool-based architecture
- REST APIs using FastAPI
- Amazon Bedrock integration
- Structured logging
- Scalable backend architecture

---

# 🏗️ Architecture

```
                   User

                    │

                    ▼

             FastAPI REST API

                    │

                    ▼

          Query Orchestrator

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

    EC2 Tool     S3 Tool      IAM Tool

      │             │             │

      └─────────────┼─────────────┘

                    ▼

        CloudWatch / Cost Explorer

                    │

                    ▼

          Amazon Bedrock (LLM)

                    │

                    ▼

         Intelligent Cloud Response
```

---

# 🛠️ Technology Stack

## Backend

- Python
- FastAPI

## Cloud

- AWS EC2
- AWS IAM
- AWS S3
- AWS CloudWatch
- AWS Cost Explorer
- Amazon Bedrock

## AI

- Large Language Models (LLMs)
- Prompt Engineering

## Development

- Git
- GitHub

---

# 📂 Project Structure

```
InfraBot/

│

├── app/

│ ├── routers/

│ ├── services/

│ ├── tools/

│ ├── orchestrators/

│ ├── config/

│ ├── utils/

│ └── main.py

│

├── requirements.txt

├── README.md

├── .env.example

├── .gitignore

└── LICENSE
```

---

# 🔧 Available APIs

## POST /query

Accepts natural language questions and retrieves relevant AWS information.

Example:

```
Show all EC2 instances

Analyze EC2 health

List IAM users

Show my AWS cost

List S3 buckets
```

---

# ☁️ AWS Services Integrated

| Service | Status |
|----------|--------|
| EC2 | ✅ |
| IAM | ✅ |
| S3 | ✅ |
| CloudWatch | ✅ |
| Cost Explorer | ✅ |
| Amazon Bedrock | ✅ |

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/InfraBot.git

cd InfraBot
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env`

Example

```text
AWS_REGION=us-east-1

AWS_PROFILE=default

MODEL_ID=amazon.nova-lite-v1:0
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

# 📸 Screenshots

Add screenshots of

- Swagger UI
- EC2 API Response
- CloudWatch Response
- Cost Explorer Response
- Folder Structure

---

# 🎯 Example Questions

```
Show all EC2 instances

Analyze EC2 health

List IAM users

Show S3 buckets

What is my AWS cost?

Show CPU utilization

Summarize my infrastructure
```

---

# 🗺️ Roadmap

## Completed

- EC2 Integration
- IAM Integration
- S3 Integration
- CloudWatch Metrics
- Cost Explorer Integration
- FastAPI Backend
- Modular Tool Architecture
- Amazon Bedrock Integration

## Planned

- AI Agent-based Tool Selection
- Kubernetes Monitoring
- Terraform Integration
- Multi-Cloud Support (AWS + GCP)
- Authentication & RBAC
- Web Dashboard
- Cost Optimization Recommendations
- Infrastructure Drift Detection
- Slack & Teams Notifications
- Infrastructure Health Reports

---

# 📄 License

This project is licensed under the MIT License.

---

