# Machine Predictive Maintenance for Industrial Machines

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-blue?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
![Shell Script](https://img.shields.io/badge/Bash-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


[![Kaggle Dataset](https://img.shields.io/badge/Kaggle_Dataset-link-blue?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)

[![Docker image](https://img.shields.io/badge/Docker_image-Link-blue?style=for-the-badge&logo=docker&logoColor=%230db7ed.svg)](https://hub.docker.com/r/dharmikjethva/edgeadmin)




## About

Predictive maintenance (PdM) is a maintenance strategy that uses data analysis to predict when a machine or equipment is likely to fail. This allows for preventive maintenance to be performed before the failure occurs, avoiding costly downtime and repairs. By combining PdM with ML, it is possible to develop models that can accurately predict machine failures days, weeks, or even months in advance. This allows organizations to schedule preventive maintenance at the most opportune time, minimizing downtime and maximizing uptime.


## Download Repository

## Set directory

## Create virtual environment

## Activate virtual environment

## Install requirements

## Train

Run `train.py` this will train the model and save the models into `models` folder

## Test

Run `test.py` to verify saved models work well

## App

Run web app

# Setup

You can run above commands one by one or you can use `setup/setup.sh` for linux or `setup/setup.bat` for windows. You should modify the code in setup.sh or setup.bat file for your cases. And then run this one file this will download repository, change directory, creating virtual environment, activating virtual environment, upgrading pip, installing requirements, training the model, testing the model, opening Flask App.

> Once you run `setup` file, then don't run again to open flask app. Just run `run/run.bat` for windows or `.run/run.sh` for linux or you can activate `.venv` manually and run `app.py`.

Download `setup` file and modify it according to your needs and run this.

## Windows

```
D:\test>dir
setup.bat

D:\test>setup.bat
"Git Cloning..."
Cloning into 'feynn-labs'...
...
...
```

## Linux

```
adhiban@DESKTOP:/test$ ls
setup.sh
adhiban@DESKTOP:/test$ bash setup.sh
Git Cloning...
Cloning into 'feynn-labs'...
...
...
```

Dark mode:

![images/Screenshot4.png](images/Screenshot4.png)

Light mode:

![images/Screenshot5.png](images/Screenshot5.png)

# Input Data

```python
>>> df = pd.read_csv('predictive_maintenance.csv')
>>> df.head()
   UDI Product ID Type  Air temperature [K]  ...  Torque [Nm]  Tool wear [min]  Target  Failure Type
0    1     M14860    M                298.1  ...         42.8                0       0    No Failure
1    2     L47181    L                298.2  ...         46.3                3       0    No Failure
2    3     L47182    L                298.1  ...         49.4                5       0    No Failure
3    4     L47183    L                298.2  ...         39.5                7       0    No Failure
4    5     L47184    L                298.2  ...         40.0                9       0    No Failure

[5 rows x 10 columns]
>>> df.columns
Index(['UDI', 'Product ID', 'Type', 'Air temperature [K]',
       'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
       'Tool wear [min]', 'Target', 'Failure Type'],
      dtype='object')
```

# Output Data

```python
>>> output = pd.read_csv('output.csv')
>>> output.head()
   UDI Product ID Type  ...  Failure Type  is_failure  failure_type
0    1     M14860    M  ...    No Failure           0    No Failure
1    2     L47181    L  ...    No Failure           0    No Failure
2    3     L47182    L  ...    No Failure           0    No Failure
3    4     L47183    L  ...    No Failure           0    No Failure
4    5     L47184    L  ...    No Failure           0    No Failure

[5 rows x 12 columns]
>>> output.columns
Index(['UDI', 'Product ID', 'Type', 'Air temperature [K]',
       'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
       'Tool wear [min]', 'Target', 'Failure Type', 'is_failure',
       'failure_type'],
      dtype='object')
```

Here `failure_type`, `is_failure` columns are added in `output.csv`

> I give the same training dataset to the Flask app to check whether it predicts correct or not. Thats why `Target`, `Failure Type` and other columns are displayed in the terminal output.

# Docker

[![Docker image](https://img.shields.io/badge/Docker_image-Link-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=%230db7ed.svg)](https://hub.docker.com/r/dharmikjethva/edgeadmin)

## Docker pull

## Docker run

Open it in browser `http://127.0.0.1:5000/`

> [!NOTE] *This Django project is in Debug=True mode*
