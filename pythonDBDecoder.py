#not part of my learning code found online
import mmap

def portals(dbfile):
    db = open(dbfile, 'rb')
    mm = mmap.mmap(db.fileno(), 0, access=mmap.ACCESS_READ)
    i, l = 0, set()
    while True:
        i = mm.find(b'\xea\x91|)', i)
        if i == -1:
            break
        l.add(mm[i+5:i+5+mm[i+4]].decode())
        i += 5 + mm[i+4]
    return l

print(portals("NV.db"))