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
    mu = 0
    sfQ = []
    sfR = []
    mu = mu0 + (g*b)
    tlist.append(0)
    qCustNumber.append(len(qcust_list))
    qCustTotNumber.append(len(qcust_total))
    qServNumber.append(len(qserv_list))
    qDpNumber.append(len(qdp_list))
    #qDpSuccessNumber.append(qDpSuccess)
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
                #qDpSuccessNumber.append(qDpSuccess)
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
                            #qDpSuccessNumber.append(qDpSuccess)
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
                            #qDpSuccessNumber.append(qDpSuccess)                       
                            qDNumber.append(len(qdonor_list))
                            qCustNumber.append(len(qcust_list))
                            qServNumber.append(len(qserv_list))
                            qDpTotNumber.append(len(qdp_total))
                
                        elif (len(qcust_list)!=0 and len(qdp_list)==0):
                            t=t+a_serv
                            tlist.append(t)
                            qdonor_list.append(newServ)
                            qcust_list.pop(0)
                            #if removeCust in qdp_list:
                               # qDpSuccess = qDpSuccess+1
                             #   qdp_list.remove(removeCust)
                            qCustTotNumber.append(len(qcust_total))
                            qDpNumber.append(len(qdp_list))
                            #qDpSuccessNumber.append(qDpSuccess)                       
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
                            #qDpSuccessNumber.append(qDpSuccess)                       
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
                        #qDpSuccessNumber.append(qDpSuccess)                       
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
                    #qDpSuccessNumber.append(qDpSuccess)                       
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
                    #qDpSuccessNumber.append(qDpSuccess)                       
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
                    #qDpSuccessNumber.append(qDpSuccess)                       
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
                        #qDpSuccessNumber.append(qDpSuccess)                       
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
                        #qDpSuccessNumber.append(qDpSuccess)                       
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
                    #qDpSuccessNumber.append(qDpSuccess)                       
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
                    #qDpSuccessNumber.append(qDpSuccess)                       
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
    while (d < len(fR)):
        b= float(math.fsum(fR[d]))
        sfR.append(float(b))
        d+=1
            
    nQ=range(0,max(qCust)+1)
    nR=range(0,max(qDp)+1)   
    
    return [nQ,sfQ,nR,sfR, tlist, qCustNumber, qDpNumber, qDNumber]
    
    '''t_array=np.array(tlist)
    qcust_array=np.array(qCustNumber)
    qserver_array=np.array(qServNumber)
    qDp_array = np.array(qDpNumber)
    qD_array = np.array(qDNumber)
    qDpSuccess_array = np.array(qDpSuccessNumber)
    Eqcustot_array = np.array(qCustTotNumber)
    qDptot_array = np.array(qDpTotNumber)
    sfR_array = np.array(sfR)
    nR_array = np.array(nR)
    sfQ_array = np.array(sfQ)
    nQ_array = np.array(nQ)

    zipper = lambda nQ,sfQ : [list(b) for b in zip(nQ,sfQ)]
    zipped_array = zipper(nQ_array, sfQ_array)
    zipper1 = lambda nR,sfR : [list(b) for b in zip(nR,sfR)]
    zipped_array1 = zipper1(nR_array, sfR_array)
    zipper1 = lambda t, qc, qs, qDp, qD, qct, qdpt : [list(c) for c in zip(t, qc, qs, qDp, qD, qct, qdpt)]
    zipped_array1 = zipper1(t_array,qcust_array,qserver_array, qDp_array, qD_array, qcustot_array, qDptot_array)
    
    np.savetxt('zippppppped', zipped_array1, delimiter='\t')
    #np.savetxt('zipped_array11', zipped_array1, delimiter='\t') '''

def event_sim1(niter,lambd,mu0,eta,b, g, p,time):    
    fQ =[]    
    fR =[]    
    nR=[]
    nQ=[]    
    y=0
    tlist=0
    qCustNo = 0
    qDpNo = 0
    qDNo = 0
    sim1 = event_sim(lambd, mu0, eta, b,g,p,time)
    tlist=sim1[4]
    qCustNo=sim1[5]
    qDpNo=sim1[6]
    qDNo=sim1[7]
    
    while (y < niter):
        fQ.append([])
        fR.append([])
        nR.append([])
        nQ.append([])
        y=y+1
    
    i=0    
    while i < niter:
        sim = event_sim(lambd, mu0, eta, b,g,p,time)
        nQ[i]=sim[0]
        fQ[i]=sim[1]
        nR[i]=sim[2]
        fR[i]=sim[3]    
        i+=1
        
    k=0    
    sfQ=[float(sum(k))/len(k) for k in zip(*fQ)]
    k=0
    sfR=[float(sum(k))/len(k) for k in zip(*fR)]
    
    minQ = min(nQ, key=len)
    minR = min(nR, key=len)
    nQ_array = np.array(minQ)
    sfQ_array = np.array(sfQ)
    nR_array = np.array(minR)
    sfR_array = np.array(sfR)
    t_array=np.array(tlist)
    qcust_array=np.array(qCustNo)
    qDp_array = np.array(qDpNo)
    qD_array = np.array(qDNo)
    zipper = lambda minQ,sfQ,minR,sfR : [list(v) for v in zip(minQ,sfQ,minR,sfR)]
    zipped_array = zipper(nQ_array,sfQ_array,nR_array,sfR_array)
    np.savetxt('Histogram', zipped_array, delimiter='\t')
    
    zipper1 = lambda t, qc,qDp, qD : [list(c) for c in zip(t, qc, qDp, qD)]
    zipped_array1 = zipper1(t_array,qcust_array, qDp_array, qD_array)
    np.savetxt('zippppppped', zipped_array1, delimiter='\t')
   
#event_sim1(1000,1,1,0.5,5,0.7,0.3,1000)
