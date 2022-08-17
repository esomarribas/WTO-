# Read the following files 
# TP: \\s46file1.cd.intel.com\sdx\program\1274\eng\hdmtprogs\spr_sds\TestProgram\SPREFJX21E2172SBFT
from ast import And
from operator import index
from traceback import print_tb

## File we need: Compare_Results.txt -> just for double check; Compare_Final_Results -> data from Compare function 
# Final_Plist -> you insert all patterns from Plist
# patmodify_Class -> File optimized from Class
# patmodify_Sort -> original Patmodify file from Sort TP 


## ************** Just for WT FIX *****
fix = 0 # Enable fiz function -> Normal Mode // 1 - . add WT Full Plist mode // 2 -> add hald diff // 3 -> multipli Wt  Full plist 
        # 4 -> when patterns doesnt existn in Sort, so first select mode 5 then 4
WT_fix = 1000 # WT you need to increase
delta = 200

# *************************************
class_file = open('HBM\Files\patmodify_Class_HBM.txt')
sort_file = open('HBM\Files\patmodify_Sort_HBM.txt')
def_sort_file = open('HBM\Files\patmod_SORT.txt')
#env_file = open('MCC\Files\EnvironmentFile_!ENG!.env')
plist_file = open('HBM\Final_Plist.txt')
results_file = open('HBM\Results.txt')
#results_Sort_file = open('MCC\R_Sort_data.txt') # File with Results from script for Sort 
#results_Class__file = open('MCC\R_Class_data.txt')# File with Results from script for Class
#results__file = open('MCC\Results.txt')


#Global Variables 
Class_file = 'HBM\Files\patmodify_class.txt'
Sort_File = 'HBM\Files\patmodify_Sort.txt'
Default_Sort_File = 'HBM\Files\patmod_SORT.txt'
Plist_File = 'HBM\Final_Plist.txt'
#Env_Flie = 'HBM\Files\EnvironmentFile_!ENG!.env'
#Results_File = 'MCC\Files\Results.txt'
#Results_Sort_File = 'MCC\R_Sort_data.txt'# File with Results from script for Sort 
#Results_Class_File = 'MCC\R_Class_data.txt' #File with Results from script for Class
Compare_Results_File = 'HBM\Compare_Results.txt'
Esp_VID_File = 'HBM\Esp_VID_File.txt'

# Variables
date_list = []
pttrn_list = []
date_class = []
#Function read pttrn_list and search for that ppttrn in class 
class_list = [] #Contains pttrn, type STF or TAP and waiting 
sort_list = []
date_sort = []
Data_DIFF_STF = [] # vector Class[2] < Sort[2]:
Data_DIFF_STF1 =[] # vector Class[2] > Sort[2]:
Data_STF = []
Data_TAP = []
# if fix ==1 
Data_STF1 = []
Data_TAP1 = []
Data_DIFF_STF_1 =[]
# if fix ==2 
Data_STF2 = []
Data_TAP2 = []
Data_DIFF_STF_2 =[]
# if fix ==3 
Data_STF3 = []
Data_TAP3 = []
Data_DIFF_STF_3 =[]
# if fix ==4 
Data_STF4 = []
Data_TAP4 = []
Data_DIFF_STF_4 =[]

date_Compare = []
Compare_sub_list = []
Compare_list = []
Data_def_STF =[]
Data_def_TAP =[]
def_date_sort = []
def_sort_list = []
##

