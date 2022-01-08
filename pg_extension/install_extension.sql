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
    hostname  'http://sql_searcher_backend:8080'
);