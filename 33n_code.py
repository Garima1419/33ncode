#!/usr/bin/env python
# coding: utf-8

# In[131]:


# Importing necessary library- pandas
import pandas as pd

Event_data_raw = pd.read_csv('events.csv', header=0)
Event_data_raw['EventDateTime']= pd.to_datetime(Event_data_raw['EventDateTime'])

# Flag-2: Not considering first row as it contains old date for EventID: '223f3ffa-15e4-4b29-a328-488369b8c127'
Event_data = Event_data_raw[1:7]

# Flag-1: Dropping row wih NaN EventID
Event_data = Event_data.dropna(subset=['EventID'])

# Final Events table
Event_data


# In[139]:


Diagnosis_data_raw = pd.read_csv('diagnoses.csv', header=0)
Diagnosis_data_raw['DiagnosisDateTime']= pd.to_datetime(Diagnosis_data_raw['DiagnosisDateTime'])

# Flag-3: Dropping duplicate row
Diagnosis_data = Diagnosis_data_raw.drop_duplicates()

# Flag-1: Dropping row wih NaN Diagnosis values
Diagnosis_data = Diagnosis_data.dropna()

# Final Diagnosis table
Diagnosis_data


# In[135]:


# Method to fetch index values for the most recent diagnosis after a particular event

def ref(df1, df2):
    index = []
    for i in df1.index:
        event_pre_id = df1['EventID'][i]
        index1 = []
        distance = []
        for j in df2.index:
            event_late_id = df2['EventID'][j]
            if event_late_id == event_pre_id:
                if (df2['DiagnosisDateTime'][j] > df1['EventDateTime'][i]):
                    dis = df2['DiagnosisDateTime'][j]-df1['EventDateTime'][i]
                    distance.append(dis)
                    index1.append(j)
        if len(distance) != 0:
            min_dis = distance.index(min(distance))
            index_need = index1[min_dis]
            index.append(index_need)
    return index


# In[136]:


index = ref(Event_data,Diagnosis_data)
Event_data['MostRecentDiagnosis'] = 'No recent diagnosis'
for i in index:
    for j in Event_data.index:
        if Event_data['EventID'][j]== Diagnosis_data.loc[i, 'EventID']:
            Event_data['MostRecentDiagnosis'][j] = Diagnosis_data.loc[i, 'Diagnosis']
Event_data


# In[ ]:




