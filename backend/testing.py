import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from database import db
import os

router = APIRouter()
logs_collection = db["logs"]
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Use .env for safety

@router.get("/insights/")
async def get_ai_insights():
    try:
        logs = list(logs_collection.find())
        if not logs:
            raise HTTPException(status_code=404, detail="No logs found")

        # Build prompt
        prompt = "Based on these blood sugar and lifestyle logs, provide 3 short, helpful tips to improve blood sugar management:\n\n"
        for log in logs[-5:]:
            prompt += f"Date: {log.get('date', '')}\n"
            prompt += f"Glucose: {log.get('glucose', 'N/A')}\n"
            prompt += f"Meals: {log.get('meals', 'N/A')}\n"
            prompt += f"Activity: {log.get('activity', 'N/A')}\n"
            prompt += f"Sleep Hours: {log.get('sleep_hours', 'N/A')}\n"
            prompt += "-----\n"

        # Call OpenRouter using HTTPX
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {"role": "system", "content": "You are a helpful health assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 400,
            "temperature": 0.7
        }

        async with httpx.AsyncClient() as client:
            res = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

        if res.status_code != 200:
            print("❌ OpenRouter error:", res.status_code, res.text)
            raise HTTPException(status_code=500, detail="OpenRouter API error")

        data = res.json()
        insights = data["choices"][0]["message"]["content"].strip()

        return {"insights": insights}

    except Exception as e:
        print("❌ Error in get_ai_insights:", str(e))
        raise HTTPException(status_code=500, detail=f"Error generating insights: {str(e)}")
