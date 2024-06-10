**RELEASE DATE**
App should be fully released by 15.5.2024.

**Description:**

This project is a web platform built with Django that allows users to share their projects, receive comments, and vote on each other's work.

**Current Status:**

The project is under active development. Daily updates are planned to bring it to a complete and functional state.

**Getting Started (For Now):**

***Clone the Repository:***  
- Get the latest code by cloning this repository.  

***Install Dependencies:***  
- Run pip install -r requirements.txt to install all necessary libraries. 
(on linux psycopg2 package may cause issues so you might want to remove it if installation is failing and install it manually `pip install --upgrade wheel` may help)  

***Note***  
- If you only wish to quickly test the project you should go into /devfolio/settiongs.py and uncomment DATABASES = {... sqlite3 ...} while comening DATABASES declaration for postgres below  


***Run the Project:***  
- If using sqlite database migate it by running `python manage.py makemigrations` and `python manage.py migrate`.    
- Start the development server with `python manage.py runserver` and access it at http://127.0.0.1:8000/ in your web browser.  

Guide.odt (Work in Progress): You can also download the included guide, which is a work in progress document outlining the website's functionalities.
Stay Tuned!

A comprehensive README with full setup and usage instructions will be available soon.

