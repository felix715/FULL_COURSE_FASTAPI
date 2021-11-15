from fastapi import FastAPI
from typing import Optional
from fastapi import FastAPI
from pyndatic import BaseModel

app=FastAPI()
class Student(BaseModel):
    name:str
    age:int
    education-level:str


class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int]=None
    education-level: Optional[str]=None
students={
    1:{
        "name": "felix"
        "age":21
        "education": "third year"
    }
}


@app.get("/")

async def root_index():
    return {"name":"hello felix"}

@app.get("/get-student/{student_id}")
async def get_student(student_id: int=Path(None, description ="The ID of the Student to view")):
    return students[student_id]

@app.get("/student-by-name/{student_id}")
async def student_by_name(*,student_id: int,name: Optional[str]=None, test= int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return "Error:Data Not found."


# creating the new data by post method
# allows you to create new student data on the fastapi docs window
@app.post("/create-student/{student_id}")
async def create_student(student_id: int,student: Student):
    if student_id in students:
        return "Error,the student exists."
    students[student_id]= student
    return students[student_id]
@app.put("/update-student/{student_id}")
async def update_student(student_id: int,student:Student):
    if student_id not in students:
        return "Error Student does not exist."

    if student.name !=None:
        students[stuent_id].name =student.name


    if student.age != None:
        students[stuent_id].age = student.age

    if student.education-level != None:
        students[stuent_id].education-level = student.education-level


    # students[student_id] = student
    return students[student_id]



# deleting the students by delete method.
@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students:
        return "Student does not exist"
    del students[student_id]
    return "student has been deleted Successfully."






