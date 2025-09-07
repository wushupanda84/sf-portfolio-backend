# Portfolio Query API

A FastAPI-based backend service that uses OpenAI's GPT-4 to answer questions about professional background.

## Setup

1. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```

The API will be available at http://localhost:8000

## API Endpoints

### GET /
Returns information about the API and its usage.

### POST /query
Send questions about the professional background.

Request body:
```json
{
    "question": "What is your experience with IoT devices?"
}
```

## Development

To run locally without Docker:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

## Documentation

Once the server is running, you can access:
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc
