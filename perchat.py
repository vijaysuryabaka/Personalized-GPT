import os
import sys

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import  TextLoader

from langchain.indexes import VectorstoreIndexCreator

from langchain.llms import OpenAI
from langchain.vectorstores import Chroma



os.environ["OPENAI_API_KEY"] = "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"

query = sys.argv[1]

loader = TextLoader("data/data.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query,llm=ChatOpenAI()))