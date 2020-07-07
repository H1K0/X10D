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
    return byts



def detbl(byts):
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
    table=tbl(hf)
    out=[]
    ln=bin(len(table))[2:] #embed the table
    while len(ln)>7:
        out.append(int('1'+ln[:7],2))
        ln=ln[7:]
    out+=[int(ln,2),8-len(ln)]+table
    stack=''
    for i in range(len(data)): #encode to Haffman
        stack+=hf[data[i]]
        while len(stack)>=8:
            out.append(int(stack[:8],2))
            stack=stack[8:]
    with open(f'{filename}.hfm','wb') as file: #save Haffman code
        file.write(bytes(out+[int(stack.ljust(8,'0'),2),len(stack)]))


def decompress_file(filename):
    with open(filename,'rb') as file: #get data
        data=[bin(byte)[2:].rjust(8,'0')for byte in file.read()]
        data[-2]=data[-2][:int(data[-1],2)]
        del data[-1]
    ln='' #extract the table
    i=0
    while 1:
        if data[i][0]=='1':
            ln+=data[i][1:]
        else:
            ln+=data[i][int(data[i+1],2):]
            break
        i+=1
    del data[:i+2]
    table=detbl(data[:int(ln,2)])
    del data[:int(ln,2)]
    data=''.join(data)
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