Docker instructions

To build
```bash
docker build -t sql_searcher_backed:0.0.1 .
```

To run
```bash
docker run -d -e GCP_DEVELOPER_KEY="your key" -e GCP_SEARCH_ENGINE_ID="your search engine id" sql_searcher_backed:0.0.1
```