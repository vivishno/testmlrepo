# Pull a pre-built alpine docker image with nginx and python3 installed
FROM python:3

ADD app.py / 
ADD sklearn_regression_model.pkl / 
ADD requirements.txt / 

# Set the folder where uwsgi looks for the app
WORKDIR /

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000 

# Run the flask server for the endpoints 
CMD python app.py
