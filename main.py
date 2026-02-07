from fastapi import FastAPI,HTTPException,Path,Query
import os
import json


app=FastAPI()
@app.get('/')
def hello():
    return{'message':'Patient Management System'}

def load_data():
    if not os.path.exists('patients.json'):
        return {}
   
    try:
        with open("patients.json","r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')

def view_patient(patient_id:str=Path(...,description='ID of the patient in the DB',example='P001')):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    return data[patient_id]


@app.get('/sort')
#3 dots(...)-->means it is required
def sort_patients(sort_by:str=Query(...,description='Sort on the basis of height,weight or bmi'),order:str=Query('asc')):
    valid_fields= ['height','weight','bmi']
    if(sort_by not in valid_fields):
        raise HTTPException(status_code=400,detail=f'Invalid fields select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select')
    data=load_data()
    sort_order= True if order =='desc' else False 
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data