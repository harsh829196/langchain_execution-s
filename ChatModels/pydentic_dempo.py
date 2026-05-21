from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = Field(
        ...,
        description="The name of the student"
    )

    age: Optional[int] = None

    email: Optional[EmailStr] = None

    grade: int = Field(
        default=5,
        gt=0,
        lt=10,
        description="The grade of the student"
    )

new_student = Student(
    name="John",
    age=20,
    grade=8
)

print(new_student)
print(type(new_student))
# feild is use to provide the description of the field and also to provide the validation for the field. it will also help us to provide the 
# default value for the field. it will also help us to provide the range for the field. it will also help us to provide the optional fields in the model.
#  if we want to make a field optional then we can use the Optional type from the typing module and set the default value of that field to None. if we want 
# to make a field required then we can use the Field function from the pydantic module and set the default value of that field to ... (ellipsis).