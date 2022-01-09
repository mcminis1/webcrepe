# WebCrepe

This is a postgres extension that connects to a google custom search project and allows you to write SQL and get results from the internet.

Current functionality is pretty limited. You can write a query using the google advanced query syntax and get the urls and brief descriptions back.

## Setup

Build instructions are in the backend and pg_extension folders. You'll need to build the images, then run docker-compose.

You must have a [google custom search engine](https://developers.google.com/custom-search) set up. You have to export your developer key and the search engine id into the app for it to work.
