#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# import numpy as np
# import glob
# import math
# import random
# import itertools
# import matplotlib.pyplot as plt

# In[2]:


path=r"C:\Users\lenovo\OneDrive\Desktop\new_profile\*.csv"


# In[3]:


# avg_speed of entire driving cycle
avg_speed_list=[]
target="speed"
for fl in glob.glob(path):
    df=pd.read_csv(fl)
    mean_speed=np.mean(df[target])
    avg_speed_list.append(mean_speed)
        

        


# In[4]:


# avg_acceleration and time proportion

sum_acc=0 #adding the desired value of accelereation
sum_dec=0
total_time=0
running_speed=0
    
#  ...................................   
value_acc=0 #for acce time prop.(how many times it occur)
value_dec=0 #for decc time prop.
value_crusing=0
value_ideling=0
value_acc_dec=0
value_creeping=0
value_running_speed=0
# ....................................   

for fl in glob.glob(path):
    df=pd.read_csv(fl) #Will read all csv in given path folder
    acc_1=df.loc[:,["real_acc"]] #locating accl. column
    speed_1=df.loc[:,["speed"]]  #locating speed. column
        
    acc_2=acc_1.to_numpy()
    speed_2=speed_1.to_numpy() #Used to convert an array-like object to a NumPy array.
        
    acc_3=acc_2.flatten()
    speed_3=speed_2.flatten()
        
    length=len(acc_3)
    total_time=total_time+length
# .............................................................        
    for i in range(length):
        if acc_3[i]>0.1 and speed_3[i]>5.0:
            sum_acc+=acc_3[i]
            value_acc+=1
                
        elif acc_3[i]<-0.1 and speed_3[i]>5.0:
            sum_dec+=acc_3[i]
            value_dec+=1
                
        elif acc_3[i]>-0.1 and acc_3[i]<0.1 and speed_3[i]>5.0:
            value_crusing+=1
                
        elif speed_3[i]==0:
            value_ideling+=1
                
        elif speed_3[i]<5.0:
            value_creeping+=1
                
        elif speed_3[i]>0:
            running_speed+=speed_3[i] # adding all values except ideling
            value_running_speed+=1
# ..........                            #......................
    for i in range (length-1):
        if acc_3[i]>0.1 and acc_3[i+1]<-0.1 and speed_3[i]>5.0:
            value_acc_dec+=1
# .............................................................
avg_acceleration= sum_acc/value_acc
avg_decceleration=sum_dec/value_dec
avg_running_speed=running_speed/value_running_speed
# ..............................................................
# occurence of that particular target parameter..
percentage=[]
percentage.append((value_acc/total_time)*100)
percentage.append((value_dec/total_time)*100)
percentage.append((value_crusing/total_time)*100)
percentage.append((value_ideling/total_time)*100)
percentage.append((value_creeping/total_time)*100)
percentage.append((value_running_speed/total_time)*100)

#     return avg_running_speed--> takes value only when vehicle speed>0 i.e vehicle is moving
#     return avg_acceleration
#     return avg_acceleration
#     return value_acc_dec
#     return percentage

    
    
    
        


# In[5]:


# RMS acceleeation and positive kinetic energy for particle

sum_acc_rms=0
sum_kinetic=0
total_time=0

for fl in glob.glob(path):
    df=pd.read_csv(fl)

    acc_1=df.loc[:,["real_acc"]]
    speed_1=df.loc[:,["speed"]]

    acc_2=acc_1.to_numpy()
    speed_2=speed_1.to_numpy()

    acc_3=acc_2.flatten()
    speed_3=speed_2.flatten()

    l=len(acc_2)
    total_time+=l

    for i in range(l):
        sum_acc_rms+=acc_3[i]**2
        sum_kinetic+=speed_3[i]**2

    avg_rms=math.sqrt(sum_acc_rms/total_time)
    avg_PKE=0.5*(sum_kinetic/total_time)

#     return avg_rms
#     return avg_PKE

    
    


# In[6]:


print("average_speed: ",np.mean(avg_speed_list))
print("avg_run_speed: ", avg_running_speed,end="\n")
print("avg_acc: ", avg_acceleration,end="\n")
print("avg_decc: ", avg_decceleration,end="\n")
print("avg_acc_to_decc ", value_acc_dec,end="\n")
print("percentage: ", percentage,end="\n")
print("avg_rms: ",avg_rms,end="\n")
print("avg_PKE: ",avg_PKE,end="\n")    





