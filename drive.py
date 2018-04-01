
# Include the Dropbox SDK
import dropbox
import requests
import os
assert dropbox
class RemoteManager:
    def __init__(self):
        self.access_token='i7l8kexaJPAAAAAAAAABtaE_9wmLol-0Wqh3jY0p2_V3YoCTgagLHzwZ3OJXqEUy'
        self.dbx = dropbox.Dropbox(self.access_token)
        self.dbx.users_get_current_account()
        self.url = "https://webdb-199518.appspot.com/"
        self.GET_VALUE = "getvalue"
        self.STORE_VALUE = "storeavalue"
    def ls(self,path=''):
        return  self.dbx.files_list_folder(path).entries
    def get(self,path,local_path='./'):
        self.dbx.files_download_to_file(local_path,'/'+path)
    def put(self,fi,path):
        with open(fi, 'rb') as f:
            self.dbx.files_upload(f.read(), '/'+path,mode=dropbox.files.WriteMode('overwrite', None))
    def listen(self,option):
        r = requests.post(self.url+self.GET_VALUE, {"tag":option})
        text = r.json()
        print(text)
        req = bool(int(text[2][1]))
        return req
    def say(self,option,v):
        requests.post(self.url+self.STORE_VALUE, {"tag":option,"value":v})

if __name__ == '__main__':
    rm=RemoteManager()
    while True:
        if rm.listen()==True:
            print('downloading')
            rm.get('recording1.3gp','./data/record/record.3gp')
            os.system('cd ./data/record/ && ffmpeg -y -i record.3gp -crf 18 record.wav' )
