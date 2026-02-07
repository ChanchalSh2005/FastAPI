## FastAPI Project
A high-performance REST API built using **FastAPI**, designed for scalability, speed, and clean architecture.

## Tech Stack
- Python  
- FastAPI  
- Uvicorn  
- Pydantic

## Concepts learned
- RESTful API endpoints
-CRUD Operation

## Dataset Used: Patient Data (`patient.json`)

This project uses a patient dataset stored in **`patient.json`**.  
It contains the following fields:

- **P_ID** – Unique patient ID  
- **Name** – Patient name  
- **City** – City of residence  
- **Age** – Patient age  
- **Gender** – Male/Female  
- **Height** – Height of the patient  
- **Weight** – Weight of the patient  
- **BMI** – Body Mass Index  
- **Verdict** – Health status based on BMI


## How to Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
uvicorn main:app --reload
