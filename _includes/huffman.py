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


def compress_file(filename):
    with open(filename,'rb') as file: #get data
        data=list(map(int,file.read()))
    hf=huffman(data)
    with open(f'{filename}.hfm.tbl','w') as file: #create a table file
        file.write(';'.join([f'{k}:{hf[k]}' for k in hf]))
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
    with open(filename+'.tbl') as file: #get table
        table={code:char for char,code in list(map(lambda c:c.split(':'),file.read().split(';')))}
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