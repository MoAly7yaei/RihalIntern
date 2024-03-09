import os
from gpt4all import GPT4All

class Model:
    def __init__(self):
        self.model_name = 'wizardlm-13b-v1.2.Q4_0.gguf'
        try:
            self.model_path = os.getcwd() + "/models"
        except:
            os.makedirs(os.getcwd() + "/models")
        self.n_ctx = 2048
        self.model = GPT4All(self.model_name, self.model_path, n_ctx=self.n_ctx)
        self.temp = 0.7
        self.n_batch = 128
        self.output_list = ['I am an assistance that I am able to looking for Informations of prompt that is been given to me and I will going to find the words that is suitable for the following prompts, I will provide answer without asking questions and I will provide answers always. I will Help you in the following prompt:']
        self.context = ''
        self.input_list = []

    def generate(self, input):
        input = str(input)
        output = self.model.generate(input, max_tokens=1000, temp=self.temp, n_batch=self.n_batch)
        return output
    
    @staticmethod
    def build_context(self, output_list):
    
        self.context += "bassed on the inputs givin as following: \n"
        self.context += '\n'.join(output_list) + '\n'
        self.context += 'By knowing all the following answers:\n'
        self.context += '\n'.join(output_list) + '\n'
        self.context += 'my answer is '
        return str(self.context)
    

    def chat(self, input):
        self.input_list.append(str(input))
        if len(self.output_list) >= 1000000:
            self.output_list = []
            return "You have exceeded the session length limitation."
        
        elif input.strip() == "":
            return "You cannot send an empty prompt"
        
        elif input == "$":
            return self.output_list + self.input_list

        else:
            ctx = Model.build_context(self, output_list=self.output_list)
            prompt = ctx + "\n" + "\nAccording to what has been mentioned above I will answer the following question: " + input
            output = Model.generate(self, str(prompt))
            self.output_list.append(output)
            return self.output_list[-1]
        

class NoChatSessionModel:
    def __init__(self):
        self.model_name = 'orca-mini-3b-gguf2-q4_0'
        try:
            self.model_path = os.getcwd() + "/models"
        except:
            os.makedirs(os.getcwd() + "/models")
        self.n_ctx = 2048
        self.model = GPT4All(self.model_name, self.model_path, n_ctx=self.n_ctx)
        self.temp = 0.7
        self.n_batch = 8
        self.output_list = ['I am an assistance that I am able to looking for Informations of prompt that is been given to me and I will going to find the words that is suitable for the following prompts, I will provide answer without asking questions and I will provide answers always. I will Help you in the following prompt:']
        self.input_list = []
        self.context = ''

    def generate(self, input):
        input = str(input)
        output = self.model.generate(input, max_tokens=1000, temp=self.temp, n_batch=self.n_batch)
        return output
        



        


