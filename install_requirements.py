import subprocess
import sys
import os


def install_requirements():
    requirements_file = 'requirements.txt'

    if os.path.isfile(requirements_file):
        try:
            print(f"Installing dependencies from {requirements_file}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
            print("All dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing dependencies: {e}")
    else:
        print(f"{requirements_file} not found. Please ensure the file exists in the current directory.")


if __name__ == "__main__":
    install_requirements()
