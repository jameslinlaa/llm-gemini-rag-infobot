import os
from typing import Any, Dict, List

from langchain_google_vertexai import VertexAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain_google_vertexai import ChatVertexAI
from langchain.chains import ConversationalRetrievalChain

import langchain 
# langchain.debug = True


def run_g_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = VertexAIEmbeddings()  # Dimention 768

    vectorstore = PineconeVectorStore(index_name=os.environ["PINECONE_INDEX_NAME"], embedding=embeddings)

    chat = ChatVertexAI(
        # Reduce the possibility of the answer is truncated 
        max_output_tokens=2000
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=vectorstore.as_retriever(), return_source_documents=True
    )

    return qa({"question": query, "chat_history": chat_history})

