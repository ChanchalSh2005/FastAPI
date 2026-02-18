#nested_models=== if one model need to be used in second model then it is called nested model 


# | Feature       | Description                  |
# | ------------- | ---------------------------- |
# | Validation    | Checks if data is correct    |
# | Parsing       | Converts strings → int, etc. |
# | Schema        | Used for API docs            |
# | Serialization | Converts model → dict/JSON   |


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
    'address':address1   #nested models
    }
patient1=Patient(**patient_dict)



#export

dict=patient1.model_dump()  #it converts modle into python dict
temp1=patient1.model_dump( exclude=['address'])   #hides particular field 
tenp2=patient1.model_dump(exclude_unset=True) #it excludes those value which is not passed during creation by user 
js=patient1.model_dump_json()
print(js)