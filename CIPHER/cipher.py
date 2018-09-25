
# -*- coding: utf-8 -*-
"""
@author : aniket alvekar
           8001

"""


    
    
def Encryp(fpath,key1,key2,key3,key4):
    # lists of characters, numbers and symbols, possibly present in any
    #document
    l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    l2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l3 = ['!','@','$','#','%','&','(',')','_','-','+','=','{','[',']','}',':',';','"',"'",'<','>',',','.','?','/','`','^',' ','*']
    l4 = ['0','1','2','3','4','5','6','7','8','9']
        
    #path of file to be encrypted           
    file = fpath

    #list to store name and extension of file
    file_n =[]
    for i in file.split('.'):
        file_n.append(i)
        
    file_in_data=[]
    file_out_data=[]

    #inserting all the data from file to a list     
    fin = open(file,'r')
    for i in fin:
        for j in i:
            file_in_data.append(j)

    #key to encrypt data in particular pattern           
    key_inp1 = key1
    key_inp2 = key2
    key_inp3 = key3
    key_inp4 = key4

    #replacing original alphabet with its alter character
    for i in file_in_data:
        inp_request = i
        if(inp_request in l1):
            index = l1.index(inp_request)    
            ind = l1.index(inp_request)
            encr_char = ind + int(key_inp1)
            if(encr_char > 25) :
                en1 = encr_char - 26
                file_out_data.append(l1[en1])
            else :
                file_out_data.append(l1[encr_char])
        elif(inp_request in l2):
            index = l2.index(inp_request)    
            ind = l2.index(inp_request)
            encr_char = ind + int(key_inp2)
            if(encr_char > 25) :
                en1 = encr_char - 26
                file_out_data.append(l2[en1])
            else :
                file_out_data.append(l2[encr_char]) 
        elif(inp_request in l3):
            index = l3.index(inp_request)
            ind = l3.index(inp_request)
            encr_char = ind + int(key_inp3)
            if(encr_char > 29) :
                en1 = encr_char - 30
                file_out_data.append(l3[en1])
            else :
                file_out_data.append(l3[encr_char]) 
        elif(inp_request in l4):
            index = l4.index(inp_request)
            ind = l4.index(inp_request)
            encr_char = ind + int(key_inp4)
            if(encr_char > 9) :
                en1 = encr_char - 10
                file_out_data.append(l4[en1])
            else :
                file_out_data.append(l4[encr_char]) 
        else:
            pass
        

        #new file to write all encrypted data with same file path
        #(only ' _encrypt' added to original name of file). It is saved at same
        #location where original file is stored.
        
        new_file = file_n[0]+'_encrypt.'+file_n[1]
        fout =open(new_file,'w') 
        for i in file_out_data:
            fout.write(i)
        fout.close()
    
def Decryp(fpath,key1,key2,key3,key4):
    l1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    l2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l3 = ['!','@','$','#','%','&','(',')','_','-','+','=','{','[',']','}',':',';','"',"'",'<','>',',','.','?','/','`','^',' ','*']
    l4 = ['0','1','2','3','4','5','6','7','8','9']
        
    file = fpath
    file_n =[]
    for i in file.split('.'):
        file_n.append(i)
     
    file_in_data=[]
    file_out_data=[]
    
    fin = open(file,'r')
    for i in fin:
        for j in i:
            file_in_data.append(j)
            
    #key to encrypt data in particular pattern           
    key_inp1 = key1
    key_inp2 = key2
    key_inp3 = key3
    key_inp4 = key4
    
    for i in file_in_data:
        inp_request = i
        if(inp_request in l1):
            index = l1.index(inp_request)    
            ind = l1.index(inp_request)
            encr_char = ind - int(key_inp1)
            if(encr_char > 25) :
                en1 = encr_char + 26
                file_out_data.append(l1[en1])
            else :
                file_out_data.append(l1[encr_char])
        elif(inp_request in l2):
            index = l2.index(inp_request)    
            ind = l2.index(inp_request)
            encr_char = ind - int(key_inp2)
            if(encr_char > 25) :
                en1 = encr_char + 26
                file_out_data.append(l2[en1])
            else :
                file_out_data.append(l2[encr_char]) 
        elif(inp_request in l3):
            index = l3.index(inp_request)
            ind = l3.index(inp_request)
            encr_char = ind - int(key_inp3)
            if(encr_char > 29) :
                en1 = encr_char + 30
                file_out_data.append(l3[en1])
            else :
                file_out_data.append(l3[encr_char]) 
        elif(inp_request in l4):
            index = l4.index(inp_request)
            ind = l4.index(inp_request)
            encr_char = ind - int(key_inp4)
            if(encr_char > 9) :
                en1 = encr_char + 10
                file_out_data.append(l4[en1])
            else :
                file_out_data.append(l4[encr_char]) 
        else:
            pass
        
                
    new_file = file_n[0]+'_decrypted.'+file_n[1]
    fout =open(new_file,'w') 
    for i in file_out_data:
        fout.write(i)
    fout.close()

#Encryp('D:\demo.txt',2,2,2,2)
#Decryp('D:\demo_encrypt.txt',2,2,2,2)



    
