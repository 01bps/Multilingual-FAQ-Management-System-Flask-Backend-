from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class FAQ(db.Model):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)  # Default (English)
    answer = db.Column(db.Text, nullable=False)  # Rich text answer
    question_hi = db.Column(db.String(255))  # Hindi translation
    question_bn = db.Column(db.String(255))  # Bengali translation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_translated_question(self, lang="en"):
        """Return the translated question based on language input."""
        if lang == "hi" and self.question_hi:
            return self.question_hi
        elif lang == "bn" and self.question_bn:
            return self.question_bn
        return self.question  # Default to English

    def __repr__(self):
        return f"<FAQ {self.id}: {self.question[:30]}>"
        