def get_ID():
    with open(Plist_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_list.append(line.strip('\n')) # date_list has all data 
            #print(date_sort)
    
    for linea in date_list:
        #print(linea)
        pttrn_ID = linea[13:20] # variable use to get pttrn ID
        pttrn_list.append(pttrn_ID)#List with all pttrn 
        #print(pttrn_list) # show list of pttrn ID list 
    len_pttrn_list = len(pttrn_list)
    print('Len Plist:',len_pttrn_list) 
    #print('Pattern ID:',pttrn_list) # show list of pttrn ID list 

    with open("HBM\Results\R_Plist.txt", "w") as external_file:
        print('Pttrn:',pttrn_list, file=external_file)
        external_file.close()
    
get_ID()

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
            #print(index2[4][2:9])
            if index1 == index2[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA 
                len_class_VID.append(index2[4][2:9]) 
                class_sub_list.append(index2[4][2:9]) # VID
                class_sub_list.append(index2[5][0:3]) # Type
                class_sub_list.append(int(index2[9])) # WT
                class_list.append(class_sub_list) #List compare with list Sort, Full list
    len_class_list = len(class_list)
    print('Len Class:',len_class_list//2)
          
    #print(class_list) #full class vecto

    with open("HBM\R_Class_data.txt", "w") as external_file:
        for index1 in pttrn_list: # get VID list
            for index2 in date_class:
                class_sub_list = [] # Class vector data
                if index1 == index2[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9], file=external_file)
        external_file.close()
get_class()

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
            #print(index4[4][1:8]) # VID sort data 
            #print(index4[5]) # TYPE sort data
            #print(index4[9]) #WT sort data
            sort_sub_list = [] # sort vector data
            if index3 == index4[4][1:8]: # Compare Class VID agains VID PLIST if are equals get data from Class
                sort_WT1 = index4[9].split(",")
                sort_WT =  int(sort_WT1[0])
                #print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:',sort_WT ) # SHOW SORT DATA
                sort_sub_list.append(index4[4][1:8])
                sort_sub_list.append(index4[5][0:3])
                sort_sub_list.append(sort_WT)
                sort_list.append(sort_sub_list) #List compare with list Sort, Full list
    len_sort_list = len(sort_list)
    
    print('Len Sort:',len_sort_list//2)

    with open("HBM\R_Sort_data.txt", "w") as sort_file:
        for index3 in pttrn_list:  # get VID from plist 
            for index4 in date_sort:
                sort_sub_list = [] # sort vector data
                WT1 = index4[9].split(",")
                WT =  WT1[0]
                if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:', WT, file=sort_file)
        sort_file.close()                  
get_sort()
          
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
                        with open("HBM\Results\R_DIFF_Results.txt", "w") as external_file: # diff debug result  Class[2] > Sort[2]   
                            for list in  Data_DIFF_STF:
                                print(list, file=external_file)

                        if diff_STF > delta:
                            if fix == 0:
                                STF = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class[2]) + ',R7'
                                Data_STF.append(STF)
                                TAP_WT1 = int(Class[2])//4
                                TAP_WT = str(TAP_WT1)
                                TAP ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT) + ',R7'
                                Data_TAP.append(TAP)
                                print(STF) 
                                print(TAP) 
                                diff_STF = Sort[2]- Class[2]

                                
                                with open("HBM\Results\R_Fix_0.txt", "w") as external_file:   # normal debug         
                                    for list in  Data_STF:
                                        print(list, file=external_file)
                                    for list2 in  Data_TAP:
                                        print(list2, file=external_file)
                                with open("HBM\Results\R_DIFF_Fix_0.txt", "w") as external_file: # diff debug result  Class[2] > Sort[2]   
                                    for list in  Data_DIFF_STF:
                                        print(list, file=external_file)
                            
                            if fix == 1: # ADD specfic Wait Time
                                #print('Fix')
                                Class_fix = Class[2] + WT_fix
                                #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                                STF1 = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class_fix) + ',R7'
                                Data_STF1.append(STF1)
                                TAP_WT2 = int(Class_fix)//4
                                TAP_WT3 = str(TAP_WT2)
                                TAP1 ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Data_TAP1.append(TAP1)
                                print(STF1) 
                                print(TAP1)

                                D_WT_1 =  Sort[2] - Class_fix
                                D_STF_1 = 'Pattern: ' +  Class[0] + ' Class_WT: ' + str(Class_fix) + ' // ' + ' Sort_WT: ' + str(Sort[2])+ ' -->' + ' DIFF_WT: ' + str(D_WT_1)
                                #print(D_STF)
                                Data_DIFF_STF_1.append(D_STF_1)

                                with open("HBM\Results\R_Fix_1.txt", "w") as external_file:   # normal debug         
                                    for list in  Data_STF1:
                                        print(list, file=external_file)
                                    for list2 in  Data_TAP1:
                                        print(list2, file=external_file)

                                with open("HBM\Results\R_DIFF_Fix_1", "w") as external_file:   # normal debug         
                                    for list in  Data_DIFF_STF_1:
                                        print(list, file=external_file)

                            if fix == 2: # Add half Diff for full plist 
                                D_STF = int(Sort[2] - Class[2] )/2
                                #print(D_STF)
                                Final_D_STF = int (Class[2] + D_STF )                 
                                #print(Final_D_STF)
                                STF3 = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Final_D_STF) + ',R7'
                                TAP_WT4 = Final_D_STF/4
                                TAP_WT5 = int(Final_D_STF/4)
                                TAP_WT3 = str(TAP_WT5)
                                TAP3 ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Diff_SFT_TAP = int(TAP_WT4) - TAP_WT4
                                #print(Diff_SFT_TAP)
                                #print(Diff_SFT_TAP)
                                if Diff_SFT_TAP >= 0.0:
                                    Data_STF2.append(STF3)
                                    Data_TAP2.append(TAP3)
                                    print(STF3) 
                                    print(TAP3)
                                    D_WT_2 = Sort[2] - Final_D_STF
                                    D_STF_2 = 'Pattern: ' +  Class[0] + ' Class_WT: ' + str(Final_D_STF) + ' // ' + ' Sort_WT: ' + str(Sort[2])+ ' -->' + ' DIFF_WT: ' + str(D_WT_2)
                                    Data_DIFF_STF_2.append(D_STF_2)

                                    with open("HBM\Results\R_Fix_2.txt", "w") as external_file:   # normal debug         
                                        for list in  Data_STF2:
                                            print(list, file=external_file)
                                        for list2 in  Data_TAP2:
                                            print(list2, file=external_file)

                                    with open("HBM\Results\R_DIFF_Fix_2", "w") as external_file:   # normal debug         
                                        for list in  Data_DIFF_STF_2:
                                            print(list, file=external_file)
                                

                            if fix == 3: # add Wt multiple 
                                #print('Fix')
                                Class_fix = Class[2]* WT_fix
                                #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                                STF3 = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class_fix) + ',R7'
                                Data_STF3.append(STF3)
                                TAP_WT2 = int(Class_fix)//4
                                TAP_WT3 = str(TAP_WT2)
                                TAP3 ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT3) + ',R7'
                                Data_TAP3.append(TAP3)
                                print(STF3) 
                                print(TAP3)
                            
                    else: # else if Class[2] > Sort[2]
                        diff_STF1 = Sort[2]- Class[2] 
                        D_STF1 = 'Pattern:' +  Class[0] + ' Class_WT:' + str(Class[2]) + ' // ' + ' Sort_WT:' + str(Sort[2])+ ' -->' + ' DIFF_WT:' + str(diff_STF1)
                        #print(D_STF)
                        Data_DIFF_STF1.append(D_STF1)
                        with open("HBM\Results\R_DIFF_Not_Results.txt", "w") as external_file:   # diff debug result  Class[2] < Sort[2]            
                            for list in  Data_DIFF_STF1:
                                print(list, file=external_file)


    
    if fix == 3 : 
        D_WT_3 =  Sort[2] - Class_fix
        D_STF_3 = 'Pattern: ' +  Class[0] + ' Class_WT: ' + str(Class_fix) + ' // ' + ' Sort_WT: ' + str(Sort[2])+ ' -->' + ' DIFF_WT: ' + str(D_WT_3)
        Data_DIFF_STF_3.append(D_STF_3)

        with open("HBM\Results\R_Fix_3.txt", "w") as external_file:   # normal debug         
            for list in  Data_STF3:
                print(list, file=external_file)
            for list2 in  Data_TAP3:
                print(list2, file=external_file)

        with open("HBM\Results\R_DIFF_Fix_3", "w") as external_file:   # normal debug         
            for list in  Data_DIFF_STF_3:
                print(list, file=external_file)      
