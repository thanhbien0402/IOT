import json

json_file = 'scheduler_data.json'

class sched:
    id = 0
    cycle = 0
    flow1 = 0
    flow2 = 0
    flow3 = 0
    area = -1
    isActive = False
    sched_name = ''
    start_time = ''
    end_time = ''
    
    def __init__(self,id):
        self.id = id
    
    def set_sched(self):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if self.id < len(data):
                temp = data[self.id]
                self.cycle = temp["cycle"]
                self.flow1 = temp["flow1"]
                self.flow2 = temp["flow2"]
                self.flow3 = temp["flow3"]
                self.area = temp["area"]
                self.isActive = temp["isActive"]
                self.sched_name = temp["sched_name"]
                self.start_time = temp["start_time"]
                self.end_time = temp["end_time"]
        
    def print_sched(self):
        print("scheduler name: ", self.sched_name)
        print("scheduler cycle: ", self.cycle)
        print("scheduler flow1: ", self.flow1)
        print("scheduler flow2: ", self.flow2)
        print("scheduler flow3: ", self.flow3)
        print("scheduler area: ", self.area)
        print("scheduler is active: ", self.isActive)
        print("scheduler start: ", self.start_time)
        print("scheduler end: ", self.end_time)

def create_sched_list(): 
    sched_list = []
    with open(json_file, 'r', encoding='utf-8') as file:
        temp = json.load(file)
        for tmp in range(len(temp)):
            sched_tmp = sched(tmp)
            sched_tmp.set_sched()
            sched_list.append(sched_tmp)
    return sched_list