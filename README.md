# Viya_Experience_DM
Imagine you have just joined the data analytics team of the Ministry of Health.  

Your mission is to analyze hospital readmissions among diabetic patients and deliver reliable insights to healthcare decision-makers. Before any analysis can begin, you must ensure that the data is accurate, complete, and secure.  

During this guided hands-on workshop, you will explore how to profile, cleanse, transform, govern, and protect data using SAS Viya. You will then leverage this trusted data foundation to perform your first analyses and uncover patterns that could help improve patient outcomes.  


## Step 1 : Import the data using Data Hub
Import to the `CASUSER` library : 
- `VXP_CITIES.xlsx`
- `VXP_DIABETIC_DATA.sashdat`
Check the number of rows and columns

## Step 2 : Discover the data using Data Governance and apply business terms
Use information catalog to profile `VXP_DIABETIC_DATA`.  
Then assign business descriptions to selected variables.

## Step 3 : Prepare data in SAS Data and AI Studio
<img width="2000" height="1075" alt="image" src="https://github.com/user-attachments/assets/1b7b3b75-11c7-4364-997b-500ddcdae114" />

### Cities :  
1. Remove duplicates (215->176)  
2. Manage variables :  
    Drop : `insee_code`, `label`, `region_name`  
    Rename : `city_code`->city, `region_geojson`->region, prefix geo for all variables  
3. Clean data :  
   Standardize : `Geo_City` --> City  
   Casing : `Geo_Department` --> Proper case  
5. Improve zip code using [Geo_Data_CP.sas](./Geo_Data_CP.sas) 

### Diabetic patients data :  
1. Add primary diagnosis based on code using [Patient_data_diag.py](./Patient_data_diag.py) 
2. Mask data

### VXP_DM_READY :  
Left Join on `Postal code`=`CP`

## Step 4 : Explore the data in SAS Visual Analytics 
1. `Readmitted` - drag and drop to the canvas
2. `Patient_nbr` - convert to category + New calculation Distinct count then add to the Readmitted graph
3. `Geo_Region` - New Geography - region by name then drag and drop to the canvas
4. `Geo_City` - New Geography by latitude and longitude
5. New Hierarchy `Geo_Region-Geo_City` then drag and drop
