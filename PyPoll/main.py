#Modules
import csv
import os

#Reading CSV Module
election_data = os.path.join('Resources/election_data.csv')
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the hedaer row first
    header = next(csvreader)

    #CHECK: SKIP HEADER
    #print(header)

    #List preparation
    voterid = []
    country = []
    candidates = []
    v_candidates = []
    ind_votes = []
    perc_votes = []

    #Task No.1: The total number of votes cast
    for row in csvreader:
        voterid.append(row[0])
        country.append(row[1])
        candidates.append(row[2])

    total_votes = len(voterid)

    #CHECK:TOTAL VOTES
    #print(total_votes)
    
    #List first candidate in the list
    v_candidates.append(candidates[0])

    #Task No.2: A complete list of candidates who received votes
    for recvotes in range(total_votes-1):
        if candidates[recvotes+1] != candidates[recvotes] and candidates[recvotes+1] not in v_candidates:
            v_candidates.append(candidates[recvotes+1])

    #CHECK: CANDIDATES
    #print(v_candidates)

    #Task No.4: The total number of votes each candidate won

    for cvotes in range(len(v_candidates)):
        ind_votes.append(candidates.count(v_candidates[cvotes]))
    
    #CHECK: INDIVIDUAL VOTES
    #print(ind_votes)

    #Task No.3: The percentage of votes each candidate won
    for percvotes in range(len(v_candidates)):
        perc_votes.append(round(((ind_votes[percvotes]/total_votes)*100), 3))
    
    #CHECK: VOTE PERCENTAGES
    #print(perc_votes)

    winner = 0
    second = 0
    third = 0

    #Task No.5: The winner of the election based on popular vote
    second = ind_votes[0]
    secondname = v_candidates[0]
    secondperc = perc_votes[0]
    for votecount in range(len(v_candidates)):
        if ind_votes[votecount]>second:
            winner = ind_votes[votecount]
            winnername = v_candidates[votecount]
            winnerperc = perc_votes[votecount]
        elif ind_votes[votecount]<second:
            third = ind_votes[votecount]
            thirdname = v_candidates[votecount]
            thirdperc = perc_votes [votecount]

    #CHECK: Winner/Second/Third Info
    #print(winner)
    #print(winnername)
    #print(winnerperc)
    #print(second)
    #print(secondname)
    #print(secondperc)
    #print(third)
    #print(thirdname)
    #print(thirdperc)

    #TEXT FILE
    output_file=open("Analysis/pypoll.txt","w")
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write("Total Votes: "+ str(total_votes)+"\n")
    output_file.write("-------------------------\n")
    output_file.write(str(v_candidates[0])+": "+ str(perc_votes[0])+"% ("+str(ind_votes[0])+")\n")
    output_file.write(str(v_candidates[1])+": "+ str(perc_votes[1])+"% ("+str(ind_votes[1])+")\n")
    output_file.write(str(v_candidates[2])+": "+ str(perc_votes[2])+"% ("+str(ind_votes[2])+")\n")
    output_file.write("-------------------------\n")
    output_file.write("Winner: "+str(winnername)+"\n")
    output_file.write("-------------------------\n")
    output_file.close()

    #PRINT TO THE TERMINAL
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+ str(total_votes))
    print("-------------------------")
    print(str(v_candidates[0])+": "+ str(perc_votes[0])+"% ("+str(ind_votes[0])+")")
    print(str(v_candidates[1])+": "+ str(perc_votes[1])+"% ("+str(ind_votes[1])+")")
    print(str(v_candidates[2])+": "+ str(perc_votes[2])+"% ("+str(ind_votes[2])+")")
    print("-------------------------")
    print("Winner: "+str(winnername))
    print("-------------------------")
