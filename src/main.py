from flask import Flask, request
from ariadne import gql, QueryType

app = Flask(__name__)

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