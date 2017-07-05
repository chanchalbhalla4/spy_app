#Import datetime

from datetime import datetime

#Import termcolor

from termcolor import colored

#Import spy_details

from spy_details import spy, Spy, ChatMessage, friends

#Import steganography

from steganography.steganography import Steganography



#list for collecting status messages set by the user

STATUS = ['To heal the wound you need to stop touching it', 'Life is simple.','You get what you deserve in life.','I am busy']


URGENT=['SOS','sos','HELP','help','save','SAVE']

#statements to greet the user!

print colored("Hello!",'blue')

print colored("Welcome to your Spy App.",'blue')

QUESTION = colored("Do you want to continue as ", 'blue') + spy.salutation + " " + spy.name + colored(" (Y/N)? ",'blue')

ANSWER = raw_input(QUESTION)



def add_status(): #Add your status

    updated_status_message = None

    if spy.current_status_message != None:

        print colored('Your current status message is %s \n','green') % (spy.current_status_message)

    else:

        print colored('You don\'t have any status message currently \n','red')

    default = raw_input(colored("Do you want to select from the older status (y/n)? ",'yellow'))

    if default.upper() == "N":

        new_status_message = raw_input(colored("What status message do you want to set? ",'yellow'))


        if len(new_status_message) > 0:

            STATUS.append(new_status_message)

            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS:

            print '%d. %s' % (item_position,colored( message,'green'))

            item_position = item_position + 1

        message_selection = int(raw_input(colored("\nChoose from the above messages ",'yellow')))


        if len(STATUS) >= message_selection:

            updated_status_message = STATUS[message_selection - 1]

    else:
        print colored('The option you chose is not valid! Press either y or n.','red')

    if updated_status_message:

        print colored('Your updated status message is: %s','blue') % colored(updated_status_message,'green')

    else:

        print colored('You current don\'t have a status update','red')

    return updated_status_message





def add_friend():#Add new friends

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input(colored("Please tell your friend's name: ",'yellow'))

    new_friend.salutation = raw_input(colored("Are they Mr. or Ms.?: ",'yellow'))

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(colored("What is age of your friend?",'yellow'))

    new_friend.age = int(new_friend.age)


    new_friend.rating = raw_input(colored(" What is Spy rating?",'yellow'))

    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12:

        friends.append(new_friend)

        print colored('Friend Added!','green')

    else:

        print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided','red')

    return len(friends)



def select_a_friend():#Select friends

    item_no = 0

    for friend in friends:

        print colored(item_no+1,'blue'),colored(friend.salutation,'green'),colored(friend.name,'green'),colored(friend.age,'green'),colored("aged",'green'),colored("with rating",'green'),colored(friend.rating,'green')
        item_no = item_no + 1

    friend_choice = raw_input(colored("Select a friend of your choice", 'blue'))

    if friend_choice.isdigit():

        friend_choice_position = int(friend_choice) - 1

        return friend_choice_position
    else:
        print colored("wrong input",'red')

        return select_a_friend()




#function for send message

def send_message(): #Send message

    friend_choice = select_a_friend()

    original_image = raw_input(colored("What is the name of the image?",'yellow'))

    output_path = "1.jpg"

    text = raw_input(colored("What do you want to say? ",'yellow'))

    Steganography.encode(original_image, output_path, text) #Encoding image file

    temp = text.split(' ') #Spliting  message into words

    for i in URGENT:

        if i in temp:

            temp[temp.index(i)] = colored('Please Help me, i am in Danger', 'red')

    text = str.join('', temp)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print colored("Your secret message image is ready!",'green')



def read_message(): #Function for reading secret message

    sender = select_a_friend()

    output_path = raw_input(colored("What is the name of the file?",'yellow'))

    secret_text = Steganography.decode(output_path) #Decoding Text from file

    secret_text = str(secret_text)

    if secret_text == 'None':

        print colored("No secret msg is found", 'red')

    else:
        temp = secret_text.split(' ')
        if len(temp) > 100:

            del friends[sender]
            print colored("friend deleted due to text limit .",'red')
            return "pass"

        else:

            for i in URGENT:

                if i in temp:
                    temp[temp.index(i)] = colored('i m in danger', 'red')

            secret_text = str.join(' ', temp)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print colored("Your secret message has been saved!",'green')



def read_chat_history(): #Read chat history

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:

        a = colored(chat.time.strftime('%d %B %Y'), 'blue')

        if chat.sent_by_me:

            print 'at', chat.time, colored("you said : ",'blue'),colored(chat.message,'green')

        else:

            print 'at',chat.time,colored( "Friend read : ",'blue'), colored(chat.message,'green')



def start_chat(spy): #Start chat

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:

        print colored("Authentication complete. Welcome ", 'green') + spy.name + colored(" age: ", 'green') + str(
            spy.age) + colored(" and rating of: ", 'green') + str(
            spy.rating) + colored(" Proud to have you onboard", 'green')

        show_menu = True

        while show_menu:

            menu_choices = colored("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n", 'blue')

            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print colored("you have",'green'),colored(number_of_friends,'green'),colored('friends','green')

                elif menu_choice == 3:
                    send_message()

                elif menu_choice == 4:
                    temp = read_message()

                elif menu_choice == 5:
                    read_chat_history()

                else:
                    show_menu = False
    else:

        print colored('Sorry you are not of the correct age to be a spy','red')

if ANSWER.upper() == "Y":

    start_chat(spy)

else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input(colored("Welcome to spy chat, you must tell me your spy name first: ",'yellow'))

    if len(spy.name) > 0:

        spy.salutation = raw_input(colored("Should I call you Mr. or Ms.?: ",'yellow'))

        spy.age = raw_input(colored("What is your age?",'yellow'))

        spy.age = int(spy.age)

        spy.rating = raw_input(colored("What is your spy rating?",'yellow'))

        spy.rating = float(spy.rating)

        start_chat(spy)

    else:

        print colored('Please add a valid spy name','red')
