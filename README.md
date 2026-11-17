# AeroDoc AI

**Engineering Documentation Intelligence powered by Retrieval-Augmented Generation (RAG).**

AeroDoc AI is a document-grounded assistant for exploring engineering manuals, specifications, and technical reference material. The goal is to answer questions using retrieved source passages and provide traceable citations, while abstaining when the available documents do not support an answer.

> **Project status:** Initial backend scaffold. Document ingestion, retrieval, generation, evaluation, and the user interface are planned implementation stages and are not yet complete.

## Product goals

- Ingest PDF engineering documents and preserve page-level source metadata.
- Split extracted text into searchable chunks.
- Generate embeddings and retrieve relevant passages for a user query.
- Generate answers constrained by retrieved context.
- Return citations identifying the source document and page.
- Evaluate retrieval quality and answer grounding.
- Expose functionality through a documented REST API.

This is an informational documentation assistant, not a certified engineering, inspection, maintenance, or flight-safety system. Outputs must be reviewed by qualified personnel and must not be used as the sole basis for safety-critical decisions.

## Initial technology choices

| Area | Technology |
|---|---|
| Language | Python 3.11+ |
| API | FastAPI |
| Validation / settings | Pydantic, pydantic-settings |
| Tests | pytest, FastAPI TestClient |
| Document extraction | PyMuPDF (planned) |
| Embeddings | Sentence Transformers (planned) |
| Vector retrieval | FAISS or Chroma (to be evaluated) |
| Persistence | PostgreSQL (planned) |
| Packaging | Docker |

Technology choices for the retrieval and generation layers will be finalized after baseline experiments.

## Repository layout

```text
aerodoc-ai/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   ├── evaluation/
│   └── main.py
├── tests/
├── data/
│   └── sample_documents/
├── docs/
├── scripts/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Run locally

Python 3.11 or newer is recommended.

```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# Install the project and development dependencies
python -m pip install --upgrade pip
pip install -e ".[dev]"

# Start the API
uvicorn app.main:app --reload
```

Open the interactive API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Current endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Health check |

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker compose up --build
```

The API is available at [http://localhost:8000](http://localhost:8000).

## Configuration

Copy `.env.example` to `.env` before adding local configuration. Never commit API keys, credentials, private documents, or production data.

## Development roadmap

- [x] Repository scaffold and application entry point
- [x] Health endpoint and baseline tests
- [ ] PDF ingestion with page-aware metadata
- [ ] Text normalization and configurable chunking
- [ ] Embedding generation and vector indexing
- [ ] Semantic retrieval with source metadata
- [ ] Grounded answer generation with citations and abstention
- [ ] Evaluation dataset and retrieval / answer metrics
- [ ] Document comparison
- [ ] PostgreSQL persistence and Dockerized services
- [ ] Streamlit interface and end-to-end demonstration

## Engineering principles

1. **Traceability:** generated claims should be attributable to retrieved source passages.
2. **Grounding:** do not present unsupported content as fact.
3. **Evaluation:** measure retrieval and answer quality with a versioned test set.
4. **Security:** validate uploads, limit file size, and keep secrets outside source control.
5. **Honesty:** report system limitations and uncertainty clearly.

## License

No license has been selected yet. All rights are reserved by default until a license is added.
