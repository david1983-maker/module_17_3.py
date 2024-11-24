from pydantic import BaseModel


class CreateUser(BaseModel):
    username = str
    firstname = str
    lastname = str
    age = int
    pass


class UpdateUser(CreateUser):
    firstname = str
    lastname = str
    age = int
    pass


class CreateTask(BaseModel):
    title = str
    content = str
    priority = int
    pass


class UpdateTask(CreateTask):
    title = str
    content = str
    priority = int
    pass
