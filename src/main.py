from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import os
from ariadne import graphql_sync, make_executable_schema, ObjectType, snake_case_fallback_resolvers, gql, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    title = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

def resolve_todos(obj, info):
    try:
        todos = [todo.to_dict() for todo in Todo.query.all()]
        payload = {
            "success": True,
            "todos": todos
        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload

query = ObjectType("Query")
query.set_field("todos", resolve_todos)

type_defs = gql(load_schema_from_path("schema.graphql"))
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)

@app.route("/", methods=['GET'])
def hello():
    return 'Hello, World!'

explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run()
