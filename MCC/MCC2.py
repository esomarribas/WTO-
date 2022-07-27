# Read the following files 
# TP: \\s46file1.cd.intel.com\sdx\program\1274\eng\hdmtprogs\spr_sds\TestProgram\SPREFJX21E2172SBFT
from ast import And
from operator import index

## File we need: Compare_Results.txt -> just for double check; Compare_Final_Results -> data from Compare function 
# Final_Plist -> you insert all patterns from Plist
# patmodify_Class -> File optimized from Class
# patmodify_Sort -> original Patmodify file from Sort TP 


## ************** Just for WT FIX *****
fix = 0 # Enable fiz function -> Normal Mode // 1 - . Full Plist mode // 2 -> For some specific 
WT_fix = 1000 # WT you need to increase
delta = 10

# *************************************
class_file = open('MCC\patmodify_Class_MCC.txt')
sort_file = open('MCC\patmodify_Sort_MCC.txt')
env_file = open('MCC\EnvironmentFile_!ENG!.env')
plist_file = open('MCC\Final_Plist.txt')
results_file = open('MCC\Results.txt')
results_Sort_file = open('MCC\R_Sort_data.txt') # File with Results from script for Sort 
results_Class__file = open('MCC\R_Class_data.txt')# File with Results from script for Class
results__file = open('MCC\Results.txt')


#Global Variables 
Class_file = 'MCC\patmodify_class.txt'
Sort_File = 'MCC\patmodify_sort.txt'
Plist_File = 'MCC\Final_Plist.txt'
Env_Flie = 'MCC\EnvironmentFile_!ENG!.env'
Results_File = 'MCC\Results.txt'
Results_Sort_File = 'MCC\R_Sort_data.txt'# File with Results from script for Sort 
Results_Class_File = 'MCC\R_Class_data.txt' #File with Results from script for Class
Compare_Results_File = 'MCC\Compare_Results.txt'
Esp_VID_File = 'MCC\Esp_VID_File.txt'


R_Class_data = 'MCC\R_Class_data.txt'
date_results = []
data_Sort_results = []
data_Class_results = []
date_sort = []
date_Compare = []
date_list = []
read_sorT =[]
date_patm_sort=[]
patm_sort_list = []
R_class = []
WTO_sort = []
WTO1_sort = []

date_class = []
date_patm_class=[]
patm_class_list = []
VID_compare_list = []
WT_compare_list = []
date = []
linea = []
pttrn_ID = []
pttrn_ID_sort = []

pttrn_list = []

pttrn_sort = []
pttrn_class =[]
len_pttrn_sort = 0
len_pttrn_list = 0
STF_pID_Class2 = []
item61 =[]
e = []
g = []
h= []
i = []
x = []

