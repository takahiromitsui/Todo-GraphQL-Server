from main import db
import uuid

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