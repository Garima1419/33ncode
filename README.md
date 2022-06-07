# 33ncode
Description: For Job position at 33n

Note: The data in CSV files- Events and Diagnosis are not up to the standard. Below mentioned flags raise the issue regarding the data quality and reliability.

Flag-1: Both files contained some null values. In the Events table, the 'EventID' column cannot be null as it is the unique key for every patient. In the Diagnosis table, the 'Diagnosis' column contained null entries. For the coding purpose, I dropped all such null values.

Flag-2: In the Events table, for the same EventID two different entries are found. For better data integration, I purposefully removed EventID with the older date.

Flag-3: In the Diagnosis table, the data contained duplicate records. For the coding purpose, such records are dropped to avoid data redundancy.

Flag-4: One weird data entry is found in Diagnosis table, with no pre-records available in Event table. The EventID is 'ed7f9b79-e1e1-432e-a4f8-5282286dacac'.

Comment: For EventIDs ('2971b0ea-df0d-4765-ab3c-956a40e1d969', 'd46d4595-b417-462b-aa7f-f02ffbf0b798') with no records present in Diagnosis table, the new column ‘MostRecentDiagnosis’ contains value ‘No recent diagnosis’.

