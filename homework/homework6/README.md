\#HW 6 Documentation

\#Cleaning Strategy

The cleaning strategy is based around replacing missing numeric values with median values to reduce bias from outliers. Categorical values are preserved as it is to avoid introducing artificial categories. We normalized numeric features to the 0–1 range, ensuring comparability across variables. Columns or rows with excessive missingness (threshold >50%) were dropped. The cleaned dataset is saved separately, and a comparison reports are generated in the notebook to document transformations.



\#Assumptions and Limitations

1\. Missing Data Handling

\- Filling missing numeric values with median assumes the missingness is MCAR or MAR (not systematically biased). We assume the missing age, income, score, and extra\_data values are not systematically missing (e.g., not all low-income people skipped reporting).  

\- Dropping rows assumes the missing rows are not critical to analysis.  

\- Imputation affects averages, distributions, and model training.





2\. Filtering / Data Cleaning

\- Removing negative or out-of-range values assumes they are errors or invalid entries. 

\- Dropping columns or rows with excessive missingness assumes those data are non-essential. If a column has >50% missing, we assume its loss won’t harm downstream analysis.

\- Rare but valid events might be lost if thresholds are too strict.



3\. Normalization

\- MinMaxScaler assumes min and max values are representative, not extreme outliers. 

-Assume features are comparable on a 0–1 scale, and relative differences matter more than absolute magnitudes 



4\. Outliers are not removed at this stage:

-Assumes they are legitimate observations unless proven otherwise.

-Scaling ensures they don’t dominate analysis



5.Categorical features (zipcode, city) are reliable as raw labels:

-Missing or ambiguous values (like "Unknown") are treated as valid categories.

-No need to impute because they don’t have natural numeric meaning



6\. Median is a good representation of central tendency for numeric variables:

-Income and score distributions may not be normal, so median is more robust than mean.



