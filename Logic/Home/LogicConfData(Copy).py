from Logic.Home.LogicEventData import LogicEventData
from Logic.Home.LogicShopData import LogicShopData

class LogicConfData:

    def encode(self):
        print("[OHDDEBUG] -> LogicConfData")
        LogicShopData.encodeShopResources(self)
        self.writeVInt(500); self.writeVInt(50)
        self.writeVInt(999900); self.writeVInt(0)
        LogicEventData.encode(self)
        LogicShopData.encodeShopPacks(self)
        self.writeVInt(0); self.writeVInt(200)
        self.writeVInt(20); self.writeVInt(0)
        self.writeVInt(10); self.writeVInt(0)
        self.writeVInt(0); self.writeVInt(0)
        self.writeVInt(0); self.writeUInt8(1)
        self.writeVInt(2)
        for _ in range(2):
            self.writeDataReference(16,33); self.writeInt(99999); self.writeInt(0)
            self.writeDataReference(16,40); self.writeInt(99999); self.writeInt(0)
        self.writeVInt(1); self.writeInt(1)
        self.writeInt(41000000 + self.player.theme_id)
        self.writeVInt(0)
        print("[OHDDEBUG] <- LogicConfData")
