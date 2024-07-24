# flight_energy_analysis
Matoso's Master Project

# Flight Data Lake Folder DATA Sequence - Bronze Layer
flight_datalake/FLT[#Number]_[AIRPORT_CODE].csv

# Flight Result Data Lake Folder DATA Sequence - Silver Layer
Result_datalake/[AIRPORT_CODE]/FLT[#Number]_[AIRPORT_CODE].csv -> This folder makes reference to SILVER layer where the data is cleaned.

# Flight Result Data Lake Folder Sequence - ENERGY PROFILE IMAGES DATA LAKE
Result_datalake/Energy_Profile/[AIRPORT_CODE]/FLT[#Number]_[AIRPORT_CODE].csv -> This folder makes reference to graph images.

# Flight Result Data Lake Folder Sequence - VERTICAL PROFILE IMAGES DATA LAKE
Result_datalake/Vertical_Profile/[AIRPORT_CODE]/FLT[#Number]_[AIRPORT_CODE].csv -> This folder makes reference to graph images.

# Flight Result Data Lake Folder Sequence - TDD X (ALT and CAS) IMAGES DATA LAKE
Result_datalake/ALTXCAS/[AIRPORT_CODE]/FLT[#Number]_[AIRPORT_CODE].csv -> This folder makes reference to graph images.