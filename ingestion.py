import os

from langchain_google_vertexai import VertexAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_pinecone import PineconeVectorStore


def ingest_docs() -> None:
    urls = [
            "https://pokemongolive.com/post/verdant-wonders-2024?hl=zh_Hant",
            "https://pokemongolive.com/post/weather-week-2024?hl=zh_Hant",
            "https://pokemongolive.com/post/kyogre-groudon-primal-raid-day-event?hl=zh_Hant",
    ]
    loader = WebBaseLoader(urls)

    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
        chunk_size=5000,
        chunk_overlap=150,
    )

    documents = text_splitter.split_documents(docs)

    print(f"Going to add {len(documents)} to Pinecone")

    # for doc in documents:
    #     print(doc)


    embeddings = VertexAIEmbeddings()

    index_name=os.getenv("PINECONE_INDEX_NAME")
    print(index_name)

    # don't mix up multiple pages
    chunk_size = 1 
    for i in range(0, len(documents)):
        print(f"iteration {i}...")
        chunked_documents = documents[i:i+chunk_size]
        PineconeVectorStore.from_documents(
            chunked_documents, embeddings, index_name=index_name
        )
    print("****Loading to vectorestore done ***")

if __name__ == "__main__":
    ingest_docs()
