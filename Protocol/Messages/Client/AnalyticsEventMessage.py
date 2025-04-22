from ByteStream.Reader import Reader

# Fix for AnalyticsEventMessage class
class AnalyticsEventMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Type = self.readString()
        self.Event = self.readString()

    def process(self, db=None):  # Modified to accept a db parameter
        print("[INFO] " + self.Type + " " + self.Event)
        # You can use db here if needed
