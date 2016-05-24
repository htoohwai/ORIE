import numpy as np
import random
import math

def entryGenerator(identity, arrival):
    return [identity, arrival]

def event_sim(lambd,mu0,eta,b, g, p,time):     #p = probability , i = priority

    a_cust=0
    a_serv=0
    a_leave = 0
    
    removeDP = 0
    
    t=0
    mu = 0
    probability = 0
    probability1 = 0

    tlist = []
    qcust_list = []
    qcust_total = []
    qserv_list = []
    qdonor_list = []
    qDNumber = [] #number of donor list
    qdp_list = []     #donor becomes patient list
    qdp_total = []
    qCustNumber = []
    qCustTotNumber = []
    qServNumber = []
    qDpNumber = []   #number of donor who becomes patient
    qDpTotNumber = []
    
    ERlist = []
    ExpectedR= 0
    EQlist = []
    ExpectedQ = 0
    
    sfQ = []
    nQ =[]
    sfR = []
    nR = []
   
    mu = mu0 + (g*b)
    tlist.append(0)
    qCustNumber.append(len(qcust_list))
    qCustTotNumber.append(len(qcust_total))
    qServNumber.append(len(qserv_list))
    qDpNumber.append(len(qdp_list))
    qDNumber.append(len(qdonor_list))
    qDpTotNumber.append(len(qdp_total))
    
    while t<time:
        
        if (len(qdonor_list)==0):
            if (len(qcust_list)==0 and len(qdp_list)==0):
                a_cust = random.expovariate(lambd)
                newCust = entryGenerator('c',a_cust)
                t = t+a_cust
                tlist.append(t)
                if (len(qserv_list)==0):
                    qcust_list.append(newCust)
                    qcust_total.append(newCust)
                    
                qCustNumber.append(len(qcust_list))
                qCustTotNumber.append(len(qcust_total))
                qServNumber.append(len(qserv_list))
                qDpNumber.append(len(qdp_list))
                qDNumber.append(len(qdonor_list))
                qDpTotNumber.append(len(qdp_total))
            else:
                a_cust = random.expovariate(lambd)
                a_serv = random.expovariate(mu)
                newCust = entryGenerator('c', a_cust)
                newServ = entryGenerator('s', a_serv)
                if (len(qdonor_list)==0):
                    if a_serv>a_cust:
                        t = t+a_cust
                        tlist.append(t)
                        if (len(qserv_list)==0):
                            qcust_list.append(newCust)
                            qcust_total.append(newCust)
                             
                            qCustNumber.append(len(qcust_list))
                            qCustTotNumber.append(len(qcust_total))
                            qServNumber.append(len(qserv_list))
                            qDpNumber.append(len(qdp_list))
                            qDNumber.append(len(qdonor_list))
                            qDpTotNumber.append(len(qdp_total))
            
                    elif a_cust > a_serv:
                        if (len(qcust_list)==0 and len(qdp_list)!=0):
                            t=t+a_serv
                            tlist.append(t)
                            qdonor_list.append(newServ)
                            removeDP = qdp_list.pop(0)
                    
                            qCustTotNumber.append(len(qcust_total))
                            qDpNumber.append(len(qdp_list))
                            qDNumber.append(len(qdonor_list))
                            qCustNumber.append(len(qcust_list))
                            qServNumber.append(len(qserv_list))
                            qDpTotNumber.append(len(qdp_total))
                
                        elif (len(qcust_list)!=0 and len(qdp_list)==0):
                            t=t+a_serv
                            tlist.append(t)
                            qdonor_list.append(newServ)
                            qcust_list.pop(0)
                            
                            qCustTotNumber.append(len(qcust_total))
                            qDpNumber.append(len(qdp_list))
                            qDNumber.append(len(qdonor_list))
                            qCustNumber.append(len(qcust_list))
                            qServNumber.append(len(qserv_list))
                            qDpTotNumber.append(len(qdp_total))
                     
                        elif (len(qcust_list)!=0 and len(qdp_list)!=0):
                            t=t+a_serv
                            tlist.append(t)
                            qdonor_list.append(newServ)
                            gamma =np.random.random()
                            if (gamma < g):
                                removeDP = qdp_list.pop(0)
                            elif (gamma >= g):
                                qcust_list.pop(0)
                                
                            qCustTotNumber.append(len(qcust_total))
                            qDpNumber.append(len(qdp_list))
                            qDNumber.append(len(qdonor_list))
                            qCustNumber.append(len(qcust_list))
                            qServNumber.append(len(qserv_list))
                            qDpTotNumber.append(len(qdp_total))        
                
    
        #simulate probability 
        elif (len(qdonor_list)!=0):
            
            if (len(qcust_list)==0 and len(qdp_list)==0):
                probability = np.random.random()
            
                if (probability < (lambd /(lambd+(len(qdonor_list)*eta)))):
                    a_cust = random.expovariate(lambd+(len(qdonor_list)*eta))
                    t=t+a_cust
                    newCust = entryGenerator('c',a_cust)
                    tlist.append(t)
                    if (len(qserv_list)==0):
                        qcust_total.append(newCust)
                        qcust_list.append(newCust)
                
                        qCustTotNumber.append(len(qcust_total))
                        qDpNumber.append(len(qdp_list))
                        qDNumber.append(len(qdonor_list))
                        qCustNumber.append(len(qcust_list))
                        qServNumber.append(len(qserv_list))
                        qDpTotNumber.append(len(qdp_total)) 
                    
            
                elif (probability < ((lambd+p*(len(qdonor_list)*eta))/(lambd+(len(qdonor_list)*eta)))):
                    a_leave = random.expovariate(lambd+(len(qdonor_list)*eta))
                    t=t+a_leave
                    tlist.append(t)
                    x = random.randint(0,len(qdonor_list)-1)
                    qdonor_list.pop(x)
             
                    qDpNumber.append(len(qdp_list))
                    qDNumber.append(len(qdonor_list))
                    qCustNumber.append(len(qcust_list))
                    qServNumber.append(len(qserv_list))
                    qCustTotNumber.append(len(qcust_total))
                    qDpTotNumber.append(len(qdp_total))
                
                elif (probability >= ((lambd+p*(len(qdonor_list)*eta))/(lambd+(len(qdonor_list)*eta)))):
                    a_leave = random.expovariate(lambd+(len(qdonor_list)*eta))
                    t=t+a_leave
                    tlist.append(t)
                    x = random.randint(0,len(qdonor_list)-1)
                    removeDP = qdonor_list.pop(x)
                    qdp_list.append(removeDP)
                    qdp_total.append(removeDP)
                
                    qDpNumber.append(len(qdp_list))
                    qDNumber.append(len(qdonor_list))
                    qCustNumber.append(len(qcust_list))
                    qServNumber.append(len(qserv_list))
                    qCustTotNumber.append(len(qcust_total))
                    qDpTotNumber.append(len(qdp_total))    
            
            else:
            
                probability1 = np.random.random()
            
                if (probability1 < (lambd /(lambd+mu+(len(qdonor_list)*eta)))):
                    a_cust = random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                    t=t+a_cust
                    tlist.append(t)
                    newCust = entryGenerator('c',a_cust)
                    if (len(qserv_list)==0):
                        qcust_total.append(newCust)
                        qcust_list.append(newCust)
                
                    qCustTotNumber.append(len(qcust_total))
                    qDpNumber.append(len(qdp_list))
                    qDNumber.append(len(qdonor_list))
                    qCustNumber.append(len(qcust_list))
                    qServNumber.append(len(qserv_list))
                    qDpTotNumber.append(len(qdp_total)) 
                
                elif (probability1 < ((mu+lambd)/(lambd+mu+(len(qdonor_list)*eta)))):
                    
                    if (len(qcust_list)==0 and len(qdp_list)!=0):
                        a_serv = random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                        newServ = entryGenerator('s',a_serv)
                        t=t+a_serv
                        tlist.append(t)
                        qdonor_list.append(newServ)
                        removeDP = qdp_list.pop(0)
                    
                        qCustTotNumber.append(len(qcust_total))
                        qDpNumber.append(len(qdp_list))
                        qDNumber.append(len(qdonor_list))
                        qCustNumber.append(len(qcust_list))
                        qServNumber.append(len(qserv_list))
                        qDpTotNumber.append(len(qdp_total))
                
                    elif (len(qcust_list)!=0 and len(qdp_list)==0):
                        a_serv = random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                        newServ = entryGenerator('s',a_serv)
                        t=t+a_serv
                        tlist.append(t)
                        qdonor_list.append(newServ)
                        qcust_list.pop(0)
                        
                        qCustTotNumber.append(len(qcust_total))
                        qDpNumber.append(len(qdp_list))
                        qDNumber.append(len(qdonor_list))
                        qCustNumber.append(len(qcust_list))
                        qServNumber.append(len(qserv_list))
                        qDpTotNumber.append(len(qdp_total))
                     
                    elif (len(qcust_list)!=0 and len(qdp_list)!=0):
                        a_serv = random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                        newServ = entryGenerator('s',a_serv)
                        t=t+a_serv
                        tlist.append(t)
                        qdonor_list.append(newServ)
                        gamma =np.random.random()
                        if (gamma < g):
                            removeDP = qdp_list.pop(0)
                        elif (gamma >= g):
                            qcust_list.pop(0)
                    
                        qCustTotNumber.append(len(qcust_total))
                        qDpNumber.append(len(qdp_list))
                        qDNumber.append(len(qdonor_list))
                        qCustNumber.append(len(qcust_list))
                        qServNumber.append(len(qserv_list))
                        qDpTotNumber.append(len(qdp_total))        
                
                elif (probability1 < ((mu+lambd+p*(len(qdonor_list)*eta))/(lambd+mu+(len(qdonor_list)*eta)))):
                    t=t+random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                    tlist.append(t)
                    x = random.randint(0,len(qdonor_list)-1)
                    qdonor_list.pop(x)
             
                    qDpNumber.append(len(qdp_list))
                    qDNumber.append(len(qdonor_list))
                    qCustNumber.append(len(qcust_list))
                    qServNumber.append(len(qserv_list))
                    qCustTotNumber.append(len(qcust_total))
                    qDpTotNumber.append(len(qdp_total))
                
                elif (probability1 >= ((mu+lambd+p*(len(qdonor_list)*eta))/(lambd+mu+(len(qdonor_list)*eta)))):
                    t=t+random.expovariate(lambd+mu+(len(qdonor_list)*eta))
                    tlist.append(t)
                    x = random.randint(0,len(qdonor_list)-1)
                    removeDP = qdonor_list.pop(x)
                    qdp_list.append(removeDP)
                    qdp_total.append(removeDP)
                
                    qDpNumber.append(len(qdp_list))
                    qDNumber.append(len(qdonor_list))
                    qCustNumber.append(len(qcust_list))
                    qServNumber.append(len(qserv_list))
                    qCustTotNumber.append(len(qcust_total))
                    qDpTotNumber.append(len(qdp_total))    
    
    qCust = qCustNumber[:]
    qCust.pop(len(qCust)-1)
    fQ = []
    y=0
    while (y <= max(qCust)):
        fQ.append([])
        y=y+1
    
    z=0
    while z <= max(qCust):
        e=0
        while e <len(qCust):
            if z == qCust[e]:
                fQ[z].append((float(tlist[e+1]-tlist[e])/float(tlist[len(tlist)-1])))
            e += 1
        if len(fQ[z]) == 0:
            fQ[z].append(0)
        z+=1    
    
    d=0 
    x=0
    while (d < len(fQ)):
        x= float(math.fsum(fQ[d]))
        sfQ.append(float(x))
        d+=1
        
    n=range(0,max(qCust)+1)
    EQlist = (np.ones(len(n))*n*sfQ).tolist()
    ExpectedQ = math.fsum(EQlist)
    
    
    qDp = qDpNumber[:]
    qDp.pop(len(qDp)-1)
    fR = []
    y=0
    while (y <= max(qDp)):
        fR.append([])
        y=y+1
    
    z=0
    while z <= max(qDp):
        e=0
        while e <len(qDp):
            if z == qDp[e]:
                fR[z].append((float(tlist[e+1]-tlist[e])/float(tlist[len(tlist)-1])))
            e += 1
        if len(fR[z]) == 0:
            fR[z].append(0)
        z+=1    
    d=0    
    e=0
    while (d < len(fR)):
        e= float(math.fsum(fR[d]))
        sfR.append(float(e))
        d+=1
        
    nQ=range(0,max(qCust)+1)
    EQlist = (np.ones(len(nQ))*nQ*sfQ).tolist()
    ExpectedQ = math.fsum(EQlist)
    
    nR=range(0,max(qDp)+1)
    ERlist = (np.ones(len(nR))*nR*sfR).tolist()
    ExpectedR = math.fsum(ERlist)    

    return [ExpectedQ, ExpectedR]
    

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def event_sim2(lambd,mu0,eta,b,p,time):     #p = probability , i = priority

    eQ=[]
    eR=[]
    valueQ = 0
    valueR = 0
    seq = [float(x)/100 for x in range(101)]
    j=0
    for j in frange(0.0, 1.01, 0.01):
        sim = event_sim(lambd,mu0,eta,b, j, p,time)
        valueQ = sim[0]
        valueR = sim[1]
        eQ.append(valueQ)
        eR.append(valueR)

    return [seq,eQ,eR]
 
def event_sim3(niter,lambd,mu0,eta,b,p,time):
    eeQ = []
    eeR =[]    
    y=0
    while (y < niter):
        eeQ.append([])
        eeR.append([])
        y=y+1    
    sq = [float(x)/100 for x in range(101)]
    
    i=0
    while i < niter:    
        sim1 = event_sim2(lambd, mu0, eta, b,p,time)
        eeQ[i] =sim1[1]
        eeR[i] = sim1[2]
        i +=1
    
    seQ=[float(sum(k))/len(k) for k in zip(*eeQ)]
    seR=[float(sum(k))/len(k) for k in zip(*eeR)]

    gamma= np.array(sq)    
    seQ_array = np.array(seQ)
    seR_array = np.array(seR)
    zipper = lambda g,seq,ser : [list(v) for v in zip(g,seq,ser)]
    zipped_array = zipper(gamma, seQ_array,seR_array)
    np.savetxt('zipped_array', zipped_array, delimiter='\t')
     
event_sim3(500,1,1,1,2,0.3,1000)