# In[7]:


# ...................FUNCTIONS ONLY FOR THE CALCULATION OF PROTOTYPE driving cycle's PARAMETER............................


# In[8]:


# avg speed (take 0 in denominator)
# avg running speed
# avg_acc
# avg_decc
# acc to dcc
# percentage
# avg_RMS
# avg_PKE


# In[9]:


# def calculate_avg_acc(my_list):
    


# In[10]:


def calculate_average_speed(my_list):
    list_sum=sum(my_list)
    list_len=len(my_list)
    average=list_sum/list_len
    return average
    


# In[11]:


def subtraction(my_list):
    final_list=[0]
    for i in range(len(my_list)-1):
        final_list.append(my_list[i+1]-my_list[i])
    return final_list


# In[12]:


# Generating Micro_Trips 
path=r"C:\\Users\\lenovo\\OneDrive\\Desktop\\new_profile\\*.csv"
micro_t=[]
length_time=[]
for fl in glob.glob(path):
    data=pd.read_csv(fl)

    speed_thres=2.50 #in m/s (0--2.5)-->Consider this range as Zero  :)

    speed_1=data.loc[:,["speed"]]
    speed_2=speed_1.to_numpy()
    speed_3=speed_2.flatten()

#   Initializing Min

    mt_st=[]
    mt_end=[]

#    Loop through data to generate Micro Trips...
    for i in range(len(data)-1):
        if (data["speed"][i]<=speed_thres and data["speed"][i+1]>speed_thres):
            mt_st.append(i+1)
        elif (data["speed"][i]>=speed_thres and data["speed"][i+1]<speed_thres):
            mt_end.append(i)
# ..................................
#     DATA MISMATCH..
    if(len(mt_st) != len(mt_end)):
        mt_st.insert(0,0)
#....................................  

# ............INDEX PRINTING.................
#     for i in mt_st:
#         print(data["speed"][i],"Index:",i,"|",end="\t")
#     print("\n...........")
#     for i in mt_end:
#         print(data["speed"][i],"Index:",i,"|",end="\t")
#     print("\n")
# ..............................................
#  Calculating time of each microtrips
    for i in range(len(mt_st)):
        length_time.append(mt_end[i]-mt_st[i])
# ...................................
    for i in range(len(mt_st)):
#         print("Micro_Trip No: ",i+1,end="\n")
#         print(speed_3[mt_st[i]:mt_end[i]:])
        micro_t.append(speed_3[mt_st[i]:mt_end[i]:])
#         print("\n")



# In[13]:


# Creating shuffled list of microtrips 

# step 1: randomly generating 10 files index out of 32 total micro trips..10 files are enough to generate 
# sufficient length of driving cycle..

def merge_lists(list_of_lists):
    merged_list = list(itertools.chain(*list_of_lists))
    return merged_list

merged_prototype_DC=[]
merged_prototype_acc_DC=[]

for i in range(30): #30 prototype driving cycle.
    random_list=random.sample(range(1,33),5)
    print (random_list)
    print("\n")
    count=0
    for j in range(len(random_list)-1):
        if abs ((micro_t[random_list[j]-1][length_time[random_list[j]-1]-1]) - (micro_t[random_list[j+1]-1][length_time[random_list[j+1]-1]-1]) <=0.4):
            count=count+1
    print("count",count,end="\n")
    if (count==len(random_list)-1):
        merged_proto_dc=[]
        for k in random_list:
            merged_proto_dc.append(micro_t[k-1])
            
#         print(merged_proto_dc,end="\n")
        final_merged_list=merge_lists(merged_proto_dc)
#         print(final_merged_list)
        merged_prototype_DC.append(final_merged_list)

print(merged_prototype_DC,end="\n\n")



for i in merged_prototype_DC:
    temp=subtraction(i)
    merged_prototype_acc_DC.append(temp)
print(merged_prototype_acc_DC,end="\n")  


# In[14]:


# avg speed (take 0 in denominator)--DONE
# avg running speed--NOT POSSIBLE
# avg_acc
# avg_decc
# acc to dcc
# percentage
# avg_RMS
# avg_PKE


# In[26]:


average_speed_dc=[]

for i in merged_prototype_DC:
    avg_sp_dc=calculate_average_speed(i)
    average_speed_dc.append(avg_sp_dc)
