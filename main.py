import requests
from fastapi import FastAPI, HTTPException
from user_agent import generate_user_agent as abo
import uuid
import string
import random

# إنشاء التطبيق باستخدام FastAPI
app = FastAPI()

# تعريف الفئة S1
class S1:
    def __init__(self):
        self.tok = ''
        self.id = ''
        self.g = 0
        self.gb = 0
        self.b = 0

    def rest(self, user):
        email=user+"@gmail.com"
        y = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        h = {
            'Content-Length': '328',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 320dpi; 720x1339; realme; RMX3269; RED8F6; RMX3265; ar_IQ)',
            'Cookie': 'mid=Z0ZQoQABAAFHk8B-qvDkQ4bq_XLc; csrftoken=wf5gPNZiHZptDbscGF9l1QX2YYNgi1oK',
            'Cookie2': '$Version=1',
            'Accept-Language': 'ar-IQ, en-US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
        }
        d = {
            'user_email': email,
            'device_id': uuid.uuid4(),
            'guid': uuid.uuid4(),
            '_csrftoken': y
        }
        re = requests.post(url, headers=h, data=d).json()
        try:
            return re["obfuscated_email"]
        except:
            return ''

    def date_sc(self, Id):
        try:
            if 1 < int(Id) < 1279000:
                return 2010
            elif 1279001 < int(Id) < 17750000:
                return 2011
            elif 17750001 < int(Id) < 279760000:
                return 2012
            elif 279760001 < int(Id) < 900990000:
                return 2013
            elif 900990001 < int(Id) < 1629010000:
                return 2014
            elif 1900000000 < int(Id) < 2500000000:
                return 2015
            elif 2500000000 < int(Id) < 3713668786:
                return 2016
            elif 3713668786 < int(Id) < 5699785217:
                return 2017
            elif 5699785217 < int(Id) < 8507940634:
                return 2018
            elif 8507940634 < int(Id) < 21254029834:
                return 2019
            else:
                return "2020-2023"
        except:
            return ''

    def inf(self, user):
    
        cookies = {
            'datr': 'lhI2Z-qsh_SE2tBAm-z9sT8c',
            'ig_did': 'FBBFF354-5D64-40BE-82A6-F40D4C80FC4E',
            'mid': 'ZzYSlgABAAFR3pvSs-MtncGVPir1',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'dpr': '2.1988937854766846',
            'ds_user_id': '277613183',
            'csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'wd': '891x1654',
            'rur': '"LLA\\054277613183\\0541764135205:01f7191faf0392a232a09e8551689df778531b54d6147fb6b0ee28550084ef623409d5ce"',
        }
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.instagram.com/dd/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(abo()),
            'x-asbd-id': '129477',
            'x-csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR07T_Q0xaDQfazO_ogFm4DlAfLnCNNeQ0b0skK1F4sWzJzO',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {
            'username': user,
        }

        res = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', params=params, cookies=cookies, headers=headers)
        pp = res.json()

        try:
            biography = pp["data"]["user"]["biography"]
        except:
            biography = None

        try:
            followers = pp["data"]["user"]["edge_followed_by"]["count"]
        except:
            followers = None

        try:
            following = pp["data"]["user"]["edge_follow"]["count"]
        except:
            following = None

        try:
            user_id = pp["data"]["user"]["id"]
            data_year = self.date_sc(user_id)
        except:
            user_id = None
            data_year=self.date_sc(user_id)

        try:
            is_private = pp["data"]["user"]["is_private"]
        except:
            is_private = None

        try:
            username = pp["data"]["user"]["username"]
        except:
            username = None

        try:
            post_count = pp["data"]["user"]["edge_owner_to_timeline_media"]["count"]
        except:
            post_count = None

        try:
            full_name = pp["data"]["user"]["full_name"]
        except:
            full_name = None

        reset_info = self.rest(user)

        return {
            "full_name": full_name,
            "username": username,
            "email": f"{user}@gmail.com",
            "reset_info": reset_info,
            "following": following,
            "followers": followers,
            "user_id": user_id,
            "is_private": is_private,
            "post_count": post_count,
            "data_year": data_year,
            "biography": biography,
            "By":"@jokerpython3"
        }


# مسار FastAPI لجلب معلومات الحساب
@app.get("/infoIg/")
async def get_instagram_info(user: str):
    try:
        info = S1().inf(user)
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
