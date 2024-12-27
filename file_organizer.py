import os  
import shutil  

# Directory of the files to organize
directory = r'D:\Downloads'

# Categories of the file type and their corresponding extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],  
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],  
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],  
    'Music': ['.mp3', '.wav', '.aac'],  
    'Archives': ['.zip', '.rar', '.tar', '.gz'],  
    'Others': [] 
}

# Create folders for each category if they don't already exist
for folder in file_types.keys():
    folder_path = os.path.join(directory, folder)  # Creating the path for each folder
    if not os.path.exists(folder_path):  # Check if folder doesn't exist
        os.makedirs(folder_path)  # Create the folder

# Iterate through all files in the directory
for filename in os.listdir(directory):  # List all files in the directory
    file_path = os.path.join(directory, filename)  # Get the full path of the file
    if os.path.isfile(file_path):  # Check if it's a file (not a folder)
        file_extension = os.path.splitext(filename)[1].lower()  # Get the file extension and make it lowercase
        for folder, extensions in file_types.items():  # Check each file type category
            if file_extension in extensions:  # If the file's extension matches a category
                shutil.move(file_path, os.path.join(directory, folder, filename))  # Move the file to the appropriate folder
                break  # Stop checking other categories once the file is moved

