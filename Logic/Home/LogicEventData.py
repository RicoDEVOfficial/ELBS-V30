import json

class LogicEventData:
    events = json.loads(open("JSON/events.json", 'r').read())

    def encode(self):
        events = json.loads(open("JSON/events.json", 'r').read())

        self.writeVInt(len(events) + 1)
        for i in range(len(events) + 1):
            self.writeVInt(i)

        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(event['Ended'])
            self.writeVInt(0)  # Timer

            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])

            self.writeVInt(event['Status'])

            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)
            
        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(999999)
            self.writeVInt(0)  # Timer

            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])

            self.writeVInt(event['Status'])

            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)