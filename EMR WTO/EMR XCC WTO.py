# Read the following files 
# TP: \\s46file1.cd.intel.com\sdx\program\1274\eng\hdmtprogs\spr_sds\TestProgram\SPREFJX21E2172SBFT
from ast import And
from operator import index
from traceback import print_tb

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

Plist_File = 'EMR WTO\Files\Final_Plist.txt'
Class_file = 'EMR WTO\Files\Class_patmodify.txt'
Sort_File = 'EMR WTO\Files\SORT_patmodify.txt'

def get_ID():
    with open(Plist_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_list.append(line.strip('\n')) # date_list has all data 
            #print(date_sort)
    
    for linea in date_list:
        #print(linea)
        pttrn_ID = linea[13:20] # variable use to get pttrn ID 
        #pttrn_ID = linea[0:7] # variable use to get pttrn ID
        pttrn_list.append(pttrn_ID)#List with all pttrn 
         
    len_pttrn_list = len(pttrn_list)
    print('Len Plist:',len_pttrn_list)
    print(pttrn_list) # show list of pttrn ID list 
    #print('Pattern ID:',pttrn_list) # show list of pttrn ID list 

    with open("EMR WTO\Results\R_Plist.txt", "w") as external_file:
        #print('Pttrn:',pttrn_list, file=external_file)
        external_file.close()
    
get_ID()

Debug_mode = 2
 # 1-> normal  // 2 -> add WT  // 3 -> set same WT (MLC -> 3760 // SLC -> 8000 )
more_wt = 2000
same_wt = 6000

def get_class():
    print('\n')
    print('********* Class ******* \n')
    with open(Class_file) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_class.append(line.split())
    #print(date_class)
    for index1 in pttrn_list:
        #print(index1) # print Class VID 
        for index2 in date_class:
            class_sub_list = [] # Class vector data
            len_class_VID = []
            STF_WT =[]
            TAP_WT =[]
            if Debug_mode == 1: 
                if index1 == index2[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                #print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9])
                    STF_WT = int(index2[9])
                    TAP_WT = STF_WT
                    if index2[5][0:3] == 'STF':                                         
                        print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(STF_WT)+ ',R7' )
                        len_class_VID.append(index2[4][9:16]) 
                        class_sub_list.append(index2[4][9:16]) # VID
                        class_sub_list.append(index2[5][0:3]) # Type
                        #class_sub_list.append(index2[9]) # WT
                        class_sub_list.append(int(index2[9])) # WT
                        class_list.append(class_sub_list) #List compare with list Sort, Full list
                    if index2[5][0:3] == 'TAP':
                        print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT)+ ',R7' )
            if Debug_mode == 2: 
                if index1 == index2[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                #print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9])
                    STF_WT = int(index2[9]) + more_wt
                    TAP_WT = STF_WT
                    if int(index2[4][2:9]) != (1893682 or 1893696 or 1893584):
                        if int(index2[9]) < 2500:
                            if index2[5][0:3] == 'STF':                                         
                                print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(STF_WT)+ ',R7' )
                                len_class_VID.append(index2[4][9:16]) 
                                class_sub_list.append(index2[4][9:16]) # VID
                                class_sub_list.append(index2[5][0:3]) # Type
                                #class_sub_list.append(index2[9]) # WT
                                class_sub_list.append(int(index2[9])) # WT
                                class_list.append(class_sub_list) #List compare with list Sort, Full list
                            if index2[5][0:3] == 'TAP':
                                print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT)+ ',R7' )
            '''if Debug_mode == 3: 
                if index1 == index2[4][2:9]: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                #print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9])
                    STF_WT = same_wt
                    TAP_WT = STF_WT//4
                    if index2[5][0:3] == 'STF':                                         
                        print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(STF_WT)+ ',R7' )
                        len_class_VID.append(index2[4][9:16]) 
                        class_sub_list.append(index2[4][9:16]) # VID
                        class_sub_list.append(index2[5][0:3]) # Type
                        #class_sub_list.append(index2[9]) # WT
                        class_sub_list.append(int(index2[9])) # WT
                        class_list.append(class_sub_list) #List compare with list Sort, Full list
                    if index2[5][0:3] == 'TAP':
                        print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index2[4][2:9] + 'D*'  +':TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT)+ ',R7' )'''
    len_class_list = len(class_list)
    print('Len Class:',len_class_list//2)
          
    #print(class_list) #full class vecto


get_class()

def get_Plist_WT():
    print('\n')
    print('********* Class ******* \n')
    with open(Class_file) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_class.append(line.split())
    #print(date_class)
    for index1 in pttrn_list:
        #print(index1) # print Class VID 
        #for index2 in date_class:
        STF_WT =[]
        TAP_WT =[]
        if Debug_mode == 3: 
            if index1 == index1: # Compare Class VID agains VID PLIST if are equals get data from Class
                #print('Pttrn:',index2[4][9:16],'de',index2[5][0:3],'WT:', index2[9]) # SHOW CLASS DATA '+ SBFT_WAITTIME MAIN PAT '+ '*V' +  Compare[0] + 'D*'  +' :STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(Compare[2]) + ',R7'
                #print('Pttrn:',index2[4][2:9],'de',index2[5][0:3],'WT:', index2[9])
                STF_WT = same_wt
                TAP_WT = STF_WT//4
                #if index2[5][0:3] == 'STF':                                         
                print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index1 + 'D*'  +':STF STF_TEST_WAIT_START 602 OPCODE_OPERAND MOV ' + str(STF_WT)+ ',R7' )
                #if index2[5][0:3] == 'TAP':
                print('+ SBFT_WAITTIME MAIN PAT '+ '*V' +  index1 + 'D*'  +':TAP TAP_TEST_WAIT_START 146 OPCODE_OPERAND MOV ' + str(TAP_WT)+ ',R7' )
        len_class_list = len(class_list)
    print('Len Class:',len_class_list//2)
          
    #print(class_list) #full class vecto


get_Plist_WT()


                        
                            


