
from pydantic import BaseModel,EmailStr,AnyUrl,computed_field,Field
from typing import List,Dict,Optional,Annotated
#Field is used for constraint on data type like length,gt,lt 
#by using Annotated and Field,we can include metadata 
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the data of the patient in less than 50 characters!!',examples=['Nitish','Amit'])]
    email:EmailStr
   # linkedin_url:AnyUrl
    age:int
    height:float
    weight:float=Field(gt=0,strict=True)  #strict prohibiting type conversion 
    #married=bool=False       #setting default value
    allergies:Optional[List[str]]=None    #keeping optional field
    contact_details:Optional[Dict[str,str]]
   
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi =round(self.weight/(self.height*self.height),2)


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.bmi)
    print(patient.height)
    print(patient.weight)
patient_info={'name':'chanchal','email':'abc123@hdfc.com','age':123,'weight':89.0,'allergies':['hair','skin'],'contact_details':{'emails':'abc123@gmail.com','mob_no':'+91XXXXXXX'} }
patient1=Patient(**patient_info) #validation->type coersion
update_patient_data(patient1)