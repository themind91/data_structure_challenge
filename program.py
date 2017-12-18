#!/usr/bin/python
# -*- coding: utf-8 -*-
from Job import PriorityQueueOfJob,Agent,Job

priority = PriorityQueueOfJob()

#lendo o arquivo
data = priority.readJsonFile('sample_input.json')

#inicializando o programa

for i in data:
    for key,value in i.items():
        if key == "new_job":
            job = Job(value["id"],value["type"],value["urgent"])
            priority.enqueue(job)
        elif key == "new_agent":
            agent = Agent(value["id"],
                           value["name"],
                           value["primary_skillset"],
                           value["secondary_skillset"],False)
            priority.createAgents(agent)


priority.dequeue()










