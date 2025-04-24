import json
from datetime import datetime

class LogicShopData:

    shop_resources = json.loads(open('JSON/shop.json','r').read())
    gold_packs    = shop_resources['GoldPacks']
    boxes         = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']
    offers        = shop_resources['Offers']
    gold_cost     = [x['Cost'] for x in gold_packs]
    gold_amount   = [x['Amount'] for x in gold_packs]

    def encodeShopPacks(self):
        print("[OHDDEBUG] -> LogicShopPacks")
        self.writeArrayVint([20,35,75,140,290,480,800,1250])
        self.writeArrayVint([1,2,3,4,5,10,15,20])
        self.writeArrayVint([10,30,80]); self.writeArrayVint([6,20,60])
        self.writeArrayVint(LogicShopData.gold_cost)
        self.writeArrayVint(LogicShopData.gold_amount)
        print("[OHDDEBUG] <- LogicShopPacks")

    def encodeShopResources(self):
        print("[OHDDEBUG] -> LogicShopResources")
        ts = int(datetime.timestamp(datetime.now()))
        self.writeVInt(ts)
        LogicShopData.encodeBoxes(self)
        LogicShopData.encodeTokenDoubler(self)
        print("[OHDDEBUG] <- LogicShopResources")

    def encodeShopOffers(self):
        print("[OHDDEBUG] -> LogicShopOffers")
        self.writeVInt(len(LogicShopData.offers))
        for x in LogicShopData.offers:
            self.writeVInt(1); self.writeVInt(x['OfferID']); self.writeVInt(x['Multiplier'])
            self.writeDataReference(*x['DataReference']); self.writeVInt(0)
            self.writeVInt(x['ShopType']); self.writeVInt(x['Cost']); self.writeVInt(x['Timer'])
            self.writeVInt(1); self.writeVInt(100); self.writeUInt8(0)
            self.writeVInt(0); self.writeVInt(x['ShopDisplay']); self.writeUInt8(0)
            self.writeVInt(0); self.writeInt(0)
            txt = 'ОТКРЫТИЕ СЕРВЕРА! 🎉' if x['OfferText']=='amogus' else x['OfferText']
            self.writeStringReference(txt); self.writeUInt8(0)
            self.writeString("45000002"); self.writeVInt(0); self.writeUInt8(0)
            self.writeVInt(2); self.writeVInt(0)
        print("[OHDDEBUG] <- LogicShopOffers")

    def encodeBoxes(self):
        print("[OHDDEBUG] -> LogicBoxes")
        self.writeVInt(100); self.writeVInt(10)
        for b in LogicShopData.boxes:
            self.writeVInt(b['Cost']); self.writeVInt(b['Multiplier'])
        print("[OHDDEBUG] <- LogicBoxes")

    def encodeTokenDoubler(self):
        print("[OHDDEBUG] -> LogicTokenDoubler")
        td = LogicShopData.token_doubler[0]
        self.writeVInt(td['Cost']); self.writeVInt(td['Amount'])
        print("[OHDDEBUG] <- LogicTokenDoubler")
