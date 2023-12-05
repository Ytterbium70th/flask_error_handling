from flask import Flask
import logging
app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Intentional error
        3578 / 0
        return "Welcome to the Home Page!"
    except Exception as e:
        app.logger.error('Error occurred: %s', e)
        return "An error occurred", 500

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500

logging.basicConfig(filename='error.log', level=logging.DEBUG)

#here's the error:
#12.43 / 0

