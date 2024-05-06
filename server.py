import datetime
import logging.config

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for, logging as flog
from joblib import load100fcf2f7c8ba1ea333ec67cbaa93fbaaeea9cfe
from transformers import AutoModelForTokenClassification, pipeline
from transformers.pipelines import PIPELINE_REGISTRY

from pipeline import NER_Pipeline

# Truncate data frame at length 1000
pd.set_option('display.max_colwidth', 1000)

APP_LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'app_file': {  # Handler for app.log
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default',
        },
        'io_file': {  # Handler for IO.log
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'IO.log',
            'formatter': 'default',
        }
    },
    'loggers': {
        'app': {
            'handlers': ['app_file'],
            'level': 'INFO',  # Not strictly relevant in this scenario
            'propagate': False
        },
        'io': {
            'handlers': ['io_file'],
            'level': 'INFO',  # Not strictly relevant in this scenario
            'propagate': False
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['app_file']  # Initially, log to app.log
    }
}


# setup the flask app
app = Flask(__name__)
logging.config.dictConfig(APP_LOGGING_CONFIG)
app.logger.level = logging.INFO
app.logger.propagate = True
app.logger = logging.getLogger("app")


# Register custom pipeline
PIPELINE_REGISTRY.register_pipeline(
    "NER_NLP_tagger",
    pipeline_class=NER_Pipeline,
    pt_model=AutoModelForTokenClassification
)

# Load NER tagger pipeline
ner_tagger = pipeline(
    "NER_NLP_tagger", model="SurtMcGert/NLP-group-CW-roberta-ner-tagging")


def logIO(message):
    app.logger = logging.getLogger("io")
    app.logger.info(f"{message}")
    app.logger = logging.getLogger("app")


# Get predictions from pipeline
def requestResults(input):
    """
    function to get result from model
    inputs:
    - input - the text to pass to the model
    """
    output = ner_tagger(input)
    logIO(f"model-output: {output}")
    return output


# Home path
@ app.route('/')
def home():
    return render_template('index.html')

# Home path method handling


@ app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        # Retrieve user input
        input = request.form['user-input']


<< << << < HEAD
logIO(f"user-input: {input}")
== == == =
print(f"input: {input}")

app.logger.info(f"user-input: {input}")
# Return `success` rout with user input parameter
>> >>>> > 100fcf2f7c8ba1ea333ec67cbaa93fbaaeea9cfe
return redirect(url_for('success', input=input))

# `/success/<input>` route handling


@ app.route('/success/<input>')
def success(input):
    # Print results as HTML page
    return "<xmp>" + str(requestResults(input)) + " </xmp> "


if __name__ == '__main__':
    app.run(debug=True)
