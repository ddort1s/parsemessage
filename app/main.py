from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

feedbacks = []

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    def check_forbidden_words(cls, value):
        forbidden_words = ["редис", "бяк", "козяв"]

        # Приводим сообщение к нижнему регистру для корректной проверки
        lower_value = value.lower()

        # Проверяем наличие каждого запрещённого слова
        for word in forbidden_words:
            if word in lower_value:
                raise ValueError("Использование недопустимых слов")
        return value


@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback.dict())
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
