# RAG with OpenAI

> A hands-on project to learn Retrieval-Augmented Generation (RAG) using Python and the OpenAI API.

## About the Project

This project is part of my learning journey into RAG. It currently covers Python project setup, environment variable configuration, and OpenAI API client initialization. More RAG components will be added as I progress through the course.

## Libraries

- **OpenAI**: [OpenAI Python SDK](https://github.com/openai/openai-python) is a Python library that provides an interface to the OpenAI API.
- **python-dotenv**: [python-dotenv](https://pypi.org/project/python-dotenv/) loads environment variables from a `.env` file.
- **colorama**: [Colorama](https://pypi.org/project/colorama/) provides colored terminal text and output.

## Install Python

- [Python Installation Guide](https://www.python.org/downloads/)
- Recommended: Python 3.12 or a version compatible with your project dependencies.

## Project Structure

```text
RAG-With-OpenAI/
├── .gitignore
├── README.md
├── env/
└── starter-project/
    ├── .env
    ├── .env.example
    ├── main.py
    ├── README.md
    └── requirements.txt
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

## Installation

Install the required libraries from the project's requirements file.

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

Create a `.env` file inside the `starter-project` folder and add:

```env
OPENAI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never upload your actual API key or `.env` file to GitHub. The `.env.example` file should contain only a placeholder.

## Run the Script

From the outer `RAG-With-OpenAI` directory:

**Windows**

```bash
python starter-project/main.py
```

**macOS/Linux**

```bash
python3 starter-project/main.py
```

The current script loads environment variables, initializes the OpenAI client, and prints a status message. An actual model request will be added in a later step.

## Learning Progress

- [x] Python project setup
- [x] Environment variable configuration
- [x] OpenAI client initialization
- [ ] Send a request to an OpenAI model
- [ ] Process documents
- [ ] Generate embeddings
- [ ] Retrieve relevant information
- [ ] Generate answers using retrieved context
- [ ] Build an end-to-end RAG application

## Learning Resource

This project is being developed while following a Udemy course on RAG.

## Author

**Sathvika Nidadavolu**

- GitHub: [Sathvika2955](https://github.com/Sathvika2955)

---

*This project is a work in progress and will be updated as I learn more about RAG.*
