import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def get_prompt_messages(question: str):
    return [
        {
            "role": "system",
            "content": """You are an AI assistant specialized in answering questions about software development, programming languages, frameworks, best practices, and related technical topics.

CRITICAL RESPONSE RULES:
1. You must ONLY use information found in the retrieved documents.
2. If an answer cannot be found in the documents, or if it is not possible to formulate an answer confidently, say: 'I don’t know' - no other variations or explanations.
3. Do not attempt to infer, extrapolate, or combine partial matches.
4. Do not use your general knowledge even if you know the answer.
5. Do not provide alternative responses or suggestions when information is not found.
6. Never apologize or explain why you don't know something.

When information IS found:
1. Provide detailed, accurate responses based solely on the retrieved documents.
2. Include specific examples and references from the documents.
3. Focus only on software development and related technical content.
4. Structure your response clearly and concisely."""
        },
        {
            "role": "user",
            "content": question,
        }
    ]

def semantic_completion(question: str, top_n_documents: int = 5):
    messages = get_prompt_messages(question)
    completion = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        max_tokens=800,
        temperature=0.2,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False,
        extra_body={
            "data_sources": [{
                "type": "azure_search",
                "parameters": {
                    "endpoint": AZURE_SEARCH_ENDPOINT,
                    "index_name": AZURE_SEARCH_INDEX_NAME,
                    "fields_mapping": {},
                    "in_scope": True,
                    "filter": None,
                    "strictness": 4,
                    "top_n_documents": top_n_documents,
                    "authentication": {
                        "type": "api_key",
                        "key": AZURE_SEARCH_API_KEY
                    },
                }
            }]
        }
    )
    return completion.choices[0].message.content

def ask_question(question: str) -> str:
    return semantic_completion(question)