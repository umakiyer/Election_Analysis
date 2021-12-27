import csv
import os
# Assign a variable for thr file to load & the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the Election Data file
with open(file_to_load) as election_data :

# COpen the Electinon Alaysis txt filr to write 
#files_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(files_to_save) as txt_file :
    File_reader = csv.reader(election_data)
#Print each row 
    header= next(File_reader)
    print(header)



