import requests
import json

def watson_request():
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=ja-JP_BroadbandModel'
    username = '*'
    password = '*'

    headers = {'Content-Type': 'audio/wav'}

    audio = open('output.wav','rb')

    r = requests.post(url, data=audio,headers=headers,auth=(username,password),)

    res = json.loads(r.text)

    watson_text = ""
    for result in res['results']:
        for alternative in result['alternatives']:
            watson_text += alternative['transcript']
    print(watson_text.strip())
    #print(res)
    
    return watson_text
    
if __name__ == "__main__":
    watson_request()
