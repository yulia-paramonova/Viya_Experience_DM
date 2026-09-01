# Welcome to Viya Experience

[SAS Viya Trial](https://www.sas.com/fr_fr/trials/software/viya/viya-trial-form.html)  

[Accès Viya Trial](https://engage.my-trials.sas.com/onboard/return/XXXXXX)

[Questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=XE3BsSU2s0WkMJVSNzoML7xb9kiO-RZHjfeO7_4YlBNURExJMFpTWFZOVVhUNkRNVUNDTjlQMlVQTy4u)  

[lien 1](https://link.sas.com/f/a/P5RoPlTwcXle1s2ngg0cQA~~/AAQRrxA~/btSBKMYR_scO2NdIyhbai6JF0OjogrzNznFDuXgqEMCwOceCYD7FnSAW3g3QC8zNL2swpDA1-q_n_lvccBtbRls4LSKKCRp7QvSMvBg-iJ-X6MdlOMEvbuMxMvqpOrRdFS5CAn98FJpEWI9zplHeI_yNJm2PE5VOXu87FeXq05s~)

# Viya Experience - Data Management
Imagine you have just joined the data analytics team of the Ministry of Health.  

Your mission is to analyze hospital readmissions among diabetic patients and deliver reliable insights to healthcare decision-makers. Before any analysis can begin, you must ensure that the data is accurate, complete, and secure.  

During this guided hands-on workshop, you will explore how to profile, cleanse, transform, govern, and protect data using SAS Viya. You will then leverage this trusted data foundation to perform your first analyses and uncover patterns that could help improve patient outcomes.  


## Step 1 : Import the data using *Access and Manage Data*
Import to the `CASUSER` library : 
- `VXP_CITIES.xlsx`
- `VXP_DIABETIC_DATA.sashdat`  
Check the number of rows and columns.
<img width="1215" height="519" alt="image" src="https://github.com/user-attachments/assets/34c70e63-034c-4634-9c14-7638514e0e28" />


## Step 2 : *Discover and Govern Data* and apply business terms
Find `VXP_DIABETIC_DATA` and submit request for analysis.  
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fdacef76-9c44-4957-bd3d-e7db78eb4e28" />


### Step 2 Extra : Assign business descriptions to the variables.
You can use terms to assign business descriptions to the variables. First you need to create the terms. 

#### a. Create a simple term
*New term:* `Primary Diagnosis`  
*Term type:* `Default`  
→ *Create term*  
*Definition:* `The principal medical condition identified during a patient encounter, hospitalization, or episode of care and considered the primary reason for treatment or healthcare services. The diagnosis is represented using an ICD-9 code to support standardized clinical documentation, reporting, analysis, reimbursement, and healthcare research.`  
*Description:* `Represents the main diagnosis assigned to a patient by a healthcare professional. This term covers diagnoses recorded as the primary reason for care and encoded using the ICD-9 classification standard. It is used for clinical reporting, population health analysis, billing, regulatory reporting, and healthcare research. Only one primary diagnosis should be assigned per patient encounter or episode of care according to organizational coding guidelines.`  
→ *Save and Publish Draft*  
→ Assign it to `diag_1`

#### b. Create Term Type 
*New term type:* `Patient Information`   
*Description:* Business glossary term type used to document patient-related data elements and their privacy protection requirements. It helps identify whether sensitive patient information must be encrypted, masked, or otherwise protected before being used for analytics, reporting, or AI applications.  
  
***Attributes:***  
*Add → Boolean*  
Label text: `Needs to be encrypted`  
Description: `Indicates whether the data element must be encrypted or hashed to protect sensitive patient information from unauthorized disclosure.`  
*Examples: Patient Number → Yes; Primary Diagnosis → No; HbA1c Result → No*    
  
*Add → Boolean*  
Label text: `Needs to be masked`  
Description: `Indicates whether the data element should be masked before being displayed, shared, or used by authorized users.`  
*Examples: Race → Yes; Gender → Yes (depending on policy); Patient Name → Yes; HbA1c Result → No*  

#### c. Create Term using term type
*New term:* `Patient identification`  
*Term type:* `Patient Information`  
→ *Create term*  
*Definition:* `Information used to uniquely identify and distinguish a patient within a healthcare organization or information system. This includes patient identifiers such as patient ID, medical record number, or other unique identifiers that enable accurate linking of clinical, administrative, and analytical records to the correct individual while supporting continuity of care.`  
*Description:* `Represents data elements used to uniquely identify a patient across healthcare systems and business processes. This term covers patient identifiers assigned by healthcare providers or organizations and used for record matching, patient tracking, care coordination, reporting, and analytics. Values classified under this term contain personally identifiable information (PII) and typically require appropriate privacy protection measures, including encryption and masking according to organizational policies.`   
*Attributes:* `Needs to be encrypted`  
→ *Save and Publish Draft*  
→ Assign it to `patient_nbr`

#### d. Create Term using term type
*New term:* `Patient Demographics`  
*Term type:* `Patient Information`  
→ *Create term*  
*Definition:* `Information describing demographic attributes of a patient, such as gender, race, ethnicity, age group, or other population characteristics. These attributes are used to support healthcare reporting, research, population health analysis, health equity studies, and regulatory compliance.`  
*Description:* `Represents patient demographic data used for statistical, operational, and clinical analysis. This term covers characteristics that describe population groups rather than uniquely identifying an individual. Because demographic data may be sensitive and subject to privacy regulations, appropriate masking and access controls should be applied according to organizational policies.`  
*Attributes:* `Needs to be masked`  
→ *Save and Publish Draft*  
→ Assign it to `gender` and `race`  

## Step 3 : Prepare data in *SAS Data and AI Studio*
<img width="2000" height="1075" alt="image" src="https://github.com/user-attachments/assets/1b7b3b75-11c7-4364-997b-500ddcdae114" />

In order to use the data for modeling or reporting we need to ensure the quality (no duplicates in rows or columns, standard values for character variables) and protection (encryption or masking).
### a. Cities :  
1. Remove duplicates (215->176)
2. Clean data :  
   Standardize : `Geo_City` → City  
   Casing : `Geo_Department` → Proper case    
3. Manage variables :  
    Drop : `insee_code`, `label`, `region_name`, `city_code`, `region_geojson`    
    Rename : `city_code_stnd`→ `Geo_City`, `region_geojson_stnd`→ `Geo_Region`, prefix geo for all variables  
4. Improve zip code using [Geo_Data_CP.sas](./Geo_Data_CP.sas)
5. Save to a table WORK.CITIES

### b. Diabetic patients data :  
1. Add primary diagnosis category based on code using [Patient_data_diag.py](./Patient_data_diag.py) 
2. Mask data :    
race → Mask all except first and last  
gender → Truncate to initial
3. Save to a table WORK.PATIENTS

### c. Join CITIES and PATIENTS
Left Join on `Postal code`=`CP`  
Save to a table CASUSER.VXP_DM_READY  

## Step 4 : *Explore and visualise* the data 
1. `Readmitted` - drag and drop to the canvas. Interpret the results. Do you consider the number of readmissions high?
2. `Patient_nbr` - convert to category + New calculation Distinct count then add to the Readmitted graph. Interpret the results. What it the number of readmitted patients?
3. `Geo_Region` - New Geography - region by name then drag and drop to the canvas. What regions are the most impacted?
4. `Geo_City` - New Geography by latitude and longitude.
5. New Hierarchy `Geo_Region-Geo_City` then drag and drop. Double click on the most impacted regions, which cities have too many readmissions?
6. `Readmitted_flag` - right click convert to category, then right click and Explain on a New page. Interpret the results.

## Step 5 (optional) : *Build models*
Train several machine learning models and choose the best performing one to accurately predict the readmissions based on patients characteristics.
