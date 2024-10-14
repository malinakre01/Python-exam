# Question 3

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message_body = []
    
    def get_sender(self):
        return self.sender
    
    def get_recipient(self):
        return self.recipient
    
    def append(self, line):
        self.message_body.append(line)
        
# The "--str--" method formats the message reader-friendly when printing an instance of the class
    def __str__(self):
        message_str = f"From: {self.sender}\nTo: {self.recipient}\n"
        message_str += "\n".join(self.message_body)
        return message_str

if __name__ == "__main__":

    email_message = Message("Kim", "Alex")

    email_message.append("Hi Alex,")
    email_message.append("I hope you are doing well!")
    email_message.append("Hugs from:")
    email_message.append("Kim")

    print(email_message)
    