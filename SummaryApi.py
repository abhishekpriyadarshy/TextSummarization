#import Text Summary class 
from TextSummary import perform_text_summary

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel 

app = FastAPI(title="Recipe API", openurl_url="/openapi.json")
# Create an instance of the FastAPI class
api_router = APIRouter()

class TextSummarization(BaseModel):
    text: str


# Define an API endpoint for square calculation
@api_router.post("/")
async def perform_summarization(item: TextSummarization):
    result = perform_text_summary(item.text)
    return result

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.11", port=8802, log_level="debug")




