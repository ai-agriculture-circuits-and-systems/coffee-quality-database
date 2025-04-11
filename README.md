# Coffee Quality Database Analysis
https://github.com/jldbc/coffee-quality-database

This project analyzes a dataset of coffee quality reviews, containing detailed information about various coffee beans and their characteristics.

## Dataset Overview

The dataset contains reviews of 1,340 coffee beans (1,312 arabica and 28 robusta) from the Coffee Quality Institute's trained reviewers. The data includes comprehensive quality measures and metadata about the beans and their origins.

### Quality Measures
* Aroma
* Flavor
* Aftertaste
* Acidity
* Body
* Balance
* Uniformity
* Cup Cleanliness
* Sweetness
* Moisture
* Defects

### Bean Metadata
* Processing Method
* Color
* Species (arabica / robusta)

### Farm Metadata
* Owner
* Country of Origin
* Farm Name
* Lot Number
* Mill
* Company
* Altitude
* Region

## Data Source

The original data was collected from the Coffee Quality Institute's [review pages](https://database.coffeeinstitute.org/) and is available in both raw and cleaned formats. The cleaned dataset is recommended for analysis as it addresses various encodings, abbreviations, and units of measurement used in the original data.

## Project Structure

```
coffee-quality-database/
├── data/                           # Dataset files
│   ├── arabica_data_cleaned.csv    # Cleaned arabica coffee data
│   ├── arabica_data_cleaned.json   # JSON format of cleaned arabica data
│   ├── arabica_ratings_raw.csv     # Raw arabica coffee ratings
│   ├── arabica_ratings_raw.json    # JSON format of raw arabica data
│   ├── robusta_data_cleaned.csv    # Cleaned robusta coffee data
│   ├── robusta_data_cleaned.json   # JSON format of cleaned robusta data
│   ├── robusta_ratings_raw.csv     # Raw robusta coffee ratings
│   └── robusta_ratings_raw.json    # JSON format of raw robusta data
├── scraper/                        # Data collection scripts
│   ├── cqi_bot_session.py          # Bot session management for CQI website
│   └── process_tables.py           # Table processing and data extraction
├── csv_to_json.py                  # CSV to JSON conversion utility
├── clean_coffee_data.R             # Data cleaning and preprocessing script
├── LICENSE                         # License information
└── README.md                       # This file
```

## Code Files Description

### Data Collection
- `scraper/cqi_bot_session.py`: Manages bot sessions for accessing the Coffee Quality Institute website
- `scraper/process_tables.py`: Processes and extracts data from CQI website tables

### Data Processing
- `clean_coffee_data.R`: Comprehensive R script for cleaning and preprocessing the coffee dataset. It handles:
  - Data standardization
  - Unit conversions
  - Missing value imputation
  - Data validation
  - Feature engineering

### Utilities
- `csv_to_json.py`: Command-line utility to convert CSV files to JSON format
  ```bash
  python csv_to_json.py -i input.csv -o output.json --indent 4
  ```

## Getting Started

1. Clone this repository
2. Install required dependencies:
   - Python packages: pandas, json
   - R packages: dplyr, stringr, digest
3. The data is available in both CSV and JSON formats in the `data` directory:
   - Raw data: `arabica_ratings_raw.csv/json` and `robusta_ratings_raw.csv/json`
   - Cleaned data: `arabica_data_cleaned.csv/json` and `robusta_data_cleaned.csv/json`
4. For data cleaning, run the R script:
   ```bash
   Rscript clean_coffee_data.R
   ```
5. To convert cleaned data to JSON format:
   ```bash
   python csv_to_json.py -i data/arabica_data_cleaned.csv
   ```

## License

This project uses data from the Coffee Quality Institute's database. Please refer to their terms of use for data usage guidelines. 