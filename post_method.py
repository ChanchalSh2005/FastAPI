
#Post method 
#client sending information(http method like post or put )the server that need to validates known as request body 

#steps :  i) client send http request 
        #  ii) validating data
        #   iii) if correct then added to the database 

from fastapi import FastAPI,HTTPException,Path,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,field_validator,computed_field
from typing import Annotated,Literal,Optional           #lietral is used to give options
import os
import json
app=FastAPI()

class Patient(BaseModel):
    patient_id:Annotated[str,Field(...,description={"enter you name"},examples=['P0001'])]
    name:Annotated[str,Field(...,descriptiom='name of the person')]
    city:str
    age:int
    gender:Annotated[Literal['male','female','other'],Field(...,description='gender entry')]
    height:float
    weight:float

    @computed_field
    @property     
    def bmi_calculated(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.4:
            return "Underweight"
class Patient_update(BaseModel):
    
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Optional[int]
    gender:Annotated[Optional[Literal['male','female','other']],Field(default=None)]
    height:Optional[float]
    weight:Optional[float]
         
def load_data():
    if not os.path.exists('patients.json'):
        return {}
   
    try:
        with open("patients.json","r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    if not os.path.exists('patients.json'):
        return 
    try:
        with open('patient.json','w') as f:
            json.dump(data,f)
    except json.JSONDecodeError:
        return 
         
@app.post('/create')
def create_patient(patient:Patient): #patient --->pydantic object
    #1load existing data load 
    data=load_data()

    #2checks if the patient already exists 
    if patient.id in data:
        raise HTTPException(status=400,detail='Patient is already exists .Cannot be added')
   
    data[patient.id]=patient.model_dump(exclude=['id'])  #convert pydantic object into dictionary 

     #3new patient add to the database
    save_data(data)
    return JSONResponse(status_code=201,content='Patient info inserted successfully!!!')


@app.put('/update/{patient_id}')
def update(patient_id:str,patient:Patient_update):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status=404,detail="Patient not found")
    patient_info=data[patient_id]
    patient.model_dump(exclude_unset=True)  #here we are exclude_usnset true to remove undefined fields
    for key in patient:
        Patient_update[patient_id]