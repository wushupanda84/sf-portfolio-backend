from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from knowledge import CONTEXT
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Portfolio Query API",
    description="API for querying professional background information using OpenAI",
    version="1.0.0"
)

# Initialize OpenAI client
client = OpenAI()

class Query(BaseModel):
    question: str

@app.get("/")
async def root():
    """
    Root endpoint providing information about the API.
    """
    return {
        "message": "Welcome to the Portfolio Query API",
        "endpoints": {
            "/query": "POST endpoint to ask questions about the professional background. Send a JSON with 'question' field."
        },
        "usage": {
            "example_request": {
                "method": "POST",
                "endpoint": "/query",
                "body": {"question": "What is your experience with IoT devices?"}
            }
        }
    }

@app.post("/query")
async def query_background(query: Query):
    """
    Endpoint to query professional background information using OpenAI.
    """
    try:
        # Construct the prompt
        prompt = f"""Based on the following context, please answer the question. 
        Keep the answer concise and professional.
        
        Context:
        {CONTEXT}
        
        Question: {query.question}"""

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional assistant helping to answer questions about someone's professional background."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the response
        return {"response": response.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
