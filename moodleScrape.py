import selenium
import requests
import selenium.webdriver
import json
import os

API_KEY =  os.environ.get('Scrape_APIKEY')
API_URL =  os.environ.get('Scrape_APIURL')


def main():
    print("WORKING...")
    page_source = get_page_source()

    response = requests.post(
        url=API_URL,

        headers = {
            "Authorization" : f"Bearer {API_KEY}",
            "Content-Type" : "application/json",
        },

        data = json.dumps({
            "model" : "deepseek/deepseek-chat:free",
            "messages" : [
                {
                    "role" : "user",
                    "content" : str(page_source)+"\n answer all the questions that are included in the source code provided above. Provide only the answers and nothing else please",
                }
            ],
        })
    )

    response_parsed = response.json()["choices"][0]["message"]["content"]

    print(response_parsed)


def get_page_source():
    cur_address = "localhost:9000"
    options = selenium.webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", cur_address)

    driver = selenium.webdriver.Chrome(options=options)

    page_source = driver.page_source

    return page_source


if __name__ == "__main__":
    main()

