import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from databaseActions import DbActions

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_actions = DbActions(app)

@app.route('/')
def index():
    events = db_actions.get_all()
    return render_template('index.html', events=events)


@app.route('/refresh-events')
def api_get_events():
    events = db_actions.get_all()

    # Converting event data to a list of dictionaries so can be returned as JSON
    events_data = []
    for event in events:
        events_data.append({
            'id': event.id,
            'source': event.source,
            'initiator_type': event.initiator_type,
            'status': event.status,
            'created_at': event.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'finished_at': event.finished_at.strftime('%Y-%m-%d %H:%M:%S') if event.finished_at else None,
        })

    return jsonify(events_data)