import json
import requests

MachineSettingsPath = "/home/pi/CoffeeBreaker/CoffeeMachine/MachineSettings.json"

with open(MachineSettingsPath) as json_file:
        MachineSettings = json.load(json_file)

url = "http://" + MachineSettings['Ip'] + ":" + str(MachineSettings['Port']) + "/" # <- insert here method path

def getHelloWorld():
    resp = requests.get(url)
    print(resp.text)

def getOrderStatus():
    resp = requests.get(url + "getOrderStatus/" + str(MachineSettings['MachineID']))
    return resp.text # OK

def getTokenStatus():
    resp = requests.get(url + "getTokenStatus/" + str(MachineSettings['MachineID']))
    return resp.text # OK
        
def getToken():
    resp = requests.get(url + "getToken/" + str(MachineSettings['MachineID']))
    return resp.text

def getOrder():
    resp = requests.get(url + "getOrder/" + str(MachineSettings['MachineID']))
    try:
        JOrder = resp.json()
        return JOrder
    except:
        return resp # OK

def postTokenStatus(status):
    codeSmile = requests.post(url + "postTokenStatus/" + str(MachineSettings['MachineID']), json={"status": status})
    # return codeSmile
    # OK

def postToken(token):
    codeSmile = requests.post(url + "postToken/" + str(MachineSettings['MachineID']), json={"token": token})

def postOrderStatus(status):
    codeSmile = requests.post(url + "postOrderStatus/" + str(MachineSettings['MachineID']), json={"status": status})
    # return codeSmile   # optional (if you are in mood)
    # OK

def postOrder(JOrder):
    codeSmile = requests.post(url + "postOrder/" + str(MachineSettings['MachineID']), json=JOrder)

def postOrderBd(finalOrder, token):
    date = token[:10]
    time = token[10:19]    
    bdOrder={"date": date,
            "time": time,
            "type": finalOrder['type'],
            "strenght": finalOrder['strenght'],
            "volume": finalOrder['volume'],
            "milk": finalOrder['milk'],
            "shugar": finalOrder['shugar']
            }
    codeSmile = requests.post(url + "postBd/" + str(MachineSettings['MachineID']), json=bdOrder) # OK

'''
finalOrder ={"MachineID": 1,
            "type": 'espresso',
            "strenght": 4,
            "volume": 2,
            "milk": 0,
            "shugar": 0
            }
'''