get_Results() 

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

    with open("HBM\Results\R_Compare_data.txt", "w") as sort_file:
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
                        STF = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                        Data_STF.append(STF)
                        TAP_WT1 = int(Compare[2])//4
                        TAP_WT = str(TAP_WT1)
                        TAP ='+ SBFT@_WAITTIME MAIN PAT ' + '*' +  Compare[0] + 'D*' +' :TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT) + ',R7'
                        Data_TAP.append(TAP)
                        print(STF) 
                        print(TAP)
                            
    with open("HBM\Compare_Final_Results.txt", "w") as external_file:           
        for list in  Data_STF:
            print(list, file=external_file)
        for list2 in  Data_TAP:
            print(list2, file=external_file)
    print('\n')
    print('********* END Compare  Sort ******* \n')                  
get_CompareResults() 

if fix ==5:
    def print_default_Sort(): # create a default data 

            print('********* DEFAULT VALUES ******* \n') 
            #New_WT_STF = 7520*Def_WT
            for RElaxed_WT in pttrn_list: 
                #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                STF1 = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  RElaxed_WT + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + '7520' + ',R7'
                Data_def_STF.append(STF1)
                '''TAP_WT2 = int(Class_fix)//4
                TAP_WT3 = str(TAP_WT2)'''
                TAP1 ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  RElaxed_WT + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + '1880' + ',R7'
                Data_def_TAP.append(TAP1)
                #print(STF1) 
                #print(TAP1)
            with open("HBM\Files\patmod_SORT.txt", "a") as external_file:   # normal debug         
                    for list in  Data_def_STF:
                        print(list, file=external_file)
                    for list2 in  Data_def_TAP:
                        print(list2, file=external_file)
                    print("Default data added ")
                                          
    print_default_Sort()

