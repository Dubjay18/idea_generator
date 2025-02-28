import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests


class Generator():
    """
    A Class that generate idea for user based Gemini API.
    """
    def __init__(self, prepared_question:str, number_of_idea: int, workshop_method:str, crazy:bool = False) -> None:
        """
        A constructor function for Generator class.
        :param prepared_question: A question that user want to ask.
        :param number_of_idea: Number of idea that user want to get.
        :param crazy: A boolean value that indicate if user want to get an unusual suggestions or a more normal one.
        :param workshop_method: A string value that indicate which workshop method user want to use.
        """
        self.prepared_question:str = prepared_question
        self.number_of_idea:int = number_of_idea
        self.crazy:bool = crazy
        self.workshop_method:str = workshop_method
        self.raw_result:dict = None
        self.idea_list:list = []
        self.idea_list_enhaced:list = []
        self.api_key:str = None
        self.payload:dict = {}
        self.model = None

    def connect_gemini(self) -> bool:
        """
        A function that create api connection to Gemini from .env file.
        """
        try:
            load_dotenv()  # Load environment variables from .env
            self.api_key = os.getenv('GEMINI_API_KEY')
            if not self.api_key:
                raise ValueError("GEMINI_API_KEY not found in .env file")
            
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            
        except Exception as e:
            print(f"Error connecting to Gemini API: {e}")
            return False
        else:
            return True
        


    def generate_idea(self) -> bool:
        """
        A Function that generate idea for user based on Gemini API.
        :return: A boolean value that indicate if idea is generated or not.
        """
        if self.connect_gemini():
            """
            If api connection is created, then generate idea.
            """
            prompt = f"{self.prepared_question}. Generate {self.number_of_idea} ideas using {self.workshop_method} method."
            try:
                response = self.model.generate_content(prompt)
                self.raw_result = {"choices": [{"text": response.text}]}
                self.get_idea_list()
                return True
            except Exception as e:
                print(f"Error generating content: {e}")
                return False
        else:
            """
            If api connection is not created, then return false.
            """
            return False
    
    def get_idea_list(self) -> list:
        """
        A function that get idea list from raw result.
        :return: A list of idea.
        """
        if self.raw_result is not None:
            self.idea_list = [choice['text'] for choice in self.raw_result['choices']]
            self.idea_list_enhaced = [choice['text'] for choice in self.raw_result['choices']]
        else:
            return False
        return self.idea_list
