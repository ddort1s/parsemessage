from pydantic import BaseModel, EmailStr, constr, field_validator, Field
from typing import Optional

class Contact(BaseModel):
    email: EmailStr
    phone: Optional[constr(min_length=7,max_length=15)] = None 

    @field_validator("phone")
    def valid_phone(cls, ph):
        if ph is not None and not ph.isdigit():
            raise ValueError("Номер должен состоять только из цифр")
        else: 
            return ph 
        
class FeedBack(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length = 10, max_length=500)
    contact: Contact

    
    @field_validator("message")
    def valid_message(cls, m):
        BUN = ["редис", "бяк", "козяв"]
        for w in BUN: 
            if w in m:
                raise ValueError("Будьте вежливы")
        return m 
    
    