if fix ==4:
    def get_def_sort(): # compare default data vs plist
        print('\n')
        print('********* DEfault Sort ******* \n')
        with open(Default_Sort_File) as fname: # file  with all pttrns of the Plist for one instance
            lines = fname.readlines()
            for line in lines:
                def_date_sort.append(line.split())

        for index3 in pttrn_list:  # get VID from plist
            #print(index3) # print Class VID  
            for index4 in def_date_sort:
                #print(index4[1][4][1:8]) # VID sort data 
                #print(index4[5]) # TYPE sort data
                #print(index4[9]) #WT sort data
                def_sort_sub_list = [] # sort vector data
                if index3 == index4[4][1:8]: # Compare Class VID agains VID PLIST if are equals get data from Class
                    sort_WT1 = index4[9].split(",")
                    def_sort_WT =  int(sort_WT1[0])
                    #print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:',sort_WT ) # SHOW SORT DATA
                    def_sort_sub_list.append(index4[4][1:8])
                    def_sort_sub_list.append(index4[5][0:3])
                    def_sort_sub_list.append(def_sort_WT)
                    def_sort_list.append(def_sort_sub_list) #List compare with list Sort, Full list
        def_len_sort_list = len(def_sort_list)
        print(index4[1][4][1:8])
        print('Def Len Sort:',def_len_sort_list//2)

        with open("HBM\R_Def_Sort_data.txt", "w") as sort_file:
            for index3 in pttrn_list:  # get VID from plist 
                for index4 in def_date_sort:
                    def_sort_sub_list = [] # sort vector data
                    WT1 = index4[9].split(",")
                    WT =  WT1[0]
                    if index3 == index4[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                        print('Pttrn:',index4[4][2:9],'de',index4[5][0:3],'WT:', WT, file=sort_file)
            sort_file.close()                  
    get_def_sort()

    def get_results_def():
        print('\n')
        print('********* DEfault RESULTS ******* \n')
        #print('Class:',class_list)
        #print('Sort:',sort_list)
        for Class in class_list:
            for Sort in def_sort_list:
                #print('Class', Class[0])
                #print('Sort', Sort[0])
                if Class[0] == Sort[0] :
                    if Class[1] =="STF" and Sort[1] =="STF":
                        if Class[2] < Sort[2]:
                            diff_STF = Sort[2]- Class[2] 
                            #print('Class',  Class[0], ' C_Type', Class[1], '=', 'Sort', Sort[0], 'S_Type', Sort[1],'--> ' 'Class WT', Class[2],  'Sort WT', Sort[2])
                            if diff_STF > delta:                          
                                STF = '+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Class[2]) + ',R7'
                                Data_STF.append(STF)
                                TAP_WT1 = int(Class[2])//4
                                TAP_WT = str(TAP_WT1)
                                TAP ='+ SBFT_WAITTIME MAIN PAT ' + '*' +  Class[0] + 'D*:TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT) + ',R7'
                                Data_TAP.append(TAP)
                                print(STF) 
                                print(TAP)
                                D_STF = 'Pattern:' +  Class[0] + ' Class_WT:' + str(Class[2]) + ' // ' + ' Sort_WT:' + str(Sort[2]) + ' -->' + ' DIFF_WT:' + str(diff_STF)
                                #print(D_STF)
                                Data_DIFF_STF.append(D_STF)
        with open("HBM\Results\R_Fix_4.txt", "w") as external_file:   # normal debug         
            for list in  Data_STF:
                print(list, file=external_file)
            for list2 in  Data_TAP:
                print(list2, file=external_file)
        with open("HBM\Results\R_DIFF_Fix_4.txt", "w") as external_file: # diff debug result  Class[2] > Sort[2]   
            for list in  Data_DIFF_STF:
                print(list, file=external_file)
        

    get_results_def()