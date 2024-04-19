# llm-gemini-rag-infobot
This is an simple web app to demonstrate how to build an LLM RAG chatbot with langChain. \
LangChain is an open source framework that allows developers to combine LLM like Google Gemini with external data.
This chatbot is like an infobot to answer the questions of Pokemon Go activity information.
The demo is based on Traditional Chinese.  


# Installing Required Libraries:
```sh
pip3 install langchain unstructured python-magic-bin langchain-pinecone langchain-core langchain-google-vertexai
pip3 install streamlit streamlit_chat streamlit_extras
```

# Environment variables

In my case, export the required variable for Pinecone (via ~/.bash_profile)
```
export PINECONE_API_KEY=[XXXXXXXXXXXXXX]
export PINECONE_ENVIRONMENT_REGION=us-central1
export PINECONE_INDEX_NAME=[XXXXXXXX]
```


# Access for LLM Gemini 
```
gcloud auth application-default login

# check the credentials
cat ~/.config/gcloud/application_default_credentials.json 
```

Refer to [ChatVertexAI|LangChain](https://python.langchain.com/docs/integrations/chat/google_vertex_ai_palm/)

This codebase uses the google.auth library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.
Details in [User credentials provided by using the gcloud CLI](https://cloud.google.com/docs/authentication/application-default-credentials#personal)


# Ingest the Pokemon Go activity information into the vector store (Pinecone) 
```sh
python3 ingestion.py 
```
Currently, the code browses three different activities in March (which are "嫩綠驚奇", "氣象週" and "「原始蓋歐卡」和「原始固拉多」團體戰日" )
The page of an Pokemon Go activity will be like
![Alt Text](https://github.com/jameslinlaa/llm-gemini-rag-infobot/blob/main/static/pokemongolive.png)




# Run the app via streamlit
Run the following command to start the app 
```sh
streamlit run app.py
```



# Demo case 1
Query the activity based on a date, and following details
![Alt Text](https://github.com/jameslinlaa/llm-gemini-rag-infobot/blob/main/static/case1-date.png)

# Demo case 2
Query the activity based on pokemon's name. The LLM can understand the question based on previous context like which ticket (入場券) 
![Alt Text](https://github.com/jameslinlaa/llm-gemini-rag-infobot/blob/main/static/case2-drill-down.png)

# Demo case 3
Query the activity based on pokemon's name. The LLM can understand what you mean "both" 
Besides, extend the max_output_tokens to prevent a truncated final answer
![Alt Text](https://github.com/jameslinlaa/llm-gemini-rag-infobot/blob/main/static/case3-2stories.png)