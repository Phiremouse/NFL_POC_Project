"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import NFL_POC_Project.views
