import os
import random
import requests
import uuid
import io

@service(supports_response="optional")
def select_random_image(directory: str = "/config/www/viewassist/backgrounds/", local: bool = True):
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
    
    if local:
        valid_extensions = ('.jpeg', '.jpg', '.tif', '.png')

        # List only image files with the valid extensions
        images = [f for f in os.listdir(filesystem_directory) if f.lower().endswith(valid_extensions)]

        # Check if any images were found
        if not images:
            return {"error": f"No images found in the directory '{filesystem_directory}'."}

        # Select a random image
        selected_image = random.choice(images)

    else:
        # source: https://unsplash.it/640/425?random
        # make temporary dir
        temp_dir = f"{directory}temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        else:
            # delete all files in temporary dir
            jpgs = [f for f in os.listdir(temp_dir) if f.lower().endswith(".jpg")]
            for f in jpgs:
                os.remove(f"{temp_dir}/{f}")
        #store file in guid from source
        url = "https://unsplash.it/640/425?random"
        
        #response = requests.get(url)
        response = task.executor(requests.get, url)
        
        if response.status_code == 200:
            # Generate a random GUID
            random_guid = uuid.uuid4()
            filename = f"{temp_dir}/{random_guid}.jpg"
            
            #with open(filename, "wb") as file:
            with task.executor(io.open,filename, "wb") as file:
                task.executor(file.write, response.content)
            #print("Retrieved image, wrote as {0}".format(filename))
            selected_image = f"{random_guid}.jpg"
            
        else:
            #print("Failed to retrieve the image. Status code:",
            #      response.status_code)
            selected_image = ""
    
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
