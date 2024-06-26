import requests
import random
import time

while True:
        
        time.sleep(random.randint(100,120))
        lis=['欢迎各位老板光临乌龟的直播间~','主播真的是人美声甜哟','欢迎各位老板上车','粉丝灯牌即可上车，童叟无欺哦~']
        word = random.choice(lis)
        url='https://api.live.bilibili.com/msg/send'

        data={
                'bubble': '0',
            'msg': word,
            'color': '5566168',
            'mode': '1',
            'room_type': '0',
            'jumpfrom': '82001',
            'reply_mid': '0',
            'reply_attr': '0',
            'replay_dmid': '',
            'statistics': '{"appId":100,"platform":5}',
            'fontsize': '25',
            'rnd': '1712769324',
            'roomid': '32040184',
            'csrf': '7370c0c52c95fdcb27ed7867c09f2c80',
            'csrf_token': '7370c0c52c95fdcb27ed7867c09f2c80',
        }
        headers={
                'Cookie': 'buvid3=462B204F-5095-1E9D-5723-7CC4013AE23A56760infoc; b_nut=1694420856; i-wanna-go-back=-1; b_ut=7; _uuid=8315E36A-7F56-5D82-D4BB-8CDC882A699956869infoc; buvid4=4D253BA1-8A82-A27B-8897-5EA5CDB3ADDE57450-023091116-z1vuhgWtceW91PwasfbFmQ%3D%3D; rpdid=|(klY~ukYu))0J\'uYmRRk|)~R; DedeUserID=364367980; DedeUserID__ckMd5=d583aa56dbea9a3d; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO2016945181856922; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; enable_web_push=DISABLE; header_theme_version=CLOSE; FEED_LIVE_VERSION=V_FAVOR_WATCH_LATER; fingerprint=d9ec586590c88761a29b468817eebd76; SESSDATA=1aa9c0cc%2C1728132269%2C521c9%2A42CjB56aBFj93b3c0NuZdlfvmNSiXUT0AOQoRCOfezeg3qJIkMDwAiG4OjeXUQGZtaO7wSVldyQTJiZGx6SkRLWkF0OGNVU2liU1J1LVV5aXBXU0ttZkhtLXJYakhvOEJjNkJVYTBqZUdGTWZTbGNhdWFWSktaclRILVJjemtQT2pxUWZkMVJWUGd3IIEC; bili_jct=7370c0c52c95fdcb27ed7867c09f2c80; sid=69przd03; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTI4Mzk1MDIsImlhdCI6MTcxMjU4MDI0MiwicGx0IjotMX0.lFW7Ko7prihow2F5CIjiGQ_0pMp5crBwexZ63FbNHSM; bili_ticket_expires=1712839442; home_feed_column=5; browser_resolution=1528-750; buvid_fp=d9ec586590c88761a29b468817eebd76; b_lsid=10DFD10B84_18EC8BCD6CD; CURRENT_QUALITY=116; bp_video_offset_364367980=918809919715541010; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1712587716,1712656778,1712679321,1712767355; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1712769211; PVID=3',
                'Origin': 'https://live.bilibili.com',
                'Referer':'https://live.bilibili.com/32040184?live_from=82001&broadcast_type=0&spm_id_from=333.1007.top_right_bar_window_dynamic.content.click',
                'Sec-Ch-Ua':'"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform':"Windows",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }

        response = requests.post(url=url, data=data,headers=headers)
        print(response.json())