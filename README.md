# FileTransfer

![Alt Text](https://github.com/nachiketgalande1609/FileTransfer/blob/main/screenshots/app.png)

## Steps to Run the Code

1. **Create Virtual Environment:**
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

2. **Install Dependencies:**
   - Make sure you are in the project directory and your virtual environment is activated.
   - Install the required packages from the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application:**
   - Run the Flask application using the following command:
     ```bash
     python app.py
     ```

4. **Upload Files:**
   - Open a web browser and go to [http://localhost:5000](http://localhost:5000) (or the specified IP address).
   - Use the provided file upload form to upload files.

5. **Check Uploaded Files:**
   - The uploaded files will be stored in the `/downloads` folder within the project directory.

6. **Shutdown the Application:**
   - To stop the application, go back to the terminal or command prompt where the Flask app is running and press `Ctrl + C` to interrupt the process.
   - Optionally, deactivate the virtual environment:
     ```bash
     deactivate
     ```
