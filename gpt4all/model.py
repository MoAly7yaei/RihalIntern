import os
from gpt4all import GPT4All

class Model:
    def __init__(self):
        self.model_name = 'orca-mini-3b-gguf2-q4_0.gguf'
        try:
            self.model_path = os.getcwd() + "/models"
        except:
            os.makedir(os.getcwd() + "/models")
        self.n_ctx = 4096
        self.model = GPT4All(self.model_name, self.model_path, n_ctx=self.n_ctx)
        self.temp = 0.8
        self.n_batch = 16
        self.output_list = []

    def generate(self, input):
        input = str(input)
        output = self.model.generate(input, max_tokens=100000, temp=self.temp, n_batch=self.n_batch)
        return output
    
    def build_context(output_list):
        if output_list:
            context = 'By knowing all the following statements:\n'
            context += '\n'.join(output_list) + '\n'
            context += 'the conclusion is:\n'
            return str(context)
        else:
            return 'You are an assistance that you are able to help of prompt that is been given to you and you will going to find the words that is suitable for the following prompts. Please Help me in the following\n'

    def chat(self, input):
        self.output_list.append(str(input))
        if len(self.output_list) >= 1000000:
            self.output_list = []
            return "You have exceeded the session length limitation."
        else:
            context = Model.build_context(self.output_list)
            prompt = context + "\n" + "\nAccording to whas is been mentioned:\n" + input
            output = Model.generate(self, str(prompt))
            self.output_list.append(output)
            if output == None:
                output = self.output_list[-1] #For debuging porpose
            return output



        


