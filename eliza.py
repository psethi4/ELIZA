"""INTRODUCTION
1)In this program ELIZA a psychotherapist is created. ELIZA engages the user in a 
conversation using regular expressions and techniques like word spotting and sentence transformations.
2)The program works as follows:
ELIZA: Hi, I'm Eliza, a psychotherapist. What is your name?
USER: My Name is MAC

Usage instructions:
a) The user should tell ELIZA its name in the beginning as that name will be used later in the program for personalization.
b) ELIZA will response correctly only for hardcoded statements and for all other non-coded statements it
will give below message which adds robustness to the program.

I am not sure I understand you fully !!! Let's focus a bit... Tell me about your family.
c) To quit the chat user should input "bye"

3)The code is the set of if-elif statements which are used for word spotting and sentence transformation
a) A if or elif function first searches for a regex and replaces it with a question or transformation to continue the dialogue.
b) If the pattern does not match any of the search statements then the default else statement is printed o the screen which is:
I am not sure I understand you fully !!! Let's focus a bit... Tell me about your family.
c) If the user tells bye then below ELIZA quits:

Additional Functionality
a) We have removed case sensitivity from the program, so if the
user inputs in any case{A-z} ELIZA should be able to handle it without any problem.
b) Also included personalization by storing the username in a variable and then calling that variable wherever required.
"""

import re
from nltk.tokenize import word_tokenize

