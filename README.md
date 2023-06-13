## Technical task

In this replication package, I make available the different scripts needed to fully replicate the results obtained in the slides.

## Content description 
- The ``code`` folder: 
		-  ``question_1.py``, ``question_2.py``, ``question_3.py``, ``question_4.py``, ``question_5.py``, ``question_6.py`` python code to answer the different questions.
						
- dataset: 
	- ``On_Time_On_Time_Performance_2017_1.csv`` the original data downloaded from (https://data.world/hoytick/2017-jan-ontimeflightdata-usa)
	- ``get_data.py`` python script to selecte needed columns and randomly select a sample of 100 rows to work on. 
	- ``data_100_sample.csv`` the ouput file resulted after running ``get_data.py``

- ``makefile``: file used to run different scripts
- ``q1.sh``,``q2.sh``, ``q3.sh``, ``q4.sh``, ``q5.sh``, and ``q6.sh``: script to get the results of different questions
- ``codepath.sh``: used to specify the path to the source code
- `requirement.txt`: file listing all the python packages needed to run experiments


## Prerequisites

- Python3


## Steps

1. To be able to run the code you need to install different python packages presented in the file "requirements.txt ". 
```bash
pip install -r requirements.txt
```
2. To be able to get the sbset of data I used to solve the task, you need to run the python file ``./dataset/get_data.py``
```bash
cd dataset
python get_data.py
```
3. To get the results of all questions, you need to run the makefile 
```bash
make 
```
4. If you want to run only a specific script, you can run it by typing Make and the specified script name (q1, q2, q3, etc.)
```bash
make  q1
```










