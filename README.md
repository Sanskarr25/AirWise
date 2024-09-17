<h1>AirWise - Predict Air Quality Index</h1>

###

<p align="left">Airwise is a Webapp to Predict Air Quality Index for Mumbai Region (More regions will be updated).</p>

###

<h4 align="left">Project Life-Cycle :</h4>

###

<p align="left">1. Data Collection:<br>This Website uses a web scrapper that scraps data from https://en.tutiempo.net/ for climate data from 2013 to 2018 and creates a HTML file for each month.</p>

###

<p align="left">2. Data Preprocessing:<br>For this step, I have taken the data from Krish Naik's project as it was from a paid API.<br>Reference: https://github.com/krishnaik06/AQI-Project/tree/master/Data/AQI.<br>This data contained hourly measurements of AQI.<br>This was converted into a dictionary format where the dictionary key is the year and values are the daily AQI values.<br>Next, the data in step 1 was combined with data of this step to create a new CSV file.</p>

###

<p align="left">3. Data Cleaning:<br>The CSV file created in step 2 was cleaned to remove null values and improper data. A new resultant CSV file was created.</p>

###

<p align="left">4.  Feature Engineering and Model Creation:<br>Tried various algorithms, like Linear Regression, Lasso and Ridge Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost Regressor.<br>Random Forest and XGBoost gave best performance. Finally, used Random Forest Regressor to perform predictions.<br>(execute individual jupyter notebooks)</p>

###

<h4 align="left">Tech-Stack :</h4>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="40" alt="numpy logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" height="40" alt="jupyter logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" alt="flask logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
</div>

###

<h4 align="left">Screenshots :</h4>

###

<div align="center">
  <img height="400" src="https://github.com/Sanskarr25/AirWise/blob/main/images/Home.png"  />
</div>

###

<div align="center">
  <img height="350" src="https://github.com/Sanskarr25/AirWise/blob/main/images/predict_input.png"  />
</div>

###

<div align="center">
  <img height="350" src="https://github.com/Sanskarr25/AirWise/blob/main/images/predict_output.png"  />
</div>

###
