# FormScrape

**Form Scrape** is a lightweight Python program designed to scrape web forms from the current webpage. It extracts form questions and relevant metadata, then communicates this information via an API to receive responses to the form's questions.

## Features
- Scrapes web forms from the current webpage
- Extracts form fields and associated labels
- Sends scraped data to a remote API
- Receives and handles API responses with answers to the form questions

## Requirements
some of the steps can be skipped
1. **Have python installed**

2. **(optional) Create a virtual environment for the project**
	-in the shell (cmd/powershell etc.), type the following "python -m venv vEnv" (this will create the environment in the current directory)
	-activate the environment by going to the scripts folder and type "./activate"
	-install the necessary modules by typing "pip install selenium" and "pip install requests"

3. **Install the necessary modules by typing "python -m pip install selenium" and "python -m pip install requests"**

4. **Open a google chrome session with an open debugging port by typing the following**
path/to/chrome/chrome.exe --remote-debugging-port=9000 --user-data-dir="directory/of/your/choice"
	- Replace the "path/to/chrome" in the above text with the path to your chrome executable on your device.
	- The "directory/of/your/choice" can be whatever, that will be where that sessions user data is going to be saved.
	- A potential problem could be parsing the path to chrome, if the path contains spaces e.g "System Files", you the path should be fixed like this:
		C:\"Program Files"\Google etc.

5. **When you are on the webpage you want to scrape, just run the program. You can do that in the command line by typing "Python ./moodleScrape.py**

## Disclaimer
This tool is intended for educational or authorized automation purposes only. Always ensure you have permission before scraping and submitting forms on any website.
