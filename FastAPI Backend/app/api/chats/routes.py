from fastapi import APIRouter
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from pathlib import Path
from app.core.config import settings

router = APIRouter()

# Load GPT-4o-mini
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    openai_api_key=settings.OPENAI_API_KEY,
)

# Load FAQ context from text file
faq_path = Path("app/resources/product_FAQs.txt")
FAQ_CONTEXT = faq_path.read_text(encoding="utf-8")

class QuestionRequest(BaseModel):
    question: str

@router.post("/query", tags=["Query"])
async def ask_question(payload: QuestionRequest):
    question = payload.question

    prompt = f"""
You are a helpful assistant. Answer the question below based on this FAQ context:

{FAQ_CONTEXT}

Question: {question}
Answer:
    """

    response = llm([HumanMessage(content=prompt)])
    return {"answer": response.content}
