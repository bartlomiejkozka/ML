# Gift ideas generator (using LLM)

## Prerequisites

1. **Python Installation**  
   This project requires Python to run. If Python is not installed on your system, follow these instructions to download and install it:
   - **Windows**: [Download Python Installer](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe) and follow the setup instructions.
   - **macOS**: Visit [Python for macOS](https://www.python.org/downloads/macos/) and download the installer.
   - **Linux**: Use your package manager, e.g., `sudo apt install python3` for Ubuntu.

   > **Note**: To verify if Python is installed, open a terminal or command prompt and run:
   > ```bash
   > python --version
   > ```
   > If Python is installed, you should see a version number.

## Installation

1. **Download the Repository Files**  
   - Clone this repository using Git:
     ```bash
     git clone https://github.com/bartlomiejkozka/ML.git
     cd ML/gift-ideas-generator
     ````
   - Alternatively, download the ZIP file from GitHub and extract it.

2. **Set Up Libraries**
   - Run this cmd to install the required libraries:
     ```bash
     python -m pip install -r requirements.txt
     ```

3. **Get your Gemini AI API_KEY**
    - Create in project folder .env file
    - Visit https://aistudio.google.com/apikey
    and click "Create API key",
    then copy the API key to .env file like:
    GEMINI_API_KEY=<your_api_key>

## Running the Application

1. **Start the Application**  
   Run the gui script to start the frontend application:
   ```bash
   python gui.py
   ```

## Using a Virtual Environment (Optional)
Visit the website if you are interested in:
[Using a Virtual Environment (Optional)](https://realpython.com/python-virtual-environments-a-primer/)
   
