
from steganography.steganography import Steganography
from termcolor import colored

from spy_details import spy, Spy, ChatMessage, friends

#list for collecting status messages sets by the user
STATUS_MESSAGES = ['My name is Gaurav, Gaurav Ahuja', 'Life is simple.','You get what you deserve in life.','I am busy']
#Simple print statements to greet the user!
special=['SOS','sos','HELP','help']
print colored("Hello!",'blue')
print colored("Welcome to your Spy App.",'blue')
#Ask u for are you an existing user
question = colored("Do you want to continue as ", 'blue') + spy.salutation + " " + spy.name + colored(" (Y/N)? ",'blue')
existing = raw_input(question)


#add_status fuction starts
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print ('Your current status message is %s \n' % (spy.current_status_message))
    else:
        print 'You don\'t have any status message currently '

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print ('The option you chose is not valid! Press either y or n ')

    if updated_status_message:
        print ('Your updated status message is: %s' % (updated_status_message))
    else:
        print ('You did not update your status message')

    return updated_status_message

#add_status function ends



#add_freind fuction starts

def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)

#add_freind fuction ends


#select_freind fuction starts
def select_friend():
  item_number = 0
  for friend in friends:

      print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                              friend.age,
                                                              friend.rating)
      item_number = item_number + 1

  friend_choice = raw_input("Choose from your friends")

  friend_choice_position = int(friend_choice) - 1

  return friend_choice_position


#select_freind fuction ends


#send_message function starts
def send_message():
  friend_choice = select_friend()

  original_image = raw_input("what is the name of your image")
  output_path = 'resources1.jpg'
  text = raw_input("What do you want to say?")
  Steganography.encode(original_image, output_path, text)
  temp = text.split(' ')
  for i in special:
      if i in temp:
          temp[temp.index(i)] = colored('Please Help me, i am in Danger', 'red')
  text = str.join('', temp)
  new_chat = ChatMessage(text, True)

  friends[friend_choice].chats.append(new_chat)

  print("Your secret message image is ready!")


  #send_message function ends




#read message function starts
def read_message():

      sender = select_friend()

      output_path = raw_input(colored("What is the name of the file?",'green'))
      secret_text = Steganography.decode(output_path)
      secret_text=str(secret_text)
      if secret_text=='None':
          print colored("No secret message is coded in the image!",'red')
      else:
          temp =secret_text.split(' ')
          for i in special:
              if i in temp:
                  temp[temp.index(i)] = colored('Please Help me, i am in Danger','red')
          secret_text=str.join('',temp)

      new_chat = ChatMessage(secret_text, False)

      friends[sender].chats.append(new_chat)
      print colored("Your secret message has been saved!",'green')
  #read message function ends


 #read_chat_history function starts
def read_chat_history():

    read_for = select_friend()

    print '\n'

    for chat in friends[read_for].chats:
        #set the color of time blue
        a = colored(chat.time.strftime('%d %B %Y'), 'blue')
        if chat.sent_by_me:

            print 'at', chat.time, "you said",chat.message
        else:
            print 'at', chat.time, "Friend read", chat.message
# read_chat_history function ends



#start_chat function starts
def start_chat(spy):

    current_status_message = None

    spy.name = spy.salutation + " " + spy.name
#condtion check age valid or not
    if spy.age > 12 and spy.age < 50:
        print colored("your age is valid!!",'green')
        if spy.rating > 4.5:
            print colored("Your rating is really high!",'green')
        elif spy.rating >= 3.5 and spy.rating <= 4.5:
            print colored('Your rating is good!','green')
        elif spy.rating >= 2.5 and spy.rating < 3.5:
            print colored('Yor rating can be better than this!','red')
        else:
             print colored("You are not eligible as per your rating",'red')
        print colored("Authentication complete. Welcome ",'green') + spy.name + colored(" age: ",'green') + str(spy.age) + colored(" and rating of: ",'green') + str(
            spy.rating) + colored(" Proud to have you onboard",'green')

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)
            #set menus
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print colored('Sorry you are not of the correct age to be a spy','red')

if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('', '', 0, 0.0)

    spy.name = raw_input(colored("Welcome to spy chat, you must tell me your spy name first: ",'blue'))

    if len(spy.name) > 0:
        spy.salutation = raw_input(colored("Should I call you Mr. or Ms.?: ",'blue'))

        spy.age = raw_input(colored("What is your age?",'blue'))
        spy.age = int(spy.age)

        spy.rating = raw_input(colored("What is your spy rating?",'blue'))
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print colored('Please add a valid spy name','red')



