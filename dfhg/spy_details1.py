from datetime import datetime
#forming the class spy
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


#forming the class chatMessage
from termcolor import colored
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('simran', 'Ms.', 18, 4.0)

friend_one = Spy('Sakshi', 'Ms.', 19, 4.2)
friend_two = Spy('Sabha', 'Ms.', 19, 4.3)
friend_three = Spy('Aryan', 'Dr.', 20,4.0 )


friends = [friend_one, friend_two, friend_three]