# Neuroflow-
This project is a web REST API application with a '/mood' endpoint, which when POSTed to persists the submitted mood value.
Users have the ability to login their credentials in  other to proceed.These credentials are the Username and a login which opens before you 
start using this web app.
The code used for this project was written in Python and HTML for the webpage.

HOW TO RUN THE CODES 

REQUIREMENTS FOR THE PYTHON CODE


In order to use this python code I have provided for this projects, you'll need to install some python modules.
These modules are:

1.Flask==1.1.1


2.flask-restful==0.3.8


3.requests==2.21.0


4.oauthlib==3.0.1


5.pyOpenSSL==19.0.0


6.Flask_Login==0.4.1


7.flask.ext.pymongo


HOW TO INSTALL THE MODULES.

The following command will install the latest version of a module and its dependencies from the Python Packaging Index:

python -m pip install SomePackage


It’s also possible to specify an exact or minimum version directly on the command line. When using comparator operators such as >, < or some other special character which get interpreted by shell, the package name and the version should be enclosed within double quotes:

python -m pip install SomePackage==1.0.4    # specific version
python -m pip install "SomePackage>=1.0.4"  # minimum version
Normally, if a suitable module is already installed, attempting to install it again will have no effect. Upgrading existing modules must be requested explicitly:

python -m pip install --upgrade SomePackage
More information and resources regarding pip and its capabilities can be found in the Python Packaging User Guide.

Creation of virtual environments is done through the venv module. Installing packages into an active virtual environment uses the commands shown above.



NB: For the HTML codes provided in this project,add an HTML extension when saving it in order for it to run.
