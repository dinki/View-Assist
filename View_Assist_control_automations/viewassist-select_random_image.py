import os
import random

@service(supports_response="optional")
def select_random_image(directory: str = "/config/www/viewassist/backgrounds/"):
    """yaml
    name: View Assist Select Random Image
    description: Selects a random image from the specified directory
    """
    valid_extensions = ('.jpeg', '.jpg', '.tif', '.png')

    # Translate /local/ to /config/www/ for directory validation
    if directory.startswith("/local/"):
        filesystem_directory = directory.replace("/local/", "/config/www/", 1)
    else:
        filesystem_directory = directory

    # Verify the directory exists
    if not os.path.isdir(filesystem_directory):
        return {"error": f"The directory '{filesystem_directory}' does not exist."}

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
