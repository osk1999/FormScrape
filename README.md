# FormScrape

**Form Scrape** is a lightweight Python program designed to scrape web forms from the current webpage. It extracts form questions and relevant metadata, then communicates this information via an API to receive responses to the form's questions.

## Features
- Scrapes web forms from the current webpage
- Extracts form fields and associated labels
- Sends scraped data to a remote API
- Receives and handles API responses with answers to the form questions

## Requirements
1. **Have Python installed**  
   Ensure Python 3.7 or later is installed on your system.

2. **(Optional) Create a virtual environment**  
   This helps isolate project dependencies:
   - In the shell (cmd/PowerShell/etc.), type:  
     ```
     python -m venv vEnv
     ```
   - Activate the environment:
     ```
     ./vEnv/Scripts/activate
     ```
   - Install required modules:
     ```
     pip install selenium
     pip install requests
     ```

3. **Install the necessary modules (without virtual environment)**  
   You can also install the modules globally:

## Disclaimer
This tool is intended for educational or authorized automation purposes only. Always ensure you have permission before scraping and submitting forms on any website.
