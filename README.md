# 📊 KFQ ISCC AutoReporter

Automatic ISCC Korea certification report generator.

## Features

- Automatic CSV download from ISCC website
- Data analysis using Pandas
- Excel report generation
- HTML summary generation
- Automatic email delivery
- Windows Task Scheduler automation

## Tech Stack

- Python
- Selenium
- Pandas
- OpenPyXL
- SMTP
- HTML

## Project Structure

```text
ISCC_Report/
├── downloader.py
├── report.py
├── mail.py
├── main.py
├── requirements.txt
└── README.md
```

## Workflow

```text
ISCC Website
      ↓
Download CSV
      ↓
Analyze Data
      ↓
Generate Excel
      ↓
Generate HTML
      ↓
Send Email
```

## Author

Heejun Kwon