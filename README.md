# RAG with OpenAI

> A hands-on project to learn Retrieval-Augmented Generation (RAG) using Python and the OpenAI API.

## About the Project

This project documents my learning journey into Retrieval-Augmented Generation (RAG) while following a Udemy course. It covers Python project setup, environment variable configuration, OpenAI API client initialization, and chat completion examples.

As I progress, I will explore document processing, embeddings, information retrieval, and context-aware response generation to build an end-to-end RAG application.

## Libraries

- **OpenAI:** [OpenAI Python SDK](https://github.com/openai/openai-python) provides a Python interface for interacting with the OpenAI API.
- **python-dotenv:** [python-dotenv](https://pypi.org/project/python-dotenv/) loads environment variables from a `.env` file.
- **Colorama:** [Colorama](https://pypi.org/project/colorama/) provides colored terminal text and output.

## Install Python

- [Download Python](https://www.python.org/downloads/)
- Python 3.12 is used as a reference; choose a version compatible with the project's dependencies.

## Project Structure

```text
RAG-With-OpenAI/
├── .gitignore
├── README.md
├── env/                       # Local virtual environment
└── starter-project/
    ├── .env                   # Local API key (not uploaded)
    ├── .env.example           # Environment variable template
    ├── main.py                # Main Python script
    ├── README.md              # Starter project documentation
    └── requirements.txt       # Python dependencies
```

## Create a Virtual Environment

**Windows**

```bash
python -m venv env
```

**macOS/Linux**

```bash
python3 -m venv env
```

## Activate the Virtual Environment

**Windows PowerShell**

```powershell
.\env\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source env/bin/activate
```

## Install Dependencies

Run these commands from the outer project directory.

**Windows**

```bash
python -m pip install -r starter-project/requirements.txt
```

**macOS/Linux**

```bash
python3 -m pip install -r starter-project/requirements.txt
```

## Get an OpenAI API Key

Create an API key from the [OpenAI API Keys page](https://platform.openai.com/api-keys).

Create a `.env` file inside the `starter-project` directory and add:

```env
OPENAI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never upload your actual API key or `.env` file to GitHub. The `.env.example` file must contain only placeholder values.

## Run the Script

Run the following command from the outer project directory.

**Windows**

```bash
python starter-project/main.py
```

**macOS/Linux**

```bash
python3 starter-project/main.py
```

The script loads environment variables, checks whether the API key is present, initializes the OpenAI client, and submits a chat completion request.

A successful live response requires a valid API key, an available API balance or eligible billing arrangement, and a supported model.

## Learning Progress

- [x] Python project setup
- [x] Environment variable configuration
- [x] OpenAI client initialization
- [x] Chat completion code written
- [ ] Successfully test a live model response
- [ ] Process documents
- [ ] Generate text embeddings
- [ ] Retrieve relevant information
- [ ] Generate answers using retrieved context
- [ ] Build an end-to-end RAG application

## Learning Resource

This project is being developed as part of my hands-on learning through a Udemy RAG course.

## Author

**Sathvika Nidadavolu**

- GitHub: [Sathvika2955](https://github.com/Sathvika2955)

---

*This project is a work in progress and will be updated as I learn and implement new RAG concepts.*
