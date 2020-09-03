# EverPost

# THIS REPOSITORY IS CURRENTLY IN DEVELOPMENT, MOST FEATURES MIGHT NOT WORK AS AN ISSUE HAS ENTERED THE MASTER BRANCH.

![A laptop](https://cdn.pixabay.com/photo/2016/11/19/15/32/business-1839876_960_720.jpg)

A blog post app similar to Twitter where users can register, log in, create posts, read posts, 
like posts, edit their posts, delete their posts, change the font and font color of their posts,
have an admin validate their posts, change their profile picture and request a password reset email
which will be sent to their registered Gmail account.

Please consider starring the repository if you liked it.

## How to clone repository

If you want to clone the repository and try it 
out on your own computer, follow the steps 
mentioned below. All the features of the app mentioned 
above will work except for the password reset email feature, which
will not work now due to security reasons. I will be editing this readme to 
also have instructions on how to enable the reset password feature as well.

If you find an issue with the application - mention it [here](https://github.com/Whitespace404/EverPost/issues/new)

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

 * Serving Flask app "flaskblog" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
```
