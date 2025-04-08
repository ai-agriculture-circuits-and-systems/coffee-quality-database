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
├── data/               # Dataset files
├── notebooks/          # Jupyter notebooks for analysis
└── README.md          # This file
```

## Getting Started

1. Clone this repository
2. Navigate to the `data` directory to access the dataset
3. Use the Jupyter notebooks in the `notebooks` directory to explore the data

## License

This project uses data from the Coffee Quality Institute's database. Please refer to their terms of use for data usage guidelines. 