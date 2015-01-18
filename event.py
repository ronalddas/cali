class event():
    def __init__(self, status, kind, end, created, icaluid, reminders, htmllink, sequence, updated, summary, start,
                 etag, location, attendees, organizer, creator, eventid):
        self.status = status
        self.kind = kind
        self.end = end
        self.created = created
        self.iCalUID = icaluid
        self.reminders = reminders
        self.htmlLink = htmllink
        self.sequence = sequence
        self.updated = updated
        self.summary = summary
        self.start = start
        self.etag = etag
        self.location = location
        self.attendees = attendees
        self.organizer = organizer
        self.creator = creator
        self.eventid = eventid

    def get_date(self):
        return self.start

    def get_name(self):
        return self.summary