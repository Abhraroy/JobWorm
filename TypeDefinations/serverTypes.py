from pydantic import BaseModel


class serverResponse(BaseModel):
    success: True
    message:object

class serverError(BaseModel):
    success: False
    error:object
