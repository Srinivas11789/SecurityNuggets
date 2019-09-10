# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

import sys
try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    return 100    

def optimalChoice(available_choice, current_score):
  
    # Logic 1 
    # * If the choice I make now will make opponent win, i will never choose it
    # * If the total is less than the choices I can make, I will make the next optimal choice

    # Analysis:
    # * It is also worth making the opponent with no moves to make
    # * Or come to zero first

    optimal_choice = None

    # Optimal logic only for when the current score is less than the sum(all choices)
    if current_score < sum(available_choice):

        # Brainstorm
        """
        for choice in range(len(available_choice)):
            if available_choice[choice] <= current_score and (current_score-available_choice[choice]) not in available_choice:
                for ch2 in available_choice[:choice]:
                    if ((current_score-available_choice[choice])-ch2) in available_choice and ((current_score-available_choice[choice])-ch2) != 0:
                        optimal_choice = ch2
                if not optimal_choice:
                    optimal_choice = available_choice[choice]
            elif choice <= current_score:
                optimal_choice = choice
        """

        # Choose from the choices
        for choice in range(len(available_choice)):
            #if available_choice[choice] == current_score:
            #    optimal_choice = available_choice[choice]
            #elif available_choice[choice] < current_score:
            #    for ch2 in available_choice[:choice]:

            # Select a choice which wont make the opponent win
            if available_choice[choice] <= current_score and (current_score-available_choice[choice]) not in available_choice:
                optimal_choice = available_choice[choice]
                # Consider opponents decision and make a better choice
                for ch2 in available_choice[:choice]:
                    if ((current_score-available_choice[choice])-ch2) in available_choice and ((current_score-available_choice[choice])-ch2) != 0:# and ((current_score-available_choice[choice])) not in available_choice:
                        optimal_choice = ch2
            elif available_choice[choice] <= current_score:
                # Fallback if you cant decide
                optimal_choice = available_choice[choice]

        # If the optimal logic does not work go with the minimum
        if not optimal_choice:
            if current_score in available_choice:
                optimal_choice = current_score
            else:
                optimal_choice = min(available_choice)
    else:
        # If the score is way above control ( sum of choices ), use the max choice to reduce score
        optimal_choice = max(available_choice)
    return str(optimal_choice)



def talk(address, port, key):

    # Initial Flow

    # Name
    connection = remote(address, port)
    response = connection.recvuntil("name?")
    print(response)
    connection.sendline("A")
    
    # Ready
    response = connection.recvuntil("Ready? Y/N")
    print(response)
    connection.sendline("Y")

    # Play Game
    key = "Your move:"
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
    
        # Game Start
        if "Well done this round" in response:
            responses = response.split("\n")
            print(responses)
            current_score = responses[5]
            current_score = int(current_score.strip("Total Score:"))
            allowed_moves = responses[4].strip("[]").split(",")
            allowed_moves_int = [int(item) for item in allowed_moves]
            allowed_moves_int.sort()
        elif "Round" in response:
            responses = response.split("\n")
            print(responses)
            allowed_moves = responses[3].strip("[]").split(",")
            allowed_moves_int = [int(item) for item in allowed_moves]
            allowed_moves_int.sort()
            current_score = int(responses[4].strip("Total Score:"))
            print(allowed_moves_int, current_score)
        else:
            responses = response.split("\n")
            print(responses, allowed_moves_int)
            current_score = response.split("\n")[2]
            current_score = int(current_score.strip("Total Score:"))
        
        # Decide on the answer
        #maxi = str(max(allowed_moves_int))
        answer = optimalChoice(allowed_moves_int, current_score)
        print("Current Score is: "+ str(current_score))
        print("My move is: "+ answer)
        print("Sending... "+ answer)
        connection.sendline(answer)

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print("Usage: ./client.py [IP] [Port] [Key]")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
