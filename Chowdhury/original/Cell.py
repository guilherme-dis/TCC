
class Cell:
    def __init__(self, state):
        self.state = state
        self.dateLastUpdated = 0
        self.stateInNextIteration = state
        self.daysRecovered = 0
    
    def get_state_in_next_iteration(self):
        return self.stateInNextIteration
    
    def set_state_in_next_iteration(self, state):
        self.stateInNextIteration = state
    
    def get_date_last_updated(self):
        return self.dateLastUpdated
    
    def set_date_last_updated(self, date):
        self.dateLastUpdated = date

    def get_state(self):
        return self.state

    def get_position(self):
        return self.position
    
    def get_days_recovered(self):
        return self.daysRecovered
    
    def increment_days_recovered(self):
        self.daysRecovered += 1


    def set_state(self, state):
        self.state = state
        self.set_date_last_updated(1)



