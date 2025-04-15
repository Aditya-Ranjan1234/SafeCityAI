# Installation Guide for Bangalore Accident Prevention System

This guide will help you set up the Bangalore Accident Prevention System on your local machine.

## Prerequisites

- Python 3.8 or higher
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/Aditya-Ranjan1234/SafeCityAI.git
cd SafeCityAI
```

## Step 2: Create and Activate a Virtual Environment

### On Windows:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

### On macOS/Linux:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

## Step 3: Install Dependencies

Install the core dependencies first:

```bash
pip install -r requirements.txt
```

If you encounter any dependency conflicts, try installing the packages in smaller groups:

```bash
# Core packages
pip install streamlit pandas numpy

# Mapping packages
pip install folium streamlit-folium geopy networkx

# API and data fetching
pip install requests openmeteo-requests retry-requests python-dotenv

# Data visualization
pip install plotly

# AI and ML components
pip install opencv-python scikit-learn

# Utility libraries
pip install pillow
```

## Step 4: Install Optional Dependencies

If you need additional features, you can install these optional dependencies:

```bash
# Additional visualization libraries
pip install matplotlib seaborn

# AI components
pip install langchain langchain-openai

# Multilingual support
pip install googletrans==4.0.0-rc1

# Advanced map visualizations
pip install pydeck
```

## Step 5: Download the CarCrash Dataset (Optional)

For the video surveillance and accident detection features:

```bash
git clone https://github.com/Cogito2012/CarCrashDataset.git
```

## Step 6: Run the Application

Once all dependencies are installed, you can run the application:

```bash
streamlit run app.py
```

The application should open in your default web browser at `http://localhost:8501`.

## Troubleshooting

### Dependency Conflicts

If you encounter dependency conflicts, try these approaches:

1. **Install dependencies one by one**: Install the most important packages first, then add others as needed.

2. **Create a clean environment**: If you're having persistent issues, create a fresh virtual environment:
   ```bash
   # Deactivate current environment
   deactivate
   
   # Remove the old environment
   rm -rf venv  # On macOS/Linux
   # OR
   rmdir /s /q venv  # On Windows
   
   # Create a new environment and start over
   python -m venv venv
   ```

3. **Update pip**: Sometimes an outdated pip can cause issues:
   ```bash
   pip install --upgrade pip
   ```

4. **Check Python version**: Ensure you're using Python 3.8 or higher:
   ```bash
   python --version
   ```

### Missing Modules

If you see errors about missing modules when running the application:

1. Ensure your virtual environment is activated
2. Install the specific missing module:
   ```bash
   pip install module_name
   ```

### Video Processing Issues

If you have issues with the video surveillance features:

1. Ensure OpenCV is properly installed:
   ```bash
   pip uninstall opencv-python
   pip install opencv-python-headless
   ```

2. Check that the video files exist in the correct location:
   ```bash
   mkdir -p src/data/videos
   ```

## Getting Help

If you continue to experience issues, please open an issue on the GitHub repository with details about the error and your environment.
