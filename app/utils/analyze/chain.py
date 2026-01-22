from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableSequence

from schemas import LanguageAnalysis
from prompt import prompt
from dotenv import load_dotenv
import os

load_dotenv()  # 会自动读取 .env 文件
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3,
    api_key = api_key
)

parser = PydanticOutputParser(pydantic_object=LanguageAnalysis)

prompt_with_format = prompt.partial(
    format_instructions=parser.get_format_instructions()
)

language_analysis_chain = (
    prompt_with_format
    | llm
    | parser
)
