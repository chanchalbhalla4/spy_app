from spy_details import spy
STATUS_MESSAGES = ['My name is Gaurav, Gaurav Ahuja', 'Life is simple.','You get what you deserve in life.','I am busy']
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
friends_status=[]
def start_chat(spy_name,spy_age, spy_rating):
  show_menu = True
  while show_menu:
    menu_choices = "What do you want to do? \n1. Add a status update \n2. Add a friend \n3.Send secret  message \n4.Read a secret message \n5.Change profile photo  \n6.Go offline"
    menu_choice = raw_input(menu_choices)
    menu_choice = int(menu_choice)
    current_status_message = add_status(current_status_message)

def add_status(current_status_message):
    if current_status_message != None:
        print ("Your current status message is " + current_status_message + "\n")
    else:
        print ('You don\'t have any status message currently \n')
        default = raw_input("Do you want to update old status?")
    if default.upper() =='N':
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        elif default.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print item_position + "." + message
                item_position = item_position + 1
            message_selection = int(raw_input("\nChoose from the above messages "))
            if len(STATUS_MESSAGES) >= message_selection:
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
            else:
                print"The option you choose is not valid.Press enter y oe n."
            if updated_status_message:
                print"Your updated status message is: %s" %(updated_status_message)
            else:
                print"You did not update your status message."


    return updated_status_message


def add_friend():
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = raw_input("Age?")
    new_rating = raw_input("Spy rating?")

    new_age = int(new_age)
    new_rating = float(new_rating)
    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_status.append(True)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends_name)





print "Hello!"
print "Let's get started"
print "Continue as " + spy['salutation'] + " " + spy['name'] + "(yes/no)?"
existing = raw_input("Please tell")
if(existing=='no'):
    # raw_input is used to get input from the user
    # spy_name is a variable which will store the user input
    spy_name = raw_input("Welcome to spy chat,What is Your Name?")
    if len(spy_name) > 0:
        spy_rating = 0.0
        spy_is_online = False
        print'Welcome! ' + spy_name + '. Glad to have you back with us.'
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
        spy_name = spy_salutation + " " + spy_name
        print"Alright " + spy_name + " . I would like to know  little bit more about you before we proceed."
        spy_age = raw_input("What is your age?")
        print type(spy_age)
        spy_age = int(spy_age)
        print type(spy_age)
        if spy_age > 12 and spy_age < 50:
            spy_rating = raw_input('What is your spy rating?')
            spy_rating = float(spy_rating)
            spy_is_online = True
            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
                spy_rating) + " Proud to have you onboard"
            if spy_rating > 4.5:
                print 'Your rating is really high!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'Your rating is good!'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'Yor rating can be better than this!'
            else:
                print "You are not eligible"
        else:
            print"Your age is not valid to be a spy"
        start_chat(spy_name, spy_age, spy_rating)
    else:
        print"A spy need a valid name. Try again"


else:
    spy_is_online = True
    print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"
    start_chat(spy['name'], spy['age'], spy['rating'])
