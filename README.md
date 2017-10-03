# News Site Reporting Tool

A reporting tool for a news site that processes the data on the site's database and outputs consolidated reports as plain text.

## Getting Started

Reporting tool main script is `news_reporting_tool.py`. Database connection is handled by `news_reporting_tool.py` module.

Make sure the python files are located where the database is. Use:
```
python3 news_reporting_tool.py
```

Check the *.txt files for report outputs. You can change the output file names from `news_reporting_tool.py`.

### Prerequisites

This project requires a pre-populated PostgreSQL database.