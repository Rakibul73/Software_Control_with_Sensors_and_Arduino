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
    print("dsfdgdgdffsdf")

# Upload the file
file_metadata = {
    'name': file_name,
}

media_content = MediaFileUpload(file_name, mimetype="text/plain")

if file_id:
    print("zzzzzzzzzzzzzzz")
    # If the file exists, update its content with the new file
    file = service.files().update(
        fileId=file_id,
        addParents='1SWdL7_Wk2CCbU0fXukeFCYa7GMFNkd4S',
        body=file_metadata,
        media_body=media_content
    ).execute()
else:
    print("xxxxxxxxxxxxxxxxxx")
    # If the file doesn't exist, create a new file
    file_metadata['parents'] = ['1SWdL7_Wk2CCbU0fXukeFCYa7GMFNkd4S']
    file = service.files().create(
        body=file_metadata,
        media_body=media_content
    ).execute()

print(file)
