import requests, time, os
from dotenv import load_dotenv

load_dotenv()
headers = {"keyId": os.getenv('API_KEY_ID'), "keySecret": os.getenv('API_KEY_SECRET')}

def create(file_name):
    files = {}
    create_url = "https://api.speechflow.io/asr/file/v1/create?lang=ru"

    files['file'] = open(file_name, "rb")
    response = requests.post(create_url, headers=headers, files=files)
    if response.status_code == 200:
        create_result = response.json()
        if create_result["code"] == 10000:
            task_id = create_result["taskId"]
        else:
            task_id = ""
    else:
        print('create request failed: ', response.status_code)
        task_id = ""
    return task_id
 
 
def query(task_id):
    query_url = "https://api.speechflow.io/asr/file/v1/query?taskId=" + task_id + "&resultType=1"
    while (True):
        response = requests.get(query_url, headers=headers)
        if response.status_code == 200:
            query_result = response.json()
            if query_result["code"] == 11000:
                result = ""
                for sentence in eval(query_result["result"])["sentences"]:
                    result += sentence['s']+" "
                if result:
                    return str(result)
                else:
                    return "Не удалось распознать текст."
            elif query_result["code"] == 11001:
                time.sleep(3)
                continue
            else:
                print(query_result)
                print("transcription error:")
                print(query_result['msg'])
                break
        else:
            print('query request failed: ', response.status_code)
 
def start_speech_flow(file_name):
    task_id = create(file_name)
    if (task_id != ""):
        return query(task_id)