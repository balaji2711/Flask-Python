# Flask-Python
A short &amp; simple flask example to get started with. 😎


The commands below set everything up to run the examples:

1. Install Python 3.10.4.
2. Clone the project using git clone https://github.com/balaji2711/Flask-Python.git.
3. Open the project folder in VS code
4. Install Flask & Flask Swagger UI using pip install flask & pip install flask_swagger_ui

You can use an extension in Visual Studio Code to run and test your Flask application with Swagger. Here's one way to do it:

Install the Swagger Viewer extension in Visual Studio Code.

In this example, we're using the get_swaggerui_blueprint() function from the flask_swagger_ui library to create a Swagger UI blueprint that will be added to our Flask app. The SWAGGER_URL variable specifies the URL where the Swagger UI will be served, and the API_URL variable specifies the path to the Swagger specification file.

Add your Swagger specification file to your Flask app's static directory. In this example, we're assuming that the specification file is named swagger.yaml and is located in the static directory.

Run your mock_service.py from within Visual Studio Code.

Open a web browser and navigate to http://your_ip_address:5000/swagger. This should open the Swagger UI page for your Flask app.

You should now be able to view and interact with your API in the Swagger UI interface.

![image](https://user-images.githubusercontent.com/15344129/224388754-e81bb5a9-24ed-4be2-af87-5fa9df62a429.png)
