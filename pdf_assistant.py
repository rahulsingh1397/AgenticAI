import typer
from typer import Optional, list
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.vectordb.pgvector import PgVector2 

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

