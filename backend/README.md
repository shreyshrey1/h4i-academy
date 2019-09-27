# url shortener

A simple web service that takes a full URL:

```
http://example.org/link/to/something/long
```

And returns a "shorter" aliased URL relative to localhost:

```
http://127.0.0.1:3000/abc
```

This shorter URL, when visited, should redirect to the original using a 300-level status code.

## Requirements

No database - this should all be done in memory to keep it simple.

## Setup

```
pip install flask
```

## Run the server

```
python server.py
```
