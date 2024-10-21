from app import db_actions
from simulator import Simulator

def test():
    db_actions.delete_all()
    simulator = Simulator()
    simulator.test()

test()
