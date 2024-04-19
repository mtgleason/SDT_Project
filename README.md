# SDT_Project

Project file for the Software Development Tools Sprint from TripleTen.

This project takes data from a vehicle advertisement website and breaks down the data into easy to understand visualizations.

## Render URL

[Interactive](https://sdt-project-k8dg.onrender.com)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `python`, `pandas`, `streamlit` and `plotly.express`

```bash
pip install python
pip install pandas
pip install streamlit
pip install plotly.express
```

## Usage

Navigate to the `/SDT_Project/` directory and execute the following command:

```bash
python run app.py
```

## Data 

**Description of the data:**
- `price` = price of the vehicle
- `model_year` = model year of the vehicle
- `model` = model of the vehicle
- `condition` = condition of the vehicle (excellent, good, fair, etc.)
- `cylinders` = number of cylinders in the vehicle
- `fuel` = type of fuel the vehicle takes (gas, diesel, etc.)
- `odometer` = the mileage of the vehicle when it was published to the website
- `transmission` = automatic, manual, other
- `paint_color` = color of the vehicle
- `is_4wd` = if the vehicle has 4-wheel drive (Boolean)
- `date_posted` = the date the vehicle was published to the site
- `days_listed` = how long the vehicle was on the site to removal