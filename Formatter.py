import datetime
import pandas as pd
import csv
import re

#Initialising all dictionaries being used
refDict={}
Sunday={}
Monday={}
Tuesday={}
Wednesday={}
Thursday={}
Friday={}
Saturday={}
scoreDict={}#Score Dictionary to add up the score of every instance of the route referenced in scores.txt 
CounterDict={}#Counter Dictionary to count every instance of the route reference in scores.txt 
finalDict={}

def formatting():
    #Iterating through reference_data.text line by line 
    with open('reference-data.txt') as f:
        for line in f:
            #Initialising the refDict with the route code as a key and the route name as the value
            refDict[line[0:42]] = line[49:-1]
            #Initialising the score dictionary that will add up the score values with route codes as keys and arrays with array values for everyday of the week initialised as 0
            scoreDict[line[0:42]]=[0,0,0,0,0,0,0]
            #Initialising the counter which will count the amount of instances of the route in scores.txt storing an array with an array value for every day of the week initialised as 0
            CounterDict[line[0:42]]=[0,0,0,0,0,0,0]
    
    #Iterating through scores.text line by line         
    with open("scores.txt") as f:
        for line in f:
            date=line[0:10].replace('/','-')
            temp = pd.Timestamp(date)#Turning date value into week day name string value
            if(temp.day_name()=="Sunday"):#Constructing listener for day of the week string value
                CounterDict[line[11:53]][0]+=1 #Populating counter dictionary
                scoreDict[line[11:53]][0]+=int(line[53:len(line)].strip())#Populating score dictionary
                Sunday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][0]/CounterDict[line[11:53]][0])]#Populating corresponding day dictionary with route names, days and scores 
            if(temp.day_name()=="Monday"):
                CounterDict[line[11:53]][1]+=1
                scoreDict[line[11:53]][1]+=int(line[53:len(line)].strip())
                Monday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][1]/CounterDict[line[11:53]][1])]
            if(temp.day_name()=="Tuesday"): 
                CounterDict[line[11:53]][2]+=1
                scoreDict[line[11:53]][2]+=int(line[53:len(line)].strip())
                Tuesday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][2]/CounterDict[line[11:53]][2])]
            if(temp.day_name()=="Wednesday"):
                CounterDict[line[11:53]][3]+=1
                scoreDict[line[11:53]][3]+=int(line[53:len(line)].strip())
                Wednesday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][3]/CounterDict[line[11:53]][3])]
            if(temp.day_name()=="Thursday"):
                CounterDict[line[11:53]][4]+=1
                scoreDict[line[11:53]][4]+=int(line[53:len(line)].strip())
                Thursday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][4]/CounterDict[line[11:53]][4])]
            if(temp.day_name()=="Friday"):
                CounterDict[line[11:53]][5]+=1
                scoreDict[line[11:53]][5]+=int(line[53:len(line)].strip())
                Friday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][5]/CounterDict[line[11:53]][5])]
            if(temp.day_name()=="Saturday"):
                CounterDict[line[11:53]][6]+=1
                scoreDict[line[11:53]][6]+=int(line[53:len(line)].strip())
                Saturday[line[11:53]]= [refDict[line[11:53]], temp.day_name(), "{:.2f}".format(scoreDict[line[11:53]][6]/CounterDict[line[11:53]][6])]
           
    with open('reference-data.txt') as f:#Populating finalDict with arrays of day arrays as values and route codes as keys 
        for line in f:
            finalDict[line[0:42]]=[]
            finalDict[line[0:42]].append(Sunday[line[0:42]])
            finalDict[line[0:42]].append(Monday[line[0:42]])
            finalDict[line[0:42]].append(Tuesday[line[0:42]])
            finalDict[line[0:42]].append(Wednesday[line[0:42]])
            finalDict[line[0:42]].append(Thursday[line[0:42]])
            finalDict[line[0:42]].append(Friday[line[0:42]])
            finalDict[line[0:42]].append(Saturday[line[0:42]])
            
    with open('results.txt', 'a') as f:#Printing to a file
        for final in finalDict: 
            wr = csv.writer(f)
            wr.writerows(sorted(finalDict[final], key=lambda x: x[2], reverse=True))
            
    #Removing commas from text file        
    listEdit=[]
    with open("results.txt","r") as f:  
       for line in f:
           listEdit.append(re.sub(","," ",line))
               
    with open("results.txt","w") as f:  
       for i in listEdit:
           f.write(i)
           
formatting()
         
