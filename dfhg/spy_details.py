from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Ahuja', 'Mr.', 21, 4.5)

friend_one = Spy('Amit', 'Mr.', 25, 3.9)
friend_two = Spy('Swapnil', 'Ms.', 22, 4.3)
friend_three = Spy('Tia', 'Dr.', 27, 4.97)


friends = [friend_one, friend_two, friend_three]