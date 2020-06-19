import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('url here') # The link where you store your HWIDS e.g. a raw pastebin

try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not in database')
        print(f'HWID: {hwid}') # prints HWID for user to copy
        time.sleep(10)
except:
    print('[ERROR] Failed to connect to database')
    print(f'HWID: {hwid}') # prints HWID for user to copy
    time.sleep(10)
    
os.system('title HWID Authentication Demo')

print('Welcome')
