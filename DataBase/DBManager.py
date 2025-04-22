# Database rewrite in tinydb

import sys
import datetime
import json
import os
from tinydb import TinyDB, Query, where
from tinydb.operations import set as tinydb_set
from Logic.Player import Player
from Utils.Helpers import Helpers


class DBManager:
    def __init__(self, conn_str=None):
        self.player = Player
        # Try to get database path from config.json
        db_path = self.get_db_path_from_config()
        
        # If conn_str is provided and valid, use that instead
        if isinstance(conn_str, str) and conn_str.lower().endswith('.json'):
            db_path = conn_str
            
        # Ensure directory exists
        self.ensure_directory_exists(db_path)
            
        try:
            self.database = TinyDB(db_path)
            # Create tables equivalent to MongoDB collections
            self.players = self.database.table('Players')
            self.clubs = self.database.table('Clubs')
        except Exception as e:
            print(f"{Helpers.red}[ERROR] Unable to initialize TinyDB: {str(e)}")
            # Fallback: ensure database is initialized
            fallback_path = 'DataBase/Data/GameData.json'
            self.ensure_directory_exists(fallback_path)
            self.database = TinyDB(fallback_path)
            self.players = self.database.table('Players')
            self.clubs = self.database.table('Clubs')

        # Keep the MongoUtils reference as an attribute for compatibility
        self.mongo_utils = self

        # Default player data template
        self.data = {
            'Name': 'Guest',
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': 0,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins': Player.unlocked_skins,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'ClubID': 0,
            'ClubRole': 0
        }

        # Default club data template
        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': [],
            'Inbox': []
        }

    def get_db_path_from_config(self):
        """Fetch database path from config.json if it exists"""
        default_path = 'DataBase/Data/GameData.json'
        
        try:
            # Try to load config.json
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
                
            # Check if DatabasePath exists in config
            if 'DatabasePath' in config:
                return config['DatabasePath']
            else:
                print(f"{Helpers.yellow}[WARNING] DatabasePath not found in config.json, using default path")
                return default_path
                
        except FileNotFoundError:
            print(f"{Helpers.yellow}[WARNING] config.json not found, using default database path")
            return default_path
        except json.JSONDecodeError:
            print(f"{Helpers.yellow}[WARNING] Invalid JSON in config.json, using default database path")
            return default_path
        except Exception as e:
            print(f"{Helpers.yellow}[WARNING] Error reading config.json: {str(e)}, using default database path")
            return default_path
    
    def ensure_directory_exists(self, file_path):
        """Ensure the directory for the database file exists"""
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"{Helpers.green}[INFO] Created directory: {directory}")
            except Exception as e:
                print(f"{Helpers.yellow}[WARNING] Could not create directory {directory}: {str(e)}")

    def merge(self, dict1, dict2):
        dict1.update(dict2)
        return dict1

    def insert_data(self, table, data):
        table.insert(data)

    def load_document(self, table, query_dict):
        User = Query()
        query_conditions = None
        for key, value in query_dict.items():
            cond = (User[key] == value)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        return table.get(query_conditions) if query_conditions else None

    def update_document(self, table, query_dict, item, value):
        User = Query()
        query_conditions = None
        for key, val in query_dict.items():
            cond = (User[key] == val)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        if query_conditions:
            table.update(tinydb_set(item, value), query_conditions)

    def update_all_documents(self, table, query_dict, item, value):
        User = Query()
        query_conditions = None
        for key, val in query_dict.items():
            cond = (User[key] == val)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        if query_conditions:
            table.update(tinydb_set(item, value), query_conditions)
        else:
            table.update(tinydb_set(item, value))

    def delete_document(self, table, query_dict):
        User = Query()
        query_conditions = None
        for key, val in query_dict.items():
            cond = (User[key] == val)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        if query_conditions:
            table.remove(query_conditions)

    def delete_all_documents(self, table, query_dict=None):
        if not query_dict:
            table.truncate()
            return
        User = Query()
        query_conditions = None
        for key, val in query_dict.items():
            cond = (User[key] == val)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        if query_conditions:
            table.remove(query_conditions)

    def load_all_documents(self, table, query_dict=None):
        if not query_dict:
            return table.all()
        User = Query()
        query_conditions = None
        for key, val in query_dict.items():
            cond = (User[key] == val)
            query_conditions = cond if query_conditions is None else query_conditions & cond
        return table.search(query_conditions)

    def load_all_documents_sorted(self, table, query_dict, sort_key):
        results = self.load_all_documents(table, query_dict)
        return sorted(results, key=lambda x: x.get(sort_key, 0), reverse=True)

    # Player methods
    def create_player_account(self, id, token):
        auth = {'ID': id, 'Token': token}
        auth.update(self.data)
        self.insert_data(self.players, auth)

    def load_player_account(self, id=None, token=None):
        query = {'Token': token} if token else {'ID': id}
        result = self.load_document(self.players, query)
        if result:
            for field, default in self.data.items():
                if field not in result:
                    self.update_player_account_by_id(result['ID'], field, default)
            return self.load_document(self.players, query)

    def load_player_account_by_id(self, id):
        return self.load_document(self.players, {'ID': id})

    def update_player_account(self, token, item, value):
        self.update_document(self.players, {'Token': token}, item, value)

    def update_player_account_by_id(self, id, item, value):
        self.update_document(self.players, {'ID': id}, item, value)

    def update_all_players(self, query, item, value):
        self.update_all_documents(self.players, query, item, value)

    def delete_all_players(self, args=None):
        self.delete_all_documents(self.players, args)

    def delete_player(self, token):
        self.delete_document(self.players, {'Token': token})

    def load_all_players(self, args=None):
        return self.load_all_documents(self.players, args)

    def load_all_players_sorted(self, args, element):
        return self.load_all_documents_sorted(self.players, args, element)

    # Club methods
    def create_club(self, id, data):
        auth = {'ID': id}
        auth.update(data)
        self.insert_data(self.clubs, auth)

    def update_club(self, id, item, value):
        self.update_document(self.clubs, {'ID': id}, item, value)

    def load_club(self, id):
        result = self.load_document(self.clubs, {'ID': id})
        if result:
            for field, default in self.club_data.items():
                if field not in result:
                    self.update_club(id, field, default)
            return self.load_document(self.clubs, {'ID': id})

    def load_all_clubs_sorted(self, args, element):
        return self.load_all_documents_sorted(self.clubs, args, element)

    def load_all_clubs(self, args=None):
        return self.load_all_documents(self.clubs, args)

    def delete_club(self, id):
        self.delete_document(self.clubs, {'ID': id})
