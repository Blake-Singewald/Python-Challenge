import csv

#initiallizing all the variables to be used
total_votes = []
canidate_list = []
unique_cand = []

#opens the election CSV file
with open('election_data.csv', newline='') as f:
    reader = csv.reader(f)
    
    #skips header row
    header = next(reader)
    
    for row in reader: 
        #creates list with all canidates voted for in the spreadsheet
        canidate_list.append(row[2])
        
#iterates through the whole list of canidates, then will check to see if
#there is a new candidate that has not showed up yet
for i in canidate_list: 
    #print(i)
    if i not in unique_cand:
        unique_cand.append(i)
        
        #if new candidate add new index to running total of votes for each canidate
        total_votes.append(int(1))
        
    else:
        #checks where the non unique canidate is and adds to the total of 
        #votes for that person
        for j in range(len(unique_cand)):
            if i == unique_cand[j]:
                total_votes[j] += 1


#finds the person with most votes and corresponding index
winner = max(total_votes)
winner_index = total_votes.index(max(total_votes))

#prints required information to terminal
print("Election Results")
print("----------------------------")

print(f"Total Votes: {len(canidate_list)}")
print("----------------------------")

#goes through a loop to print each candidate with vote count and percentage of total votes
for i in range(len(unique_cand)):
    print(f"{unique_cand[i]}: {round(total_votes[i]*100/len(canidate_list),3)}% ({total_votes[i]})")

print("----------------------------")

print(f"Winner: {unique_cand[winner_index]}")
print("----------------------------")


#prints to a .txt file
with open('PyPoll_Results.txt', 'w') as myfile:
    print("Election Results", file=myfile)
    print("----------------------------", file=myfile)

    print(f"Total Votes: {len(canidate_list)}", file=myfile)
    print("----------------------------", file=myfile)

    #goes through a loop to print each candidate with vote count and percentage of total votes
    for i in range(len(unique_cand)):
        print(f"{unique_cand[i]}: {round(total_votes[i]*100/len(canidate_list),3)}% ({total_votes[i]})", file=myfile)

    print("----------------------------", file=myfile)

    print(f"Winner: {unique_cand[winner_index]}", file=myfile)
    print("----------------------------", file=myfile)
    
myfile.close()
