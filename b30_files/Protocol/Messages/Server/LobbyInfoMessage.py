from ByteStream.Writer import Writer

class LobbyInfoMessage(Writer):

    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        self.writeVInt(self.count)
        self.writeString("Brawl Stars \n Version 30.242 \n Base made by BreadDEV \n Database Improvements by RicoDEV \n \n Database was rewritten in TinyDB, Bytestream & core adjusted to work with TinyDB \n \n Made with <3 by: \n \n Classic Brawl Team \n BreadDEV \n RicoDEV")

        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
