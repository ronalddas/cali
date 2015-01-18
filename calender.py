class calendar():
    def __init__(self):
        self.events={}

    def add_event(self,eventID,eventobject):
        self.events[eventID]=eventobject