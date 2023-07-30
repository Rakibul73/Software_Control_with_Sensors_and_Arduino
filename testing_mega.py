from mega import Mega

def upload_to_mega(mega_email, mega_password, file_path, remote_folder_name=None):
    # Create an instance of Mega class
    mega = Mega()
    print("mega = Mega()")

    # Log in to your Mega account
    m = mega.login(mega_email, mega_password)
    print("m = mega.login(mega_email, mega_password)")

    # Get the root folder of your Mega account
    root_folder = m.find('root')
    print("root_folder = m.find('root')")

    # Find or create the remote folder where you want to upload the file
    remote_folder = m.find(remote_folder_name) if remote_folder_name else root_folder
    print("remote_folder = m.find(remote_folder_name) if remote_folder_name else root_folder")

    # Upload the file
    uploaded_file = m.upload(file_path, remote_folder)
    print("uploaded_file = m.upload(file_path, remote_folder)")
    
    # Get the public handle (file share link) from the uploaded file information
    public_handle = uploaded_file['h']
    print("public_handle = uploaded_file['h']")
    
    # Return the public handle (file share link)
    return public_handle

# Usage example
if __name__ == "__main__":
    # Replace 'your_mega_email', 'your_mega_password', and 'path/to/your/file.ext'
    # with your Mega credentials and the actual path to your file
    public_handle = upload_to_mega('your_mega_email', 'your_mega_password', 'D:/Mine/Anime_Online_Site_List.txt', remote_folder_name='optional_remote_folder_name')
    print("File share link (public handle): https://mega.nz/file/" + public_handle)
