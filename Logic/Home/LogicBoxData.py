import random

class LogicBoxData:

    def randomize(self, box_type):
        print(f"[OHDDEBUG] -> LogicBoxData.randomize type={box_type}")
        rewards = []
        if box_type == 10:
            if random.randint(0,100) < 20:
                locked = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if locked:
                    b = random.choice(locked)
                    rewards.append({'Value':1,'DataRef':[16,b],'Amount':1})
                    self.player.brawlers_unlocked.append(b)
                    self.player.db.update_player_account(self.player.token,'UnlockedBrawlers',self.player.brawlers_unlocked)
            gold = random.randint(20,100)
            rewards.append({'Value':7,'DataRef':[0,0],'Amount':gold})
            self.player.resources[1]['Amount'] += gold
            self.player.db.update_player_account(self.player.token,'Resources',self.player.resources)
            pp = random.randint(5,30)
            b2 = random.choice(self.player.brawlers_unlocked)
            rewards.append({'Value':6,'DataRef':[16,b2],'Amount':pp})
            self.player.brawlers_powerpoints[str(b2)] += pp
            self.player.db.update_player_account(self.player.token,'BrawlersPowerPoints',self.player.brawlers_powerpoints)
        print(f"[OHDDEBUG] <- LogicBoxData.randomize returned {len(rewards)} items")
        return rewards

    def encode(self, box_type):
        print(f"[OHDDEBUG] -> LogicBoxData.encode type={box_type}")
        r = self.randomize(box_type)
        self.writeVInt(len(r))
        for it in r:
            self.writeVInt(it['Value'])
            self.writeDataReference(it['DataRef'][0], it['DataRef'][1])
            self.writeVInt(it['Amount'])
        print("[OHDDEBUG] <- LogicBoxData.encode")
