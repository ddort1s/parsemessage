from fastapi import FastAPI, Query
from .models import FeedBack

app = FastAPI()

fake_data_base = []
@app.post("/feedback")
async def Feedback(fb: FeedBack, is_premium:bool = Query(None)):
    fake_data_base.append({"name": fb.name, "message": fb.message, "email": fb.contact.email, "phone": fb.contact.phone, "is_premium": is_premium})
    if is_premium==True: 
        return {"message": f"Спасибо, {fb.name}! Ваш отзыв сохранен. Ваш отзыв будет рассмотрен в приоритетном порядке."}
    return {"message": f"Спасибо, {fb.name}! Ваш отзыв сохранен"}