STF = []
TAP = []
newpttrn = []
Final_list = []
# Function gets pttrn ID from Plist_instance file 
# Import the variables is pttrn_list has all pttrn id in file
def get_ID():
    with open(Plist_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_list.append(line.strip('\n'))
            #print(date_sort)
    
    for linea in date_list:
        pttrn_ID = linea[9:16] # variable use to get pttrn ID
        pttrn_list.append(pttrn_ID)#List with all pttrn
        #print(pttrn_list) # show list of pttrn ID list 
    len_pttrn_list = len(pttrn_list)
    print('Len Plist:',len_pttrn_list) 
    #print('Pattern ID:',pttrn_list) # show list of pttrn ID list 

    with open("MCC\R_Plist.txt", "w") as external_file:
        print('Pttrn:',pttrn_list, file=external_file)
        external_file.close()
    
get_ID()

date_Esp_VID = []
Esp_VID_sub_list = []
Esp_VID_list = []

def get_Esp_VID():
    print('\n')
    print('********* Specific VID ******* \n')
    with open(Esp_VID_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_Esp_VID.append(line.split())
        print('Your VID: ',date_Esp_VID)
    if fix == 2:
        len_Esp_VID_list = len(date_Esp_VID)
        print('LEn VID:',len_Esp_VID_list)
    else:
        print(' No specific Mode')
get_Esp_VID()


#Function read pttrn_list and search for that ppttrn in class 
class_list = [] #Contains pttrn, type STF or TAP and waiting 
class_list_VID = [] #Contains pttrn, type STF or TAP and waiting 

def get_class():
    print('\n')
    print('********* Class ******* \n')
    with open(Class_file) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_class.append(line.split())

    for index1 in pttrn_list:
        #print(index1) # print Class VID 
        for index2 in date_class:
            class_sub_list = [] # Class vector data
            len_class_VID = []
            if index1 == index2[4][9:16]: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA 
                len_class_VID.append(index2[4][9:16])
                class_sub_list.append(index2[4][9:16])
                class_sub_list.append(index2[5][0:3])
                class_sub_list.append(int(index2[9]))
                class_list.append(class_sub_list) #List compare with list Sort, Full list
    len_class_list = len(class_list)
    print('Len Class:',len_class_list//2)
    
    if fix ==2: # Just for especif VID in order change some patterns

        for index1 in date_Esp_VID:
            #print(index1) # print Class VID 
            for index2 in date_class:
                class_sub_list = [] # Class vector data
                len_class_VID = []
                if index1 == index2[4][9:16]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA 
                    len_class_VID.append(index2[4][9:16])
                    class_sub_list.append(index2[4][9:16])
                    class_sub_list.append(index2[5][0:3])
                    class_sub_list.append(int(index2[9]))
                    class_list_VID.append(class_sub_list) #List compare with list Sort, Full list
        len_class_list = len(class_list_VID)
        print('Len Class VID:',len_class_list)        
    #print(class_list) #full class vecto

    with open("MCC\R_Class_data.txt", "w") as external_file:
        for index1 in pttrn_list: # get VID list
            for index2 in date_class:
                class_sub_list = [] # Class vector data
                if index1 == index2[4][9:16]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9], file=external_file)
        external_file.close()
get_class()
sort_list = []
sort_VID_list = []


def get_sort():
    print('\n')
    print('********* Sort ******* \n')
    with open(Sort_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_sort.append(line.split())

    for index3 in pttrn_list:  # get VID from plist
        #print(index3) # print Class VID  
        for index4 in date_sort:
            #print(index4[4][2:9]) # VID sort data 
            #print(index4[5]) # TYPE sort data
            #print(index4[9]) #WT sort data
            sort_sub_list = [] # sort vector data
            if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                sort_WT1 = index4[9].split(",")
                sort_WT =  int(sort_WT1[0])
                #print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:',sort_WT ) # SHOW SORT DATA
                sort_sub_list.append(index4[4][2:9])
                sort_sub_list.append(index4[5][0:3])
                sort_sub_list.append(sort_WT)
                sort_list.append(sort_sub_list) #List compare with list Sort, Full list
    len_sort_list = len(sort_list)
    print('Len Sort:',len_sort_list//2)

    if fix ==2: 
        for index3 in date_Esp_VID:  # get VID from plist
        #print(index3) # print Class VID  
            for index4 in date_sort:
                #print(index4[4][2:9]) # VID sort data 
                #print(index4[5]) # TYPE sort data
                #print(index4[9]) #WT sort data
                sort_VID_sub_list = [] # sort vector data
                if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    sort_WT1 = index4[9].split(",")
                    sort_WT =  int(sort_WT1[0])
                    #print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:',sort_WT ) # SHOW SORT DATA
                    sort_VID_sub_list.append(index4[4][2:9])
                    sort_VID_sub_list.append(index4[5][0:3])
                    sort_VID_sub_list.append(sort_WT)
                    sort_VID_list.append(sort_VID_sub_list) #List compare with list Sort, Full list
        len_sort_list_VID = len(sort_VID_list)
        print('Len Sort VID:',len_sort_list_VID)


    with open("MCC\R_Sort_data.txt", "w") as sort_file:
        for index3 in pttrn_list:  # get VID from plist 
            for index4 in date_sort:
                sort_sub_list = [] # sort vector data
                WT1 = index4[9].split(",")
                WT =  WT1[0]
                if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:', WT, file=sort_file)
        sort_file.close()                  
get_sort()

           
results_list = []
sort_VID = []
Data_STF = []
Data_TAP = []
Data_STF1 = []
Data_TAP1 = []
Class_fix = []
Data_DIFF_STF = []
Data_DIFF_STF_1 =[]
def get_Results():
    print('\n')
    print('********* RESULTS ******* \n')
    #print('Class:',class_list)
    #print('Sort:',sort_list)
    for Class in class_list:
        for Sort in sort_list:
            #print('Class', Class[0])
            #print('Sort', Sort[0])
            if Class[0] == Sort[0] :
                if Class[1] =="STF" and Sort[1] =="STF":
                    if Class[2] < Sort[2]:
                        diff_STF = Sort[2]- Class[2] 
                        D_STF = 'Pattern:' +  Class[0] + ' Class_WT:' + str(Class[2]) + ' // ' + ' Sort_WT:' + str(Sort[2])+ ' -->' + ' DIFF_WT:' + str(diff_STF)
                        #print(D_STF)
                        Data_DIFF_STF.append(D_STF)
                        #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                        if diff_STF > delta:
                            STF = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class[2]) + ',R7'
                            Data_STF.append(STF)
                            TAP_WT1 = int(Class[2])//4
                            TAP_WT = str(TAP_WT1)
                            TAP ='+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT) + ',R7'
                            Data_TAP.append(TAP)
                            if fix == 4: # add Wt multiple 
                                #print('Fix')
                                Class_fix = Class[2]* WT_fix
                                #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                                STF1 = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class_fix) + ',R7'
                                Data_STF1.append(STF1)
                                TAP_WT2 = int(Class_fix)//4
                                TAP_WT3 = str(TAP_WT2)
                                TAP1 ='+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Data_TAP1.append(TAP1)
                                print(STF1) 
                                print(TAP1)
                            if fix == 3: # Add half Diff for full plist 
                                D_STF = int(Sort[2] - Class[2] )/2
                                #print(D_STF)
                                Final_D_STF = int (Class[2] + D_STF )                 
                                #print(Final_D_STF)
                                STF3 = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Final_D_STF) + ',R7'
                                Data_STF.append(STF3)
                                TAP_WT4 = Final_D_STF/4
                                TAP_WT5 = int(Final_D_STF/4)
                                TAP_WT3 = str(TAP_WT5)
                                TAP3 ='+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Data_TAP.append(TAP3)
                                Diff_SFT_TAP = int(TAP_WT4) - TAP_WT4
                                #print(Diff_SFT_TAP)
                                if Diff_SFT_TAP >= 0.0:
                                    print(STF3) 
                                    print(TAP3)
                            if fix == 1: # ADD specfic Wait Time
                                
                                #print('Fix')
                                Class_fix = Class[2] + WT_fix
                                #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                                STF1 = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class_fix) + ',R7'
                                Data_STF1.append(STF1)
                                TAP_WT2 = int(Class_fix)//4
                                TAP_WT3 = str(TAP_WT2)
                                TAP1 ='+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Data_TAP1.append(TAP1)
                                D_WT_1 =  Sort[2] - Class_fix
                                D_STF_1 = 'Pattern: ' +  Class[0] + ' Class_WT: ' + str(Class_fix) + ' // ' + ' Sort_WT: ' + str(Sort[2])+ ' -->' + ' DIFF_WT: ' + str(D_WT_1)
                                #print(D_STF)
                                Data_DIFF_STF_1.append(D_STF_1)
                                print(STF1) 
                                print(TAP1)
                            if fix == 0:
                                print(STF) 
                                print(TAP)
    with open("MCC\R_DIFF_Results.txt", "w") as external_file:           
        for list in  Data_DIFF_STF:
            print(list, file=external_file)                       
                            
    with open("MCC\Results.txt", "w") as external_file:           
        for list in  Data_STF:
            print(list, file=external_file)
        for list2 in  Data_TAP:
            print(list2, file=external_file)
    
    if fix == 1:
        print('Fix file')
        with open("MCC\Results_FIX.txt", "w") as external_file:           
            for list in  Data_STF1:
                print(list, file=external_file)
            for list2 in  Data_TAP1:
                print(list2, file=external_file)
        with open("MCC\R_DIFF_1.txt", "w") as external_file:           
            for list in  Data_DIFF_STF_1:
                print(list, file=external_file)
        

get_Results() 
Compare_sub_list = []
Compare_list = []

def get_Compare():
    print('\n')
    print('********* Compare  Sort ******* \n')
    with open(Compare_Results_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_Compare.append(line.split())
 
        for index4 in date_Compare:
            #print(index4)
            #print(index4[4][2:9]) # VID sort data 
            #print(index4[5]) # TYPE sort data
            #print(index4[10]) #WT sort data
            Compare_sub_list = [] # sort vector data
            
            Compare_WT1 = index4[9].split(",")
            Compare_WT =  int(Compare_WT1[0])
            #print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:',Compare_WT )
            Compare_sub_list.append(index4[4][2:9])
            Compare_sub_list.append(index4[5][0:3])
            Compare_sub_list.append(Compare_WT)
            Compare_list.append(Compare_sub_list) #List compare with list Sort, Full list
            #print(Compare_list)
    len_Compare_list = len(Compare_list)
    print('Len Sort VID:',len_Compare_list)

    with open("MCC\R_Compare_data.txt", "w") as sort_file:
        for index3 in pttrn_list:  # get VID from plist 
            for index4 in date_sort:
                Compare_sub_list = [] # sort vector data
                WT1 = index4[9].split(",")
                WT =  WT1[0]
                if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:', WT, file=sort_file)
        sort_file.close()
    
get_Compare()


def get_CompareResults():
    
    #print('*********  COMPARE FINAL RESULTS ******* \n')
    #print('Class:',class_list)
    #print('Compare:',Compare_list)
    for Compare in Compare_list:
        for Sort in sort_list:
            #print('Class', Class[0])``
            #print('Sort', Sort[0])
            if Compare[0] == Sort[0] :
                if Compare[1] =="STF" and Sort[1] =="STF":
                    if Compare[2] >= Sort[2]:
                        
                        #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                        STF = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                        Data_STF.append(STF)
                        TAP_WT1 = int(Compare[2])//4
                        TAP_WT = str(TAP_WT1)
                        TAP ='+ SBFT@_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*' +' :TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT) + ',R7'
                        Data_TAP.append(TAP)
                        print(STF) 
                        print(TAP)
                            
    with open("MCC\Compare_Final_Results.txt", "w") as external_file:           
        for list in  Data_STF:
            print(list, file=external_file)
        for list2 in  Data_TAP:
            print(list2, file=external_file)
    print('\n')
    print('********* END Compare  Sort ******* \n')                  
get_CompareResults() 



def default_Sort():
    print('********* DEFAULT VALUES ******* \n') 
    #New_WT_STF = 7520*Def_WT
    for RElaxed_WT in pttrn_list: 
        #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
        STF1 = '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  RElaxed_WT + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + '7520' + ',R7'
        Data_STF1.append(STF1)
        '''TAP_WT2 = int(Class_fix)//4
        TAP_WT3 = str(TAP_WT2)'''
        TAP1 ='+ SBFT_WAITTIME MAIN PAT '+ '*V' +  RElaxed_WT + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + '1880' + ',R7'
        Data_TAP1.append(TAP1)
        print(STF1) 
        print(TAP1)

                            
default_Sort()