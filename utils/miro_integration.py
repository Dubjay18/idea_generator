import requests
import random
import os


class MiroIntegrator():
    """
    A Class that handles the Miro API integration operations.
    """

    def __init__(self) -> None:
        """
        A Constructor for the MiroIntegrator class.
        """
        self.api_key:str = None
        self.board_id:str = None
        self.url:str = f'https://api.miro.com/v1/boards/{self.board_id}/widgets/'
        self.headers:dict = None
        self.payload:dict = None
    
    def create_connection(self, api_key:str, board_id:str) -> bool:
        """
        """
        pass

    def create_sticker(self, text:str) -> bool:
        """
        A Function to create a sticker on Miro board
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.payload)
        except:
            return False
        else:
            return True
