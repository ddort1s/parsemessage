from pydantic import BaseModel, Field, field_validator

BAN = ["редис", "бяк", "козяв"]

class validMessage(BaseModel): 
    name: str = Field(..., min_length=1, max_length=20)
    message: str = Field(..., min_length=10, max_length=20)

    @field_validator("message")
    def valid_message(cls, msg):
        if any(word for word in BAN): 
            raise ValueError("ВНИМАНИЕ: запрещенные слова")
        return msg 

    

