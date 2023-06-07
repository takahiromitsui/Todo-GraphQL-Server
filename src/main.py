from flask import Flask, request
from ariadne import gql, QueryType
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()




@app.route("/", methods=['GET'])
def hello():
    return 'Hello, Wold!'

@app.route("/graphql", methods=['POST'])
def graphql():
    return 'Hello, World!'