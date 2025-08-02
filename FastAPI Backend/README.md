# FASTAPI Backend

<p align="center">
  <a href="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" 
target="blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="200" alt="FastAPI Logo" /></a>
</p>


### Clone the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone
```

Set Up a Virtual Environment
Create and activate a virtual environment to manage your dependencies:

On macOS/Linux
```bash
python -m venv venv
source venv/bin/activate    
```

On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Install the Required Libraries

The requirements.txt file contains all the necessary libraries for the project. Install them using the following command:

```bash
pip install -r requirements.txt
```

Update the requirements.txt file with the following command:

```bash
pip freeze > requirements.txt
```


### Run the Backend Application
Development Environment

To run the application in a development environment, use the following command:
    
```bash
uvicorn app.main:app --reload
```

To force stop all the python processes, use the following command:

```bash
pkill -f python
taskkill /IM "python.exe" /F
```

### Production Environment

To run the application in a production environment, use the following command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Add Library to requirements.txt
To add a new library to the requirements.txt file, you can use the following command:

```bash
pip freeze | grep <library_name> >> requirements.txt
```

**NOTE:** The script **_run.sh_** and **_stop.sh_** can be used to start and stop the application respectively.