print("average speed of dc: ",average_speed_dc,end="\n")


# In[27]:


acc_made_dc=[]
decc_made_dc=[]
value_acc_to_decc_dc=0

for i in range(len(merged_prototype_DC)):
    sum_1=0
    value_1=0
    sum_2=0
    value_2=0
    for j in range(len(merged_prototype_DC[i])):
        if(merged_prototype_acc_DC[i][j]>0.1 and merged_prototype_DC[i][j]>5.0):
            sum_1=sum_1+merged_prototype_acc_DC[i][j]
            value_1=value_1+1
        elif (merged_prototype_acc_DC[i][j]<-0.1 and merged_prototype_DC[i][j]>5.0):
            sum_2+=merged_prototype_acc_DC[i][j]
            value_2+=1
            
            
    acc_made_dc.append(sum_1/value_1)
    decc_made_dc.append(sum_2/value_2)

for i in range(len(merged_prototype_DC)):
    for j in range(len(merged_prototype_DC[i])-1):
        if(merged_prototype_acc_DC[i][j]>0.1 and merged_prototype_acc_DC[i][j+1]<-0.1 and merged_prototype_DC[i]>5.0):
            value_acc_to_decc_dc+=1

print("Acceleration of dc: ",acc_made_dc,end="\n\n")
print("Deceleration of dc: ",decc_made_dc,end="\n")
# print(value_acc_to_decc_dc,end="\n")


# In[17]:


rms_dc_list=[]
pke_dc_list=[]
# RMS
for i in range(len(merged_prototype_acc_DC)):
    rms_dc=0
    for j in range(len(merged_prototype_acc_DC[i])): 
        rms_dc+=merged_prototype_acc_DC[i][j]**2
    rms_dc_list.append(math.sqrt(rms_dc/len(merged_prototype_acc_DC[i])))

# pke
for i in range(len(merged_prototype_DC)):
    pke_dc=0
    for j in range(len(merged_prototype_DC[i])): 
        pke_dc+=merged_prototype_DC[i][j]**2
    pke_dc_list.append(0.5*(pke_dc/len(merged_prototype_DC[i])))
print("rms list of dc ", rms_dc_list,end="\n\n")
print("pke list of dc ", pke_dc_list,end="\n\n")


# In[18]:


comparison=[]
for i in range(len(average_speed_dc)):
    value_1=abs((np.mean(avg_speed_list)-average_speed_dc[i]))
    value_2=abs(avg_acceleration-acc_made_dc[i])
    value_3=abs(avg_decceleration-decc_made_dc[i])
    value_4=abs(avg_rms-rms_dc_list[i])
    value_5=abs(avg_PKE-pke_dc_list[i])
    
    comparison.append(value_1+value_2+value_3+value_4+value_5)
minimum_index=comparison.index(min(comparison))
print(comparison,end="\n")
print(minimum_index,end="\n")


# In[19]:


print("original_DC_Average speed: ",np.mean(avg_speed_list),"m/s ",
      "| Made_DC_Average speed: ",average_speed_dc[minimum_index],"m/s",end="\n\n")

print("Made_DRIVING CYCLE_Total Time: ",len(merged_prototype_DC[minimum_index]),"sec",end="\n")

print("orginal_average_acc: ",avg_acceleration,"m^2/s",
      "| Made_DC_average_acc: ",acc_made_dc[minimum_index],"m^2/s",end="\n\n")

print("orginal_average_decc: ",avg_decceleration,"m^2/s",
      "| Made_DC_average_decc: ",decc_made_dc[minimum_index],"m^2/s",end="\n\n")

print("orginal_average_rms: ",avg_rms,"m^2/s",
      "| Made_DC_average_rms: ",rms_dc_list[minimum_index],"m^2/s",end="\n\n")

print("orginal_average_PKE: ",avg_PKE,"kg.(m^2/s^2)",
      "| Made_DC_average_pke: ",pke_dc_list[minimum_index],"kg.(m^2/s^2)",end="\n\n")


# In[20]:


time_list=[]
for i in range(len(merged_prototype_DC[minimum_index])):
    time_list.append(i)
    
x = time_list
y = merged_prototype_DC[minimum_index]

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set_xlabel('Time (sec)')
ax.set_ylabel('Speed (m/s)')
ax.set_title('Driving Cycle')

plt.show()

