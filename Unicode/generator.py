import os
class SafeList(list):
    def __getitem__(self,key):
        if( key < list.__len__(self) ):
            return list.__getitem__(self,key)
        else: 
            return ''    
def safe_get(self,key):
    if( key < len(self) ):
        return self[key]
    else: 
        return 0
def generate(labels):
    path=os.path.join(os.getcwd(),'working')
    # f= open(path+"/labels.txt")
    # labels=f.read()
    # print(labels)
    f= open(path+"/output.txt",'w', encoding="utf-8")
    text=""
    for word in labels:
        # text = text + "".join(word)+ " "
        i=0
        word=SafeList(word)
        while( i < len(word) ):
            if( word[i]=='െ'):
                if( word[i+1]=='െ' ):
                    f.write(word[i+2])
                    f.write('ൈ')
                    i=i+2
                else:
                    f.write(word[i+1])
                    if(i+2 < len(word) and word[i+2]=='ാ'):
                        f.write('ൊ')
                        i=i+2
                    else:
                        f.write('െ')
                        i=i+1
            elif( word[i]=='േ' ):
                f.write(word[i+1])
                if(i+2 < len(word) and word[i+2]=='ാ'):
                    f.write('ോ')
                    i=i+2
                else:
                    f.write('േ')
                    i=i+1
            elif( word[i]=='്ര' ):
                f.write(word[i+1])
                f.write('്ര')
                i=i+1
            else:
                f.write(word[i])
            i=i+1
        f.write(' ')
    # f.write(text)
    f.close()
    print("generated output")