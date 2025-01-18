import os
import random
import requests
import uuid
import io
import time

@service(supports_response="optional")
def select_random_image(directory: str = "/config/www/viewassist/backgrounds/", local: bool = True, max_images: int = 10):
    """yaml
    name: View Assist Select Random Image
    description: Selects a random image from the specified directory if local = True, or from unsplash.it is local = False
    """
    # Translate /local/ to /config/www/ for directory validation
    if directory.startswith("/local/"):
        filesystem_directory = directory.replace("/local/", "/config/www/", 1)
    else:
        filesystem_directory = directory

    # Verify the directory exists
    if not os.path.isdir(filesystem_directory):
        return {"error": f"The directory '{filesystem_directory}' does not exist."}
    if not local:
        # source: https://unsplash.it/640/425?random
        # make temporary dir
        filesystem_directory = f"{filesystem_directory}temp"
        
        if not os.path.exists(filesystem_directory):
            os.makedirs(filesystem_directory)
        
        # delete old downloaded files in temporary dir as configured by max_images
        jpg_files = []
        for filename in os.listdir(filesystem_directory):
            if filename.lower().endswith('.jpg'):
                file_path = os.path.join(filesystem_directory, filename)
                if os.path.isfile(file_path):
                    file_mtime = os.path.getmtime(file_path)
                    jpg_files.append((file_path, file_mtime))
        # Sort the list by modification time (oldest first)
        jpg_files.sort(key=lambda x: x[1])
        
        # Delete the oldest files if there are more than max_images
        if len(jpg_files) > max_images:
            files_to_delete = len(jpg_files) +1 - max_images
            for i in range(files_to_delete):
                #print(f"Deleting {jpg_files[i][0]}")
                task.executor(os.remove, jpg_files[i][0])
        
        #store file in guid from source
        url = "https://unsplash.it/640/425?random"
        try:
            response = task.executor(requests.get, url)
            if response.status_code == 200:
                # Generate a random GUID
                random_guid = uuid.uuid4()
                filename = f"{filesystem_directory}/{random_guid}.jpg"
                with task.executor(io.open,filename, "wb") as file:
                    task.executor(file.write, response.content)
                #selected_image = f"temp/{random_guid}.jpg"
            else:
                return {"error": f"Failed to retrieve an image from unsplash. Status code: {response.status_code}"}
                #selected_image = ""
        except Exception as e:
            #return {"error": f"Failed to retrieve an image from unsplash. Exception: {e}"}
            pass
            
    valid_extensions = ('.jpeg', '.jpg', '.tif', '.png')

    # List only image files with the valid extensions
    images = [f for f in os.listdir(filesystem_directory) if f.lower().endswith(valid_extensions)]

    # Check if any images were found
    if not images:
        return {"error": f"No images found in the directory '{filesystem_directory}'."}

    # Select a random image
    selected_image = random.choice(images)

    # Replace /config/www/ with /local/ for constructing the relative path
    if filesystem_directory.startswith("/config/www/"):
        relative_path = filesystem_directory.replace("/config/www/", "/local/")
    else:
        relative_path = directory
    # Ensure trailing slash in the relative path
    if not relative_path.endswith('/'):
        relative_path += '/'

    # Construct the image path
    image_path = f"{relative_path}{selected_image}"

    # Return the image path in a dictionary
    return {"image_path": image_path}
