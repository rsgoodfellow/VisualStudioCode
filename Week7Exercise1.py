votes = { # Dictionary for each canidate and their total votes
    "Trump": 0, # Canidate 1
    "Harris": 0, # Canidate 2
    "Goodfellow": 0 # Canidate 3
}

def cast_vote(candidate_name): # Method to cast a vote for a canidate
    if candidate_name in votes: # if statement checking if user entered canidate is in the system
        votes[candidate_name] += 1 # adds vote to selected canidate
        print(f"Voted for {candidate_name}.") # Displays text confirming the canidate you voted for
    else: # else statement if user entered canidate is not in the system
        print("Invalid candidate.") # displays text saying invalid canidate

def display_results(): # method to display the election results
    print("Voting Results:") # displays text
    for candidate, vote_count in votes.items(): # for loop that loops through each canidate and displays their name and vote count
        print(f"{candidate}: {vote_count} votes") # see above

def reset_votes(): # method to reset the vote count
    for candidate in votes: # for loop that loops through each canidate
        votes[candidate] = 0 # sets the canidates vote count to 0
    print("Votes have been reset.") # displays text confirming the users action

def main(): # main method
    while True: # while loop to loop the program until the user exits
        print("Ballot Box Menu:") # Menu text
        print("1. Cast Vote") # option 1
        print("2. Display Results") # option 2
        print("3. Reset Votes") # option 3
        print("4. Exit") # option 4

        choice = input("Enter your choice: ") # user input

        if choice == '1': # if condition for option 1
            candidate_name = input("Enter candidate name: ") # asks user to enter a canidate name
            cast_vote(candidate_name) # calls cast_vote method with user entered canidate as input
        elif choice == '2': # else if condition for opiton 2
            display_results() # calls display_results method
        elif choice == '3': # else if condition for opiton 3
            reset_votes() # calls reset_votes method
        elif choice == '4': # else if condition for opiton 4
            print("Exiting") # displays text
            break # breaks from while loop
        else: # else condition if invalid input
            print("Invalid choice. Please try again.") # tells the user they're dumb

if __name__ == "__main__": # statement to run the program
    main() # calls main method