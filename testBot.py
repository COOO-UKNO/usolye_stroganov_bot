import requests
from dotenv import load_dotenv
import os


load_dotenv()
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
FILE_PATH = "disk:/УКНО/Черноисточинск/test.xlsx"  # Проверьте путь!

def download_yandex_disk_file(oauth_token, file_path):
    # Проверка токена
    check = requests.get(
        "https://cloud-api.yandex.net/v1/disk",
        headers={"Authorization": f"OAuth {oauth_token}"}
    )
    if check.status_code != 200:
        print("Ошибка токена:", check.json())
        return

    # Запрос на скачивание
    api_url = "https://cloud-api.yandex.net/v1/disk/resources/download"
    headers = {"Authorization": f"OAuth {oauth_token}"}
    params = {"path": file_path}
    
    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Проверка HTTP-ошибок
        download_url = response.json().get("href")
        
        if download_url:
            file_data = requests.get(download_url)
            file_data.raise_for_status()
            with open("test.xlsx", "wb") as f:
                f.write(file_data.content)
            print("Файл скачан!")
        else:
            print("Ошибка: Ссылка не получена. Ответ API:", response.json())
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-ошибка {e.response.status_code}:", e.response.json())
    except Exception as e:
        print("Ошибка:", e)

download_yandex_disk_file(OAUTH_TOKEN, FILE_PATH)
