# Runtime DataValidation and AutomaticeDataParsing

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Unknown'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing cgpa of a student')

# new_std: Student = {'name':'Hritik', 'age':22, 'email':'a', 'cgpa':4.7} # this not enforce, don't use
std_d = {'name':'Hritik', 'age':22, 'email':'a@e.c', 'cgpa':4.7}
new_std = Student(**std_d)

print(type(new_std), new_std)

s = new_std.model_dump_json()
s.save('./s.json')