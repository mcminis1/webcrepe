Docker instructions

To build
```bash
docker build -t pg_searcher:0.0.1 .
```

To run
```bash
docker run -d -e POSTGRES_PASSWORD=password pg_searcher:0.0.1
```

To initialize the fdw
```
docker exec {container id} psql -f install_extension.sql
``` 

