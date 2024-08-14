# PDFix - PDF Summarizer
**Powered by OpenAI**

## Overview
PDFix is a powerful web-based PDF summarizing tool designed to streamline the research process using OpenAI's GPT-4.
This repository contains a Streamlit web application designed to summarize research paper PDFs using AI. The app allows users to quickly generate comprehensive summaries by leveraging a map-reduce approach with LangChain prompts. The summarized content is presented in a clean UI.

![image](https://github.com/user-attachments/assets/19322ddf-2552-4c74-b5f7-330b72616a22)

## Key Features

- **PDF Upload**: Users can upload research papers in PDF format (up to 5MB).
- **AI-Powered Summarization**: The app uses OpenAI's GPT-4 LLM, implemented using a map-reduce technique with LangChain prompts, to summarize the uploaded document. The output summary is concise and easy to read.
- **Responsive UI**: The interface is responsive and inspired by Apple's design guidelines.

## Tools and Technologies Used

- **Streamlit**: The main framework used to build the web app.
- **LangChain**: Employed for generating the summaries using a map-reduce approach with custom prompts.
- **Python**: The primary programming language used for the backend logic.
- **HTML/CSS**: Custom components and styling for enhanced UI/UX.
- 

## How It Works

### 1. **Environment Setup**
  - The application loads environment variables, including the OpenAI API key, using the `dotenv` library.

### 2. **PDF Upload**:
   Users can upload a PDF document via the Streamlit web app. The file uploader restricts the upload size to 5MB to make it cost-efficient. The `PyPDFLoader` from LangChain is used to load and extract the content of the PDF file.

### 3. **Text Splitting**:
   - The `RecursiveCharacterTextSplitter` is employed to split the document's text into manageable chunks. This is crucial for handling large documents by dividing them into smaller sections based on a specified `chunk_size` and `chunk_overlap`.

### 4. **Prompt Template**:
   - A custom prompt template is loaded from the `template.md` file. This template guides the AI model on how to generate summaries from the text chunks. The prompt is formatted using the `PromptTemplate` class from LangChain.

### 5. **Language Model**:
   - The app uses the `ChatOpenAI` model, specifically configured for summarization tasks. The model is initialized with specific parameters, including the model type (GPT-4o-mini` and `temperature` (set to 0 for deterministic output).

### 6. **Map-Reduce Summarization**:
   - The application utilizes the `load_summarize_chain` method with the "map_reduce" chain type:
     - **Map Step**: Each chunk of text is processed individually using the loaded prompt template.
     - **Reduce Step**: The summarized chunks are then combined into a coherent final summary, ensuring the essential information from the entire document is captured.

### 7. **Output**:
   - After the API processes the chunks, it returns the summarized content in markdown format, which is displayed in clean readable format.


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Amirtmgr/PDFix.git
cd PDFix
```

### 2. Export OpenAI Key
The API Key can be generated from [OpenAI](https://openai.com/api/pricing/).
```bash
$ export OPEN_API_KEY="XXXXX"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```
</div><h3 align="left">Connect with me:</h3>
<div> <a href="https://www.linkedin.com/in/https://www.linkedin.com/in/amirthapamagar/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
<a href="https://github.com/amirtmgr" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
<a href = "mailto:amir.thapamagar01@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
<a href="https://www.xing.com/profile/Amir_ThapaMagar" target="_blank"><img alt="Xing" src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Xing_logo.svg" target="_blank" height="22"></a>
