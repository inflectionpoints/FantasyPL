import csv
import requests
import time


a = time.time()


def transfersdata():
    # @param gws = first and last gameweek
    
    with open('ORTable.csv', mode='r',encoding="utf-8") as Players:
       league  = list(csv.DictReader(Players))
    url1 = "https://fantasy.premierleague.com/api/entry/"
    TransferData = []
 
    for i in range(0, len(league)): #change this
        url = url1 + str(league[i]['entry'])+"/transfers/#/" 
        TData = requests.get(url).json()
                
        for j in TData:
            j.update({'PlayerName':league[i]['player_name']})
            j.update({'PlayerID':league[i]['id']})
            j.update({'EntryID':league[i]['entry']})
            

        
        TransferData.append(TData)
    filewriter(TransferData,'TransferData')
        
        
        
      
def filewriter(list1, filename):
    # @param list1 = list of dictonaries.
    # @param filename= string of desired CSV name.
    #Outputs each list/dictionary set to a CSV.
    #PlayerData is in the List/List/Dictionary Format and needs to be cleaned in the try/catch
    #League data isn't.

    list2 = []
    try:
        for i in range(0,len(list1)):
            for j in range(0, len(list1[i])):
                list2.append(list1[i][j])
    except:
        list2 = list1
        
  
    with open(filename+".csv","w", encoding="utf-8",newline='') as outf:
        w = csv.DictWriter(outf, fieldnames=list2[0].keys())
        w.writeheader()
        w.writerows(list2)

transfersdata()




b= time.time()
print(b-a)




