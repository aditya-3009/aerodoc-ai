# Architecture

## Target request flow

1. A user uploads one or more supported engineering documents.
2. The ingestion layer extracts text and records document identifiers, filenames, and page numbers.
3. The chunking layer creates bounded passages while retaining source metadata.
4. The embedding layer converts passages into vectors.
5. The retrieval layer selects relevant passages for a user question.
6. The generation layer receives the question and retrieved passages, then produces a grounded answer.
7. The response includes citations to the source document and page, plus an abstention response when evidence is insufficient.

## Initial implementation boundary

The current application only exposes service metadata and a health check. The pipeline above is the target architecture, not an implemented feature set yet.

## Design constraints

- Preserve document and page metadata through every pipeline stage.
- Keep ingestion, retrieval, generation, and evaluation independently testable.
- Treat document content as untrusted input.
- Enforce upload size and file-type limits before parsing.
- Avoid logging document contents or secrets.
- Keep model and vector-store providers behind interfaces so they can be swapped and evaluated.
