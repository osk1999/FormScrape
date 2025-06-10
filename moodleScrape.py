import selenium
import requests
import selenium.webdriver
import json

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
TEST_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfz3bbNhn17DITvuRMElbO1O6U1kOiFy1EyPebtO3Lz8jgRfg/viewform?usp=header"


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

