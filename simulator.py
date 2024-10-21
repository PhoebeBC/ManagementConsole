import time
import os
import datetime
import random
from eventsTable import Event
from app import db_actions


class Simulator:
    def __init__(self):
        self.sources = ["Agents", "Messages", "Functional Layer", "API", "User Front End",
                                   "3rd Party Application"]
        self.initiator_types = ["User", "System"]

    def create_event(self, source=None, initiator_type=None):
        # If no argument provided use a random one form list above
        event_source = source or random.choice(self.sources)
        event_initiator_type = initiator_type or random.choice(self.initiator_types)
        created_at = datetime.datetime.now()
        event_status = "Active"
        finished_at = None

        event = Event(
            source=event_source,
            initiator_type=event_initiator_type,
            status=event_status,
            created_at=created_at,
            finished_at=finished_at
        )
        db_actions.add_event(event)

        return event

    def test(self):
        active_events: Event = []
        for num_events in range(0,200):
            rand_num = random.randint(0,10)
            print(f"sleep time {rand_num}")
            time.sleep(rand_num)

            if active_events and random.choice([True, False, False]):
                finish_event: Event = random.choice(active_events)
                print(f"finish event {finish_event}")
                db_actions.event_finished(finish_event)
                active_events.remove(finish_event)
            else:
                new_event = self.create_event()
                print(f"new event {new_event}")
                active_events.append(new_event)
