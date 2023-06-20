from flask import Flask, make_response, request
import requests
import json
import pandas as pd
from slacker import Slacker
from crawling_code import *
from links_code import *
from nouns_code import *
import os

#개인 토큰은 제외했습니다.
token = ""
app = Flask(__name__)
slack = Slacker(token)

g = open("/Users/hanuri/Desktop/capstone_design/result/wordcloud.png")

def get_answer(user_query):
    trim_text = user_query.replace(" ", "")
    link_dict = {
        '링크': '링크'
        }
    wc_dict = {
        '워드클라우드': '워드클라우드'
    }
    manual_dict = {
        '사용법': '크롤링 후 링크와 워드 클라우드를 생성하는 데 시간이 걸리니 크롤링 할 단어 입력 후 1분 정도 지난 후 링크 또는 워드 클라우드를 입력해주세요.'
    }
    if trim_text in link_dict.keys():
        f = pd.read_csv("/Users/hanuri/Desktop/capstone_design/result/links.csv")
        return f['link'][0]
    elif trim_text in wc_dict.keys():
        global g
        g = open("/Users/hanuri/Desktop/capstone_design/result/wordcloud.png")
        return wc_dict[trim_text]
    elif trim_text in manual_dict.keys():
        return manual_dict[trim_text]
    else:
        return crawler(trim_text), nouns(), link()

def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)
    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:
        try:
            user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
            answer = get_answer(user_query)
            if answer == '워드클라우드':
                response = requests.post("https://slack.com/api/files.upload",
                                          headers={'content_type': 'application/x-www-form-urlencoded',
                                                                   "Authorization": "Bearer " + token},
                                          data={"channels": channel, 'text': answer},
                                          files={"file": g})
            else :
                response = requests.post("https://slack.com/api/chat.postMessage",
                                         headers={"content_type": "application/json",
                                                  "Authorization": "Bearer " + token},
                                         data={"channel": channel, "text": answer})
            return make_response("ok", 200, )
        except IndexError:
            pass
    message = "[%s] cannot find event handler" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200)
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run(debug=True)
