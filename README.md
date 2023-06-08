# Todo GraphQL Server

This is a simple Todo GraphQL server implemented using Flask, Ariadne, and flask-migrate. The server allows you to manage a collection of Todo items through a GraphQL API.

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Change into the project directory: `cd <project-directory>`
3. Install Poetry (if not already installed): [Poetry Installation](https://python-poetry.org/docs/#installation)
4. Install the project dependencies: `poetry install`

## Usage

### Running the Server

To run the Todo GraphQL server, execute the following command:

```
cd src
export FLASK_APP=main.py
poetry run flask run
```

The server will start running at `http://localhost:5000`.

### GraphQL Endpoint

You can interact with the GraphQL API using the following endpoint:

```
POST /graphql
```

To use the GraphQL Explorer, you can access the following endpoint in your browser:

```
GET /graphql
```

## Schema

The GraphQL schema used by the server is defined in the `schema.graphql` file. It contains the following types and operations:

### Types

- `Todo`: Represents a Todo item with properties such as `id`, `title`, `completed`, `created_at`, and `updated_at`.

### Queries

- `todos`: Retrieves a list of all Todo items.
- `todo`: Retrieves a single Todo item by its `id`.

### Mutations

- `createTodo`: Creates a new Todo item with the specified `title`.
- `updateTodoCompleted`: Toggles the `completed` status of a Todo item identified by its `id`.
- `deleteTodo`: Deletes a Todo item identified by its `id`.

## Database

The server uses a Postgres database to store the Todo items. The database is automatically created and managed using Flask-Migrate.
To set up your database connection, duplicate .env.example as .env and pass your database url.

## Example Usage

Here are some example queries and mutations that can be performed on the server:

```graphql
# Get all Todo items
query {
  todos {
    id
    title
    completed
    created_at
    updated_at
  }
}

# Get a Todo item by ID
query {
  todo(id: "todo-id") {
    id
    title
    completed
    created_at
    updated_at
  }
}

# Create a new Todo item
mutation {
  createTodo(title: "Buy groceries") {
    success
    todo {
      id
      title
      completed
      created_at
      updated_at
    }
  }
}

# Update the completed status of a Todo item
mutation {
  updateTodoCompleted(id: "todo-id") {
    success
    todo {
      id
      title
      completed
      created_at
      updated_at
    }
  }
}

# Delete a Todo item
mutation {
  deleteTodo(id: "todo-id") {
    success
    todo {
      id
      title
      completed
      created_at
      updated_at
    }
  }
}
```