# deploy-test Flask app

Minimal Flask application used to test Docker-based deployment.

Quick start

Build the image (from project root):

```bash
docker build -t deploy-test-flask .
```

Run the container:

```bash
docker run --rm -p 8080:8080 deploy-test-flask
```

Then visit `http://localhost:8080/` and `http://localhost:8080/health`.
