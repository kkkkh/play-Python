# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5

# 设置你的appid和appkey
appid = ""
appkey = ""

from_lang = "en"
to_lang = "zh"
endpoint = "http://api.fanyi.baidu.com"
path = "/api/trans/vip/translate"
url = endpoint + path


def make_md5(s, encoding="utf-8"):
    return md5(s.encode(encoding)).hexdigest()


def baidu_translate_en2zh(query):
    if len(query) > 50:
        raise Exception("翻译文本过长超过50个字符")
    """
    传入英文字符串，返回百度翻译的中文结果
    """
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "appid": appid,
        "q": query,
        "from": from_lang,
        "to": to_lang,
        "salt": salt,
        "sign": sign,
    }
    try:
        r = requests.post(url, params=payload, headers=headers, timeout=5)
        result = r.json()
        # result = {"trans_result": [{"dst": "你好"}]}
        # print("翻译 result", result)
        # 检查返回结果
        if "trans_result" in result:
            # 支持多段翻译，拼接所有段落
            return "\n".join([item["dst"] for item in result["trans_result"]])
        else:
            # 返回错误信息
            raise Exception("翻译失败")
    except Exception as e:
        print("翻译异常", e)
        raise e


# 示例用法
if __name__ == "__main__":
    en_text = "Hello World! This is 1st paragraph.\nThis is 2nd paragraph."
    zh_text = baidu_translate_en2zh(en_text)
    print(zh_text)
