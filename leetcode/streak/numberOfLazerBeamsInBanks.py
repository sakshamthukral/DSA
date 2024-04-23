from typing import List


def numDevices(floor_plan:str)->int:
    devices = 0
    for i in floor_plan:
        if i == "1":
            devices+=1
    return devices

def numberOfBeams(bank: List[str])->int:
    beams = 0
    floor = 0
    devices1 = 0
    devices2 = 0
    while floor<len(bank):
        floor_devices = numDevices(bank[floor])
        if floor_devices!=0:
            if devices1==0:
                devices1 = floor_devices
            elif devices2==0:
                devices2 = floor_devices
        
        if devices1!=0 and devices2!=0:
            beams+=(devices1*devices2)
            devices1 = devices2
            devices2 = 0
        floor+=1
    return beams

bank = [ele for ele in input().split()]
print(numberOfBeams(bank))