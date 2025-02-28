# CDP Chatbot

This chatbot answers "how-to" questions about Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap.

## Features
- Extracts relevant data from official documentation
- Handles various question formats
- Provides direct answers with references

## Setup

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Scraper
```bash
python scraper.py
```

### Index the Data
```bash
python indexer.py
```

### Start the Chatbot API
```bash
uvicorn chatbot_api:app --reload
```

### Ask Questions
Open a browser and enter:
```
http://127.0.0.1:8000/ask?query=How to set up a source in Segment?
```

## Author
Created for educational purposes.
