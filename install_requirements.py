import subprocess
import sys
import os

def install_requirements():
    requirements_file = 'requirements.txt'

    # Check if the requirements file exists
    if os.path.isfile(requirements_file):
        try:
            # Attempt to install dependencies listed in the requirements file
            print(f"Installing dependencies from {requirements_file}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
            print("All dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            # Handle errors that occur during installation
            print(f"An error occurred while installing dependencies: {e}")
    else:
        # Notify the user if the requirements file is not found
        print(f"{requirements_file} not found. Please ensure the file exists in the current directory.")


# Automatically install requirements if the script is executed directly
if __name__ == "__main__":
    install_requirements()