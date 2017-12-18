#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import re
import json

class Job:
    def __init__(self,id,type,urgent):
        self.id = id
        self.type = type
        self.urgent = urgent
        self.dt_created = datetime.datetime.now()

    def getType(self):
        return self.type

    def getPriority(self):
        return self.urgent


class Agent:
    def __init__(self,id,name,primary_skillset,secondary_skillset,job_request):
        self.id = id
        self.name = name
        self.primary_skillset = primary_skillset
        self.secondary_skillset = secondary_skillset
        self.job_request = job_request

    
class JobAssigned:
    def __init__(self,job_id, agent_id):
        self.job_id = job_id
        self.agent_id = agent_id

   

class PriorityQueueOfJob:

    def __init__(self):

        self.jobslist = []
        self.agentsList = []
        self.job_requests=[]
        self.jobs_assigned=[]
        self.len = 0

    def readJsonFile(self,filename):
        try:
            with open(filename) as json_data:
                dados = json.load(json_data)
                return dados
        except Exception as  error:
            print(error)
        return None

    def is_file_empty(self,data):
        if data == "":
            return True
        else:
            return False
    
    def job_exists(self,job_id,list_jobs):
        
        if list_jobs.find(str(job_id)) == -1:
            return False
        else:
            return True
 
    def generate_output(self,job_id,agent_id):
        priory = PriorityQueueOfJob()
        print("job id %s" %job_id)
        di = {"job_assigned":{"agent_id":agent_id,"job_id":job_id}}
        with open('sample_output2.json','r') as json_file:
            read_data = json_file.read()
            if priory.is_file_empty(read_data) == False:
                
                d = json.loads(read_data)
                if priory.job_exists(job_id,read_data) is True:
                    print(" o job informado já existe ")
                else:
                     d.append(di)
                     priory.write_output(d)
                
            else:
                di = [{"job_assigned":{"agent_id":agent_id,"job_id":job_id}}]
                print(" primeira escrita no arquivo ")
                priory.write_output(di)
            
    def write_output(self,newvalue):
        with open('sample_output2.json','w') as outputfile:
            json.dump(newvalue,outputfile,indent=4)
    
    def assign_job_toUser(self,job, agent):
        print(agent.primary_skillset)
        for i in agent.primary_skillset:
            if i == job.type:
                return True
        for i in agent.secondary_skillset:
            if i == job.type:
                return True
        return False


    def get_agent(self,agent_id):
        agent = ""
        for dados in self.agentsList:
            if dados.id == agent_id:
                agent =  dados
                break
        return agent

    def enqueue(self,job):
        if(self.isJobsEmpty):
            self.jobslist.append(job)
        self.len +=1

    def get_jobs_requests(self):
        data = self.readJsonFile('sample_input.json')
        for i in data:
            for key,value in i.items():
                if key == "job_request":
                    hasJobRequests = True
                    self.job_requests.append(value['agent_id'])

        return self.job_requests

    def dequeue(self):
        hasUrgentJob=False
        for y in self.get_jobs_requests():
            for i in range(self.len):
                if self.jobslist[i].urgent is True:
                    if self.assign_job_toUser(self.jobslist[i],self.get_agent(y)) is True:
                        self.generate_output(self.jobslist[i].id,y)
                        self.jobslist.pop(i)
                        hasUrgentJob = True
                        self.job_requests.pop(0)
                        self.len-=1
                        break
        
            if hasUrgentJob is not True and len(self.jobslist) > 0:
                if self.assign_job_toUser(self.jobslist[0],self.get_agent(y)) is True:
                    self.generate_output(self.jobslist[0].id,y)
                    self.jobslist.pop(0)
                    self.job_requests.pop(0)
                    self.len-=1
                else:
                    print(" o agent informado não pode consumir o job ")

            elif len(self.jobslist) == 0:
                print(" não existem mais jobs a serem consumidos ")
            break
                
    def createAgents(self,agent):
        self.agentsList.append(agent)
        return True

    def isJobsEmpty(self):
        if len == 0:
            return True
        return False

   


            

        
            
        


