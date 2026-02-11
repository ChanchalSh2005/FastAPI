#nested_models=== if one model need to be used in second model then it is called nested model 

from pydantic import BaseModel

class Address(BaseModel):
    House_no:int
    Street:str
    city:str
    State:str
class Patient(BaseModel):
    name:str
    age:int
    address:Address  #nested model

add={'House_no':1308,'Street':'MadhavPuram','city':'Meerut','State':'UP'}
address1=Address(**add)
patient_dict={'name':'Chanchal',
    'age':21,
    'address':address1}
patient1=Patient(**patient_dict)



#export

dict=patient1.model_dump()  #it converts modle into python dict
temp1=patient1.model_dump( exclude=['address']) 
tenp2=patient1.model_dump(exclude_unset=True) #it excludes those value which is not passed during creation
js=patient1.model_dump_json()
print(js)