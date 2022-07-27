# Read the following files 
# TP: \\s46file1.cd.intel.com\sdx\program\1274\eng\hdmtprogs\spr_sds\TestProgram\SPREFJX21E2172SBFT
from operator import index


class_file = open('MCC\patmodify_Class_MCC.txt')
sort_file = open('MCC\patmodify_Sort_MCC.txt')
env_file = open('MCC\EnvironmentFile_!ENG!.env')
plist_file = open('MCC\Final_Plist.txt')

#Global Variables 
Class_file = 'MCC\patmodify_class.txt'
Sort_File = 'MCC\patmodify_sort.txt'
Plist_File = 'MCC\Final_Plist.txt'
Env_Flie = 'MCC\EnvironmentFile_!ENG!.env'

date_sort = []
date_list = []
read_sorT =[]
date_patm_sort=[]
patm_sort_list = []

date_class = []
date_patm_class=[]
patm_class_list = []

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
    #print('Len Plist:',len_pttrn_list) 
    
get_ID()
#print(pttrn_list)

#Function read pttrn_list and search for that ppttrn in class 
class_list = [] #Contains pttrn, type STF or TAP and waiting 
def get_class():
    #print('Class')
    with open(Class_file) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_class.append(line.split())
    
    #print(date_class[4][9:16])
    #print(date_class[4])
    #print(pttrn_list)
    for index1 in pttrn_list:
        #print(index1)
        for index2 in date_class:
            class_sub_list = []
            if index1 == index2[4][9:16]:
                #print('Pttrn:',index1,'de',index2[5],'con waiting:', index2[9])   
                class_sub_list.append(index2[4][9:16])
                class_sub_list.append(index2[5])
                class_sub_list.append(index2[9])
                class_list.append(class_sub_list) #List compare with list Sort
                #print('PRUEBA')
    #print(index2[5])

get_class()
#print(date_class)
#print(date_class[0][4][2:9])
#print('Class data:', class_list[1][1][0:3])
#print('\n',class_list)

#Function getts pttrn ID from patmodify_sort file
def get_sort():
    print('sort')
    with open(Sort_File) as fname: # file  with all pttrns of the Plist for one instance
        lines = fname.readlines()
        for line in lines:
            date_patm_sort.append(line.split())
    print('Sort data:',date_patm_sort[5][5][0:3])
    for index1 in date_patm_sort:
       for index2 in class_list:
            print('index 1:',index1[9])
            #print('index 2:',index2[0])
            #print('Before IF#1')
            if index2[0] == index1[4][2:9]: #and 
                #print('IF #1')
                if index2[1][0:3] == index1[5][0:3]:
                    print('Pttrn Sort:', index1[4][2:9], 'Pttrn Class',index2[0])                   
                    #print('Tipo Class:',index2[1][0:3],'=',index1[5][0:3],':Tipo Sort')  
                    print('WT Class:',index2[2],'=',index1[9],':WT Sort')
                    print(index1[9])
                    t = index1[9].split(",") # wait time split
                    e = int(t[0]) # solo variable int wait itme
                    f = int(index2[2]) # wait time class
                    h = []
                    if e > f:
                        g = f # nueva variable almacena new int wait time for sort
                        tap_wt = g//4
                        #print(tap_wt)
                        #print('e =',t[0],' >',index2[2],' = f')
                        #print('g =',g,' =',index2[2],' = f')
                        i = str(g) + ',R7' # wait time sort convertido a str
                        #print(i)
                        index1[9] = i
                        join_list = ' '.join(index1)
                        Final_list.append(join_list)
                    else:
                        join_list = ' '.join(index1)
                        Final_list.append(join_list)


                    #print('indesx 1:',index1)
                    #h.append(i) # wait time modificado 
                    #index1[9] = h
                    #print('Index2:',index2)
                    #print(t)
                    #print(e)
                    #print(f)
                    #print('Lo encontro porfin')
get_sort()

#print('Final list:',Final_list)
#print('File')
with open('MCC\MCC_WTO.txt', 'w') as filehandle:
    for listitem in Final_list:
        filehandle.write(listitem + '\n') 
#print('END FILE')    

#print('END FILE') 



#print(date_patm_sort)
#print(class_list[0][2])
#print(date_patm_sort[0][4][1:8])
#print(date_patm_sort[0][5][0:3])
#print(date_patm_sort[0][9])
##print(h)

   