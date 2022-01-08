
```bash
# Install required packages
apt-get update
apt-get install --yes postgresql-server-dev-12 python3-setuptools python3-dev make gcc git

git clone git@github.com:sawtoothdata/Multicorn.git && cd Multicorn
PYTHON_OVERRIDE=python3.7 make 
sudo make install
```

for sql_searcher
```bash
sudo python3.7 -m pip install --system sql_searcher/
```

```sql
create extension multicorn;

CREATE SERVER sql_searcher_srv FOREIGN DATA WRAPPER multicorn
OPTIONS (
    wrapper 'sql_searcher.ConstantForeignDataWrapper'
);

CREATE FOREIGN TABLE sql_searcher_sample (
    q text,
    rank int,
    title text,
    link text,
    snippet text
) SERVER sql_searcher_srv
OPTIONS (
    hostname  'http://localhost:8000'
);
```

GOTCHA!
- run pg_config and check that the version of python you're linking to in postgres is the same you pip installed to!



