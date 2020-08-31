# A Blog Post App
## How to clone repository

If you want to clone the repository and try it 
out on your own computer, follow the steps 
mentioned below.

## Mac OS 
The installation proccess for Mac is 
mentioned below.

### Prerequisites

#### 1) Python 3.6+
Download from [here](https://www.python.org/)

Macs already come with **Python2**. This version of Python is not supported by this application.
You will have to download a version of Python that is higher than __Python 3.6__. 

If you want to check which version of Python you have, simply type in:

```bash
python3 --version
python --version
```

```bash
git clone https://github.com/Whitespace404/Blog_Post_App.git
cd Blog_Post_App
pip3 install flask -q
pip3 install flask_sqlalchemy -q
pip3 install flask_bcrypt -q
pip3 install flask_login -q
pip3 install flask_mail -q
pip3 install flask-wtf -q
pip3 install wtforms[email] -q
pip3 install pillow -q
pip3 install email-validator==1.1.1 -q
python3 run.py
```

Once you have ran all the above commands,
 you can open a web browser and visit
  localhost:5000 to view it. 
  
  If you followed all the steps above correctly,
  you should see something similar to this in your Terminal 
  window after you have executed the last command:
  
  ```bash
python3 run.py

    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py:833: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Serving Flask app "flaskblog" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
```


---
## Windows
The installation for Windows is a little
bit different from the process that Mac users might follow
but that is explained here as well.
### Prerequisites

#### 1) GitBash Terminal.
Download from [here](https://git-scm.com/downloads).
We will be using Git to clone the repository 
from GitHub. If you know how to download a Zip file
of this repository, then you are welcome to do so that way.

#### 2) Python 3.6+
Download from [here](https://www.python.org/).
If you think you already have a version of Python and don't know which version of Python it is, simply execute the following command:
```bash
python --version
```

---

Once you have downloaded and installed the prerequisites, run the following commands from GitBash Terminal:

```
git clone https://github.com/Whitespace404/Blog_Post_App.git
cd Blog_Post_App
pip install flask -q
pip install flask_sqlalchemy -q
pip install flask_bcrypt -q
pip install flask_login -q
pip install flask_mail -q
pip install flask-wtf -q
pip install wtforms[email] -q
pip install pillow -q
pip install email-validator==1.1.1 -q
python run.py
```

Once you have ran all the above commands,
 you can open a web browser and visit
  localhost:5000 to view it. 
  
  If you followed all the steps above correctly,
  you should something similar this in your terminal 
  window after you have executed the last command:
  
  ```
python run.py

    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py:833: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Serving Flask app "flaskblog" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
```
