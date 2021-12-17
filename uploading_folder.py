import os
from posixpath import relpath
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
        

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,"rb") as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))


def main():
    access_token = "sl.A-WcxHKB4kV11k4O8o5rVrAxDgiK6EP_iWDfGpEQSGE9hPj6LiOhZSKYG2c_rrmBW82rbqtVb0C93UUhxSWWBTIAdxmB3_XyJ9kZ-Qod8szxEyy7grk74Fr7QItGt0TIIoitkdc"
    transferData = TransferData(access_token)

    file_from = str(input("Enter file pathg to transfer : "))
    file_to = input("Enter the full path to upload to dropbox : ")

    transferData.upload_file(file_from,file_to)
    print("file as be moved")

main()
        