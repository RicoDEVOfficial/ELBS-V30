import json

class LogicEventData:
    events = json.loads(open("JSON/events.json", 'r').read())

    def encode(self):
        print("[OHDDEBUG] -> LogicEventData")
        evs = LogicEventData.events
        # upcoming IDs
        self.writeVInt(len(evs))
        for i, ev in enumerate(evs):
            self.writeVInt(i+1)
        # full list
        self.writeVInt(len(evs))
        for i, ev in enumerate(evs):
            self.writeVInt(i+1); self.writeVInt(i+1)
            self.writeVInt(ev['Ended']); self.writeVInt(0); self.writeVInt(0)
            self.writeDataReference(15, ev['ID'])
            self.writeVInt(ev['Status'])
            self.writeString(""); self.writeVInt(0); self.writeVInt(0); self.writeVInt(0)
            self.writeBoolean(ev['Modifier'] > 0)
            if ev['Modifier'] > 0:
                self.writeVInt(ev['Modifier'])
            self.writeVInt(0); self.writeVInt(0)
        # history mirror
        self.writeVInt(len(evs))
        for i, ev in enumerate(evs):
            self.writeVInt(i+1); self.writeVInt(i+1)
            self.writeVInt(999999); self.writeVInt(0); self.writeVInt(0)
            self.writeDataReference(15, ev['ID'])
            self.writeVInt(ev['Status'])
            self.writeString(""); self.writeVInt(0); self.writeVInt(0); self.writeVInt(0)
            self.writeBoolean(ev['Modifier'] > 0)
            if ev['Modifier'] > 0:
                self.writeVInt(ev['Modifier'])
            self.writeVInt(0); self.writeVInt(0)
        print("[OHDDEBUG] <- LogicEventData")
