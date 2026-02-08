#type validation

from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
#Field is used for constraint on data type like length,gt,lt 
#by using Annotated and Field,we can include metadata 
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,titl='Name of the patient',description='Give the data of the patient in less than 50 characters!!',examples=['Nitish','Amit'])]
    email:EmailStr
   # linkedin_url:AnyUrl
    age:int
    weight:float=Field(gt=0,strict=True)  #strict prohibiting type conversion 
    #married=bool=False       #setting default value
    allergies:Optional[List[str]]=None    #keeping optional field
    contact_details:Optional[Dict[str,str]]

    @field_validator('email',mode='after')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform(cls,value):
        return value.upper()

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')


patient_info={'name':'chanchal','email':'abc123@gmail.com','age':123,'allergies':['hair','skin'],'contact_details':{'emails':'abc123@gmail.com','mob_no':'+91XXXXXXX'} }
patient1=Patient(**patient_info) #validation->type coersion
insert_patient_data(patient1)