def main():
    print("=====================================================================")
    print("         EEEEEEE   L       IIIIIII  ZZZZZZZ        A")
    print("         E         L          I          Z        A A")
    print("         E         L          I         Z        A   A")
    print("         EEEE      L          I        Z        AAAAAAA")
    print("         E         L          I       Z        A       A")
    print("         E         L          I      Z        A         A")
    print("         EEEEEEE   LLLLLLL IIIIIII  ZZZZZZZ  A           A")
    print("=====================================================================")
    print('Talk to the program by typing in plain English and correct words')
    print('                      Enter "Bye" when done.')
    print("=====================================================================")
    #Eliza will introduce itself and ask for name of the user
    print ("\nHi, I'm Eliza, a psychotherapist. What is your name?")
    

    while True:
        statement = input(">")  #here user will enter input
        #In this Eliza is going to retrive the name of the user and save it in a varible for future use 
        if re.search(r'My name is (.*)', statement, flags=re.IGNORECASE):  
            to=word_tokenize(statement)
            name=to[3]
            print(re.sub(r'My name is (.*)', r'Hi \1!!! How can I help you today', statement,flags=re.IGNORECASE)) #The name identified above will be used here
        elif re.search(r'I want to (.*)', statement, flags=re.IGNORECASE): 
            #if a person writes that he/she wants to do something, Eliza will recognize it
            print(re.sub(r'I want to (.*)', name + r', Why do you want to \1?', statement,flags=re.IGNORECASE))
        elif re.search(r'I need (.*)', statement, flags=re.IGNORECASE):
            #if a person says he/she needs something, eliza will recignize the user needs
            print(re.sub(r'I need (.*)', name + r', Why do you need \1?', statement,flags=re.IGNORECASE))
        elif re.search(r'I can (.*)', statement, flags=re.IGNORECASE):
            #if a person says he/she can do anything, eliza will recognize and ask futher questions regarding same
            print(re.sub(r'I can (.*)', r'How do you know you can \1?', statement,flags=re.IGNORECASE))
        elif re.search(r"I can't (.*)", statement, flags=re.IGNORECASE):
            #if a person says he/she can't do anything, eliza will recognize and ask user to think of reasons why he/she cant
            print(re.sub(r"I can't (.*)", r"How do you know you can't \1?", statement,flags=re.IGNORECASE))
        elif re.search(r"I don't know I (feel|crave) .+",statement, flags=re.IGNORECASE): 
            #here we have used disjunction to select either from feel or crave
            print(re.sub(r"I don't know I (feel|crave) .+",r"Why don't you tell me more about your \1ings", statement,flags=re.IGNORECASE))	
        elif re.search(r"I (feel|crave) .+",statement, flags=re.IGNORECASE): 
            print(re.sub(r"I (feel|crave) .+",r"Tell me more about your \1ings", statement,flags=re.IGNORECASE))	
        elif re.search(r'Because I (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'Because I (.*)',r"Why do you think you \1?", statement,flags=re.IGNORECASE))
        elif re.search(r'I am (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I am (.*)',r'How long have you been \1?', statement,flags=re.IGNORECASE))
        elif re.search(r'I\'?m (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I\'?m (.*)',r'How does being \1 make you feel?', statement,flags=re.IGNORECASE))
        elif re.search(r'What (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'What (.*)',r'What do you think?', statement,flags=re.IGNORECASE))
        elif re.search(r'Are you ((^\?)*)\??',statement, flags=re.IGNORECASE):
            print(re.sub(r'Are you ((^\?)*)\??',r'Why does it matter whether I am \1', statement,flags=re.IGNORECASE))
        elif re.search(r'(.*) father(.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'(.*) father(.*)',r'How do you feel about your father?', statement,flags=re.IGNORECASE))
        elif re.search(r'(.*) family(.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'(.*) family(.*)',r'Do you have trouble showing affection with your family?', statement,flags=re.IGNORECASE))
        elif re.search(r'(.*) mother(.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'(.*) mother(.*)',r'What is your relationship with your mother like?', statement,flags=re.IGNORECASE))
        elif re.search(r'(.*) mother(.*)',statement, flags=re.IGNORECASE):
            #if user discuss about mother,Eliza will spot the word and indulge into futher knowing the relationship
            print(re.sub(r'(.*) mother(.*)',r'What is your relationship with your mother like?', statement,flags=re.IGNORECASE))
        elif re.search(r'I want (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I want (.*)',r'If you got \1, then what would you do?', statement,flags=re.IGNORECASE))
        elif re.search(r'I would (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I would (.*)',r'Could you explain why you would \1 ?', statement,flags=re.IGNORECASE))
        elif re.search(r'You are(.*)',statement, flags=re.IGNORECASE):
            #If user says something disrespecting to Eliza,it will have a perfect reply
            print(re.sub(r'You are(.*)',r'Perhaps you are really talking about yourself?', statement,flags=re.IGNORECASE))   
        elif re.search(r'You (.*)',statement, flags=re.IGNORECASE):
            #In case user starts discussing Eliza,the below statement will again redirect focus to the user
            print(re.sub(r'You (.*)',name + r', We should be discussing you,not me. Tell me more about your inner feelings?', statement,flags=re.IGNORECASE))   
        elif re.search(r'I have (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I have (.*)',r'Now that you have \1, what will you do next?', statement,flags=re.IGNORECASE))   
        elif re.search(r'Is there (.*)',statement, flags=re.IGNORECASE):
            print(re.sub(r'Is there (.*)',r"It's likely that there is \1.", statement,flags=re.IGNORECASE))   
        elif re.search(r'I gave (.+) to (.+)',statement, flags=re.IGNORECASE):
            print(re.sub(r'I gave (.+) to (.+)',r"Why did you give \2 \1?", statement,flags=re.IGNORECASE))      
        elif re.search(r"I don't (.*)",statement, flags=re.IGNORECASE):
            print(re.sub(r"I don't (.*)",r"How can you say that don't \1?", statement,flags=re.IGNORECASE))
        elif re.search(r"(Good|Great|Awesome)(.*)",statement, flags=re.IGNORECASE):
            print(re.sub(r"(Good|Great|Awesome)(.*)",r"Wow!!! Tell me more", statement,flags=re.IGNORECASE))
        elif re.search(r'Bye(.*)',statement, flags=re.IGNORECASE):
            #when user wants to quit,user can say bye and Eliza will give below response and quit
            print("I hope I was able to help you,see you next time.Bye")
            break
        else:
            print ("I am not sure I understand you fully !!! \nLet's focus a bit... Tell me about your family.")
            #if a person enters gibberish or something which is not in above questions eliza will say that it doesn't understand and try to continue the talk

if __name__ == "__main__":
    main()
    
# Here we have used re.IGNORECASE as an argument in re.sub so that if the user enters any question
# irrespective of the case, eliza is going to recognize that.
# If the user inputs gibberish or a very complicated question,Eliza responds in plausible way
# This makes Eliza robust
# 
# References
# Joseph Weizenbaum - "Computational Linguistics" - 1966
# re.sub arguments - "www.stackoverflow.com"