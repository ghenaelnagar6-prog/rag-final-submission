# First Aid Book Assistant (RAG)

An Arabic-friendly question-answering assistant that answers first-aid questions **only from the content of a first-aid book** (365 pages), and tells the user which part of the book it used.

**🔗 Live demo:** https://ghena-first-aid-rag.streamlit.app

## Screenshots

**Arabic question**: "أعراض الكسر" (symptoms of a fracture)

(الصورة العربي هنا)

**English question**: "What are the symptoms of a fracture?"

(الصورة الإنجليزي هنا)

*The assistant answers in the user's language and cites the part of the book it used.*<img width="663" height="479" alt="لقطة شاشة 2026-11-18 142004" src="https://github.com/user-attachments/assets/3f73c431-2823-4303-b1f1-59357c8013f4" />
![Uploading لقطة شاشة 2026-11-18 142004.png…]()
<img width="523" height="407" alt="لقطة شاشة 2026-11-18 144711" src="https://github.com/user-attachments/assets/ee683e6e-d206-4cf5-8e8a-16b3ce4f3c33" />

## How it works

The project is a Retrieval-Augmented Generation (RAG) pipeline:

1. **Documents**: load the book (`01_documents.py`)
2. **Preprocessing**: clean the text (`02_preprocessing.py`)
3. **Chunking**: split it into passages (`03_chunking.py`)
4. **Embeddings**: multilingual sentence embeddings (`04_vector_representation.py`)
5. **Vector store**: ChromaDB (`05_create_chroma_store.py`)
6. **Retrieval**: top matching passages for each question (`06_retrieve_context.py`)
7. **Prompting + LLM**: answer only from the retrieved context (`07_prompting.py`, `streamlit_app.py`)

If the answer is not in the book, the assistant says it doesn't know.

## Tech stack

Python · Streamlit · ChromaDB · Sentence-Transformers (`paraphrase-multilingual-MiniLM-L12-v2`) · OpenRouter API

## Results

Answer accuracy: **96%**.

## Run locally<img width="663" height="479" alt="لقطة شاشة 2026-11-18 142004" src="https://github.com/user-attachments/assets/fcca485e-ab23-48d1-b761-0800f5d38504" />


```bash
pip install -r requirements.txt
export OPENROUTER_API_KEY="your-key"
streamlit run streamlit_app.py
```

## نبذة بالعربي

مساعد إسعافات أولية يجيب على الأسئلة من محتوى كتاب إسعافات أولية (365 صفحة) فقط باستخدام تقنية RAG، ويذكر الجزء الذي استند إليه في الإجابة. يدعم الأسئلة بالعربية والإنجليزية.

## Author

**Ghena El-Nagar**: [LinkedIn](https://www.linkedin.com/in/ghena-elnagaranddata)
