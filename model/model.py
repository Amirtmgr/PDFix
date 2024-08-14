import os
import dotenv
import sys
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader

# Load folder paths
sys.path.append("..")


# Load the .env file and invoke the secret API key from the file
dotenv.load_dotenv('.env')
OpenAI.api_key = os.getenv("OPEN_API_KEY")


# Load Prompt Template
def load_prompt_template(path: str = 'utils/template.md') -> str:
    # Load the prompt template from 'template.md'
    with open(path, 'r') as file:
        prompt_template = file.read()
        return prompt_template
    
# Summarize the PDF file
def summarize_pdf(file_path, chunk_size=2000, model="gpt-4o-mini", temperature=0, chunk_overlap=200, key=OpenAI.api_key):
    # Load model
    llm = ChatOpenAI(model=model, temperature=0, openai_api_key=key)

    #Load PDF file
    loader = PyPDFLoader(file_path)
    docs_raw = loader.load()

    #Create multiple documents
    docs_raw_text = [doc.page_content for doc in docs_raw]

    #Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs_chunks = text_splitter.create_documents(docs_raw_text)

    #Load the prompt
    prompt_text = load_prompt_template()
    map_prompt = PromptTemplate(template=prompt_text, input_variables=["text"])

    #Summarize the chunks
    chain = load_summarize_chain(llm, chain_type="map_reduce",
                                    map_prompt=map_prompt)
   
    #Return the summary
    return chain.run(docs_chunks)
