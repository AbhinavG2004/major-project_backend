import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyCEp1NwU_PaSOMEl2toJ_wGSbTGc90dJ50"))

# ✅ Stable model for v1beta
model = genai.GenerativeModel("models/gemini-pro")

def llm_response(question, flood_risk, lat, lng):
    try:
        prompt = f"""
You are an intelligent flood risk assistant.

Location:
Latitude: {lat}
Longitude: {lng}

Predicted Flood Risk: {flood_risk}

User Question:
{question}

Explain clearly and give safety advice if relevant.
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"LLM error occurred: {str(e)}"
