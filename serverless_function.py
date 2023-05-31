import os
import requests

# URL of your Azure Function endpoint
url = "https://dob-func.azurewebsites.net/api/httptrigger13"

# Prompt the user to enter the folder path
folder_path = input("Enter the folder path:")

# Validate if the folder path exists
if not os.path.isdir(folder_path):
    print("Invalid folder path. Please provide a valid folder path.")
    exit()

# Get a list of file names in the folder
file_names = os.listdir(folder_path)

for file_name in file_names:
    # Construct the file path
    file_path = os.path.join(folder_path, file_name)

    # Read the file contents
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Create a dictionary with the file as 'file' key
    files = {"file": file_content}

    # Send a POST request to the Azure Function endpoint
    response = requests.post(url, files=files)

    # Check the response
    if response.status_code == 200:
        # Print the processed output

        output_file_path = os.path.join(folder_path, file_name + "_processed.txt")
        with open(output_file_path, "w") as output_file:
            output_file.write(response.text)
    else:
        # Print the error message
        print(f"Error: {response.text}")
