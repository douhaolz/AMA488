import queue


class Machine:
    def __init__(self):
        self.state=1
        self.nextEvent=-1
        self.idleTime=0

class Product:
    def __init__(self):
        self.state=0
        self.waitTime=0


quenumOfSpinning=25
quenumOfWeaving =0
quenumOfFinishing =0
quenumOfPacking =0
queOfSpinning = queue.Queue()
for i in range(1,26):
    j=Product()
    queOfSpinning.put(j)
queOfSpinning.maxsize=25

queOfWeaving = queue.Queue()
queOfFinishing = queue.Queue()
queOfPacking = queue.Queue()
# for numberOfSpinning in range(1,11):
#     for numberOfWeaving in range(1,11):
#         for numberOfFinishing in range (1,11):
#             for numberOfPacking in range(1,11):
def simulate(numberOfSpinning,numberOfWeaving,numberOfFinishing,numberOfPacking):
    currentTime=0
    machineOfSpinning=[Machine() for i in range(1,numberOfSpinning+1)]
    machineOfWeaving = [Machine() for i in range(1,numberOfWeaving+1)]
    machineOfFinishing = [Machine() for i in range(1,numberOfFinishing+1)]
    machineOfPacking = [Machine() for i in range(1,numberOfPacking+1)]

    idleMachineOfSpinning = numberOfSpinning
    idleMachineOfWeaving = numberOfWeaving
    idleMachineOfFinishing = numberOfFinishing
    idleMachineOfPacking = numberOfPacking

    for i in range(0,numberOfSpinning):
        if(machineOfSpinning[i].state==1):
            if(queOfSpinning.empty()==False):
                spin = queOfSpinning.pop()










def process():
    EventSpan()



