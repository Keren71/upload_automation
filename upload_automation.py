import os
import time
import subprocess
import shutil

# Define directories
source_folder = "C:/Users/pc/Pictures/Captures"
uploaded_folder = "C:/Users/pc/Pictures/uploaded"

# Ensure the uploaded folder exists
os.makedirs(uploaded_folder, exist_ok=True)

# Define the upload URL
upload_url = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

# Monitor the source folder
print("Monitoring folder:", source_folder)

while True:
    try:
        # List all files in the source folder
        files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

        for file in files:
            file_path = os.path.join(source_folder, file)
            # Wait 30 seconds
            print(f"Waiting 30 seconds before uploading: {file}")
            time.sleep(30)

            # Execute the curl command
            try:
                print(f"Uploading: {file}")
                response = subprocess.run(
                    ["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", upload_url],
                    capture_output=True,
                    text=True
                )

                if response.returncode == 0:
                    print(f"Upload successful for: {file}")
                    # Move the file to the uploaded folder
                    shutil.move(file_path, os.path.join(uploaded_folder, file))
                else:
                    print(f"Upload failed for: {file}. Error: {response.stderr}")

            except Exception as e:
                print(f"Error uploading file {file}: {e}")

    except Exception as e:
        print(f"Error monitoring folder: {e}")

    # Pause briefly before checking the folder again
    time.sleep(5)
