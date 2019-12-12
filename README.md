# Big Data Final Project


## Task2
**Note that**
1. ***stanford-ner-2018-10-16*** is the dictionary that contains trained model and classifier developed by **Stanford CoreNLP**. In this task, we use this model to predict **person_name**<br>
   **Note that:** In order to use this in the **task2.py**. You **should** make sure that this folder and **task2.py** are in the same path.
2. Also, the txt files and **dataset.csv** are resources referenced by **task2.py**. **Make sure** that these auxiliary files and **task2.py** are in the same folder.

### To Run

1. `cd ../task2`<br>
**change the dictionary to task2 and Run the code below**<br>
2. ```spark-submit --conf spark.pyspark.python=/share/apps/python/3.6.5/bin/python task2.py```<br>
**After successful processing, a dictionary named 'final_data' will be made. The final result JSON file will be saved into ot**<br>
Note that: If *final_data* exists already, please remove it before run the code