# 33ncode
Description: For Job position at 33n

Note: The data in CSV files- Events and Diagnosis are not up to the standard. Below mentioned flags raise the issue regarding the data quality and reliability.

Flag-1: Both files contained some null values. In the Events table, the 'EventID' column cannot be null as it is the unique key for every patient. In the Diagnosis table, the 'Diagnosis' column contained null entries. For the coding purpose, I dropped all such null values.

Flag-2: In the Diagnosis table, the data contained duplicate records. For the coding purpose, such records are dropped to avoid data redundancy.

Flag-3: Two foreign data entry are found in Diagnosis table, where details for two events were mentioned but they got no pre records in Events table. Those EventIDs are: '2971b0ea-df0d-4765-ab3c-956a40e1d969', 'd46d4595-b417-462b-aa7f-f02ffbf0b798'
