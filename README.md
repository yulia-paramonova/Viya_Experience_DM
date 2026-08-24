# Viya_Experience_DM

## SAS Studio

Cities :  
1. Remove duplicates (215->176)  
2. Manage variables :  
    Drop : insee, label, region_name  
    Rename : city_code->city, region_geojson->region, prefix geo for all variables  
3. Clean data :  
   Standardize : Geo_City --> City  
   Casing : Geo Department --> Proper case  
5. Improve zip code using code  

Diabetic data :  
1. Python transform
2. Mask data

Join on CP = Postal code

## SAS Visual Analytics 
Encounter_id, patient_nbr convert to category  
Readmitted - automatic graph  
Patient_nbr distinct count, add to readmitted  
Geography - region by name ; city by lat lon  
Hierarchy region-city  
