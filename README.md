# Viya_Experience_DM

## SAS Studio
<img width="2000" height="1075" alt="image" src="https://github.com/user-attachments/assets/1b7b3b75-11c7-4364-997b-500ddcdae114" />

Cities :  
1. Remove duplicates (215->176)  
2. Manage variables :  
    Drop : `insee_code`, `label`, `region_name`  
    Rename : `city_code`->city, `region_geojson`->region, prefix geo for all variables  
3. Clean data :  
   Standardize : `Geo_City` --> City  
   Casing : `Geo_Department` --> Proper case  
5. Improve zip code using [Geo_Data_CP.sas](./Geo_Data_CP.sas) 

Diabetic patients data :  
1. Add primary diagnosis based on code using [Patient_data_diag.py](./Patient_data_diag.py) 
2. Mask data

VXP_DM_READY :  
Left Join on `Postal code`=`CP`

## SAS Visual Analytics 
1. `Readmitted` - automatic graph
2. `Patient_nbr` convert to category + new calculation distinct count then add to readmitted
3. `Region` Geography - region by name ; city by lat lon  
Hierarchy region-city  
