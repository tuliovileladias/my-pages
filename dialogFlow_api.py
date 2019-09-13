# _*_ coding: utf-8 _*_

__author__ = "Tulio Dias"
__copyright__ = "Copyright 2019, Inatel Competence Center"
__credits__ = "Inatel"
__license__ = "MIT"
__maintainer__ = "Tulio Dias"
__email__ = "tuliodias@inatel.br"

import json
import requests
import time

google_api_key = "AIzaSyB6We3fHS45qXGA3f0N2SSafaIrIM2X1mY"
client_access_token = "6a7f22983443430fb8abc5f47d8757ce"
developer_access_token = "6ed1d18c2e6f4d4d87e55ca5ae5c3399"
project_id = "teste-gsxvkr"
service_account = "dialogflow-nwqdyl@teste-gsxvkr.iam.gserviceaccount.com"
headers = {
    "Content-Type": "application/json"
}


#https://dialogflow.googleapis.com/v2/projects/*/agent?access_token=6a7f22983443430fb8abc5f47d8757ce&key=[YOUR_API_KEY] HTTP/1.1





def get_agents():
    global headers
    r = requests.get("https://dialogflow.googleapis.com/v2/projects/teste-gsxvkr/agent?key="+google_api_key, headers=headers)
    print(r)
    resposta = ""
    try:
        resposta = r.json()
    except:
        print("Error - JSON")
    print(resposta)


def function_base():


    data = json.dumps({
        "info": "valor"
    })

    r = requests.post("https://link", headers=headers, data=data)
    resposta = ""
    try:
        resposta = r.json()
    except:
        print("Error - JSON")



get_agents()