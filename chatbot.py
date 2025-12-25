from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Flood Chatbot API")

class ChatRequest(BaseModel):
    message: str
    latitude: float
    longitude: float

@app.post("/chat")
def chat(req: ChatRequest):
    # Dummy data (same logic as prediction)
    rainfall = random.uniform(0, 300)
    soil_moisture = random.uniform(0, 1)

    if rainfall > 200 and soil_moisture > 0.7:
        risk = "High"
        advice = "⚠️ High flood risk. Avoid travel and stay alert."
    elif rainfall > 100:
        risk = "Medium"
        advice = "⚠️ Moderate flood risk. Monitor weather updates."
    else:
        risk = "Low"
        advice = "✅ Low flood risk. Conditions are normal."

    response = (
        f"📍 Location ({req.latitude}, {req.longitude})\n"
        f"🌧 Rainfall: {rainfall:.1f} mm\n"
        f"🌱 Soil Moisture: {soil_moisture:.2f}\n"
        f"🚨 Flood Risk: {risk}\n\n"
        f"{advice}"
    )

    return {"reply": response}
