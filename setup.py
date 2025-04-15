"""
Setup script for the Bangalore Accident Prevention System.

This script helps with setting up the environment and installing dependencies.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required.")
        print(f"Current Python version: {platform.python_version()}")
        return False
    return True

def create_virtual_env():
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

def install_dependencies():
    """Install dependencies from requirements.txt."""
    print("Installing dependencies...")
    
    # Determine the pip command based on the platform
    if platform.system() == "Windows":
        pip_cmd = os.path.join("venv", "Scripts", "pip")
    else:
        pip_cmd = os.path.join("venv", "bin", "pip")
    
    # Upgrade pip
    subprocess.run([pip_cmd, "install", "--upgrade", "pip"])
    
    # Install core dependencies
    print("Installing core dependencies...")
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("Core dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Warning: Some dependencies could not be installed.")
        print("Attempting to install dependencies in smaller groups...")
        
        # Try installing in smaller groups
        dependency_groups = [
            ["streamlit", "pandas", "numpy"],
            ["folium", "streamlit-folium", "geopy", "networkx"],
            ["requests", "openmeteo-requests", "retry-requests", "python-dotenv"],
            ["plotly"],
            ["opencv-python", "scikit-learn"],
            ["pillow"]
        ]
        
        for group in dependency_groups:
            try:
                print(f"Installing: {', '.join(group)}")
                subprocess.run([pip_cmd, "install"] + group)
            except Exception as e:
                print(f"Warning: Could not install {group}. Error: {e}")

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        "src/data/videos",
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            print(f"Creating directory: {directory}")
            os.makedirs(directory, exist_ok=True)

def main():
    """Main function to set up the environment."""
    print("Setting up Bangalore Accident Prevention System...")
    
    if not check_python_version():
        return
    
    create_virtual_env()
    install_dependencies()
    create_directories()
    
    print("\nSetup completed!")
    print("\nTo activate the virtual environment:")
    if platform.system() == "Windows":
        print("    venv\\Scripts\\activate")
    else:
        print("    source venv/bin/activate")
    
    print("\nTo run the application:")
    print("    streamlit run app.py")

if __name__ == "__main__":
    main()
