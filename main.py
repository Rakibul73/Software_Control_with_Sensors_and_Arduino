import time
from pymata4 import pymata4
import os
import subprocess
from pynput.keyboard import Key, Controller
keyboard = Controller()



trigpin = 11       # trigger pin no
ecopin = 12        # echo pin no
gggg = 0

board = pymata4.Pymata4()

def the_callback(data):
    global gggg
    
    print("distance: ", data[2])    # data list has 4 index, we need only distance which stores in data[2] index
    if data[2] < 10 and gggg == 0:  # if distance 10 , then execute 
        gggg = 1
        os.startfile("C:\\Users\\spry-shanto\\Desktop\\Anime_Online_Site_List.txt") # opens a excel file with given path
    elif gggg == 1 and data[2] > 10:
        keyboard.press(Key.ctrl)         # press ctrl+s 
        keyboard.press('s')              # press ctrl+s 
        keyboard.release('s')            # press ctrl+s 
        keyboard.release(Key.ctrl)       # press ctrl+s 
        subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)  #kills the excel.exe forcefully
        
        # Google drive Upload part
        
        from googleapiclient.http import MediaFileUpload
        from Google import Create_Service

        CLIENT_SECRET_FILE = 'credentials.json'
        API_NAME = 'drive'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        # Upload and Replace a file
        file_name = 'Anime_Online_Site_List.txt'
        file_id = None

        # Check if the file already exists in Google Drive
        results = service.files().list(
            q=f"name='{file_name}'",
            spaces='drive',
            fields='files(id, name)',
            pageSize=10
        ).execute()

        items = results.get('files', [])

        if items:
            # If the file exists, get its ID to replace it later
            file_id = items[0]['id']
            

        # Upload the file
        file_metadata = {
            'name': file_name,
        }

        media_content = MediaFileUpload(file_name, mimetype="text/plain")

        if file_id:
            # If the file exists, update its content with the new file
            file = service.files().update(
                fileId=file_id,
                addParents='1SWdL7_Wk2CCbU0fXukeFCYa7GMFNkd4S',  # folder ID where to upload
                body=file_metadata,
                media_body=media_content
            ).execute()
        else:
            # If the file doesn't exist, create a new file
            file_metadata['parents'] = ['1SWdL7_Wk2CCbU0fXukeFCYa7GMFNkd4S']
            file = service.files().create(
                body=file_metadata,
                media_body=media_content
            ).execute()

        print(file)

        
        gggg = 0


# def the_callback(data):
#     print("distance: ", data[2] , " ", data[0] , " " , data[1] , "\n" , date)
#     if data[2] < 10:
        
#         os.startfile("D:\\Mine\\Anime_Online_Site_List.txt")
#     else:
#         subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)


board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)
    except:
        board.shutdown()