import csv
import os
# Assign a variable for thr file to load & the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Set Total Votes to 0
total_votes=0
# Candidates Option & candidate votes
candidate_options=[]
# 1. Declare empty dictionary
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the Election Data file
with open(file_to_load) as election_data :

    # Open the Electinon Alaysis txt filr to write 
    files_to_save = os.path.join("analysis", "election_analysis.txt")
    #with open(files_to_save) as txt_file :
    File_reader = csv.reader(election_data)
    #Print row header 
    header= next(File_reader)
    # print each row in CSV file
    for row in File_reader :
        total_votes+=1
        candidate_name=row[2]
        if candidate_name not in candidate_options :
        #append candidate name to candidate_option
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
        # Save the results to our text file.
    with open(files_to_save, "w") as txt_file :
        # Print the final vote count to the terminal.
        election_results = (
            f" \nElection Results\n"
            f"-------------------------\n"
            f"Total Votes:  {total_votes:,}\n"
            f"-------------------------\n")  
        print(election_results)
        txt_file.write(election_results)

    #print(candidate_votes)
#iterate thru' candidate list
for candidate_name in candidate_votes :
    # find the number of votes for the candidate
    votes= candidate_votes[candidate_name]
    # calculate the percentage
    vote_percentage=float(votes)/float(total_votes) * 100 
   # print(f"{candidate_name} :received {vote_percentage:.1f} % of the vote ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage) :
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
     # Save the results to our text file.
    with open(files_to_save, "w") as txt_file :
        # Print the final vote count to the terminal.
        election_results = (
            f" \nElection Results\n"
            f"-------------------------\n"
            f"Total Votes:  {total_votes:,}\n"
            f"-------------------------\n")  
        print(election_results)
        txt_file.write(election_results)        
        # Print Individual candidate
            for candidate_name in candidate_votes :
                # find the number of votes for the candidate
                votes= candidate_votes[candidate_name]
                # calculate the percentage
                vote_percentage=float(votes)/float(total_votes) * 100 
                candidate_results = (
                    f"{candidate_name} : {vote_percentage:.1f} % ({votes:,})\n")
                txt_file.write(candidate_results)
        # Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)