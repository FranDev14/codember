import os

class Message:
    def __init__(self):
        self.decoded_msg = ""
        self.queue = {}
        self.input_array = []
        self.txt_file = ""

    # Declare a method for add the words to a dict that works as a queue
    def _add_word(self, word):
        if word in self.queue:
            self.queue[word] += 1
        else:
            self.queue[word] = 1

    # Method for read a txt file and add to an list
    def _input_file(self):
        with open(self.txt_file, "r") as file:
            for chars in file.read().split(" "):
                self.input_array.append(chars)

    # Method for execute add word method for all the array
    def _array_word(self):
        for word in self.input_array: 
            self._add_word(word)

    def _get_messages(self):
        for key, value in self.queue.items():
            self.decoded_msg += key
            self.decoded_msg += str(value)
        return self.decoded_msg

    def _save_file(self, output_file):
        with open(output_file, "w") as file:
            file.write(self.decoded_msg)

    # Function for exetuce all the program
    def process_messages(self, txt_file):
        self.txt_file = txt_file
        
        self._input_file()
        self._array_word()
        
        self._get_messages()

        # Build one level folder to write the output file
        current_directory = os.path.dirname(os.path.realpath(__file__))
        output_file_path = os.path.join(current_directory, "..", "solutions", "challenge_01.txt")
        
        self._save_file(output_file_path)


if __name__ == "__main__":
    decoder = Message()
    
    decoder.process_messages("challenge_01\\message_01.txt")
