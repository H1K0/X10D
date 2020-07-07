def huffman(data):
    units={} #getting element-wise info
    for c in data:
        if c in units:
            units[c]+=1
        else:
            units[c]=1
    units,codes=sorted([([u],units[u]) for u in units],key=lambda u:u[1]),dict.fromkeys(units.keys(),'')

    while units: #creating Haffman table
        if len(units)>2:
            b=int(units[0][1]+units[1][1]>units[1][1]+units[2][1])
        else:
            b=0
        for c in units[b][0]:
            codes[c]='0'+codes[c]
        for c in units[1+b][0]:
            codes[c]='1'+codes[c]
        units[2*b]=units[b][0]+units[1+b][0],units[b][1]+units[1+b][1]
        if len(units)>2:
            del units[1]
            units.sort(key=lambda u:u[1])
        else:
            del units
            break
    return codes



def tbl(table):
    table=';'.join([f'{k};{table[k]}' for k in table]).split(';')
    byts=[]
    for i in range(len(table)):
        if i%2:
            num=table[i]
        else:
            num=bin(int(table[i]))[2:]
        while len(num)>7:
            byts.append(int('1'+num[:7],2))
            num=num[7:]
        byts.append(int(num,2))
        byts.append(8-len(num))
    return bytes(byts)



def detbl(byts):
    byts=list(map(lambda b:bin(b)[2:].rjust(8,'0'),byts))
    dec=[]
    table={}
    stack=''
    i=0
    while i<len(byts):
        if byts[i][0]=='1':
            stack+=byts[i][1:]
        else:
            stack+=byts[i][int(byts[i+1],2):]
            dec.append(stack[:])
            stack=''
            i+=1
        i+=1
    for i in range(0,len(dec),2):
        table[dec[i+1]]=int(dec[i],2)
    return table



def compress_file(filename):
    with open(filename,'rb') as file: #get data
        data=list(map(int,file.read()))
    hf=huffman(data)
    with open(f'{filename}.hfm.tbl','wb') as file: #create a table file
        file.write(tbl(hf))
    l=''
    out=[]
    for i in range(len(data)): #encode to Haffman
        l+=hf[data[i]]
        while len(l)>=8:
            out.append(int(l[:8],2))
            l=l[8:]
    with open(f'{filename}.hfm','wb') as file: #save Haffman code
        file.write(bytes(out+[int(l.ljust(8,'0'),2),len(l)]))


def decompress_file(filename):
    with open(filename,'rb') as file: #get data
        data=[bin(byte)[2:].rjust(8,'0')for byte in file.read()]
        data[-2]=data[-2][:int(data[-1],2)]
        del data[-1]
        data=''.join(data)
    with open(filename+'.tbl','rb') as file: #get table
        table=detbl(file.read())
    stack=''
    out=[]
    for c in data: #decode Haffman
        stack+=c
        if stack in table:
            out.append(int(table[stack]))
            stack=''
    filename=filename[:-4]
    with open(f'{filename}','wb') as file: #save decoded data
        file.write(bytes(out))