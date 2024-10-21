import os
import datetime
from eventsTable import Event, db

class DbActions:
    def __init__(self, app):
        self.db = db
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.db.init_app(app)
        self.create_database()

    def create_database(self):
        self.db.create_all()

    def add_event(self, event):
        self.db.session.add(event)
        self.db.session.commit()

    def get_all(self):
        return Event.query.all()

    def event_finished(self, event: Event):
        event.finished_at = datetime.datetime.now()
        event.status = "Complete"
        self.add_event(event)
        return event

    def delete_all(self):
        self.db.drop_all()
        self.create_database()
