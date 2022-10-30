from _fetch import *
import json 


def getdb():

    db = ''
    with open(f'/_db/payloads.json','r') as f:
        db= json.loads(f.read())
    
    return db

class config:
    payloads = getdb['payloads']
    names    = getdb['names']
    status   = getdb['status']

def payloadsystem(fxc):
    if(fxc.startswith("set payload")):
        payloadname = fxc.split('set payload')[1].split()[0]
        print(payloadname)
        return True