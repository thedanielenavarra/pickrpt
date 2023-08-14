import os


def i2four(b, ord):
    bts=[0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        bts[7-i]=b%2
        b = b//2
        if b<=0:
            break
    if ord==1:
        return bts[:4]
    else:
        return bts[4:]
    
def four2i(m, ord):
    if ord==0:
        m=m[:4]
    else:
        m=m[4:]
    out=0
    for i in range(4):
        out=out+m[i]*2**i
    return out



def halfsum(b, msg, order):
    realb=four2i(b, order)
    realmsg=four2i(msg, order)
    while realb+realmsg>255:
        realb-=255
    return realb+realmsg


def modulefile(path, msg):
    carrierLen=os.path.getsize(path)
    step=carrierLen//len(msg*2)
    written=0
    pos=0
    with open(path, 'wb') as f:
        while pos<carrierLen:
            f.seek(pos)
            orig=f.read(1)
            for i in range(2):
                f.write(halfsum(i2four(orig, i), i2four(ord(msg[written]), i)))
                pos+=step
                f.seek(pos)
            written+=1
