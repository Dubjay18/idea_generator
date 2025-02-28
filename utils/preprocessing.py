import os



class Preprocessing():
    """
    A class that handles the preprocessing of the raw user input
    depending on the workshop method selected
    return : json ?(str?)
    """
    #     workshop_method = data['workshop_method']



    def __init__(self, input_data:str):
        """
        Initializes the preprocessing class.
        :param intput_data: The directory of the data.
        :param output_data: The output data.
        """
        self.input_data:str = input_data
        self.output_data:str = None
    
    def process_hmw(self) -> str:
        """ 
        A Function that prepares usable question for GPT-3 
        for the "How might we..?" workshops
        """
         # raw input from the user interface for ex. "we, cook" > {subject},{problem}
         # output for GPT3 "How might {subjet} {problem} ?"
        

        problem = self.input_data
        if not problem:
            raise ValueError(" Please enter your text")
        if len(problem) <= 50:
            self.output_data = f"How might we {problem}?"
        else:
            raise ValueError("Too long! Only 50 characters allowed!")
                
        return self.output_data
        




    def process_opposite (self) -> str:
    
        """ 
        A Function that prepares usable question for GPT-3 
        for the "Opposite thinking" workshops
        """
         # raw input from the user interface for ex. " cook" > {problem}
         # output for GPT3 "What is the opposite of how {problem} should be ?"

        problem = self.input_data
        if not problem:
            raise ValueError(" Please enter your text")
        if len(problem) <= 50:
            self.output_data = f"What is the opposite of how {problem} should be ?"
        else:
            raise ValueError("Too long! Only 50 characters allowed!")
                
        return self.output_data

    def process_bad_idea(self) -> str:
    
        """ 
        A Function that prepares usable question for GPT-3 
        for the "Worst possible idea" workshops
        """
         # raw input from the user interface for ex. " cook" > {problem}
         # output for GPT3 "What is the worst possible idea about {problem} ?"
   
        problem = self.input_data
        if not problem:
            raise ValueError(" Please enter your text")
        if len(problem) <= 50:
            self.output_data = f"What is the worst possible idea about {problem} ?"
        else:
            raise ValueError("Too long! Only 50 characters allowed!")
                
        return self.output_data

    def process_free_text(self) -> str:
    
        """ 
        A Function to take a free text input 
        to generate ideas from GPT3 during a workshop
        """
        problem = self.input_data
        if not problem:
            raise ValueError(" Please enter your text")
        if len(problem) <= 50:
            self.output_data = problem
        else:
            raise ValueError("Too long! Only 50 characters allowed!")
                
        return self.output_data