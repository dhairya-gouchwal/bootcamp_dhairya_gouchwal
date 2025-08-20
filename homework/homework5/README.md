\## Data Storage



I saved intermediate datasets in two places:

\- `data/raw/`: CSV format — human-readable, good for inspection and portability.

\- `data/processed/`: Parquet format — efficient for storage, preserves dtypes.



The notebook uses environment variables (`DATA\_DIR\_RAW`, `DATA\_DIR\_PROCESSED`) from `.env` to locate the folders.  

Utility functions `write\_df` and `read\_df` automatically choose CSV vs Parquet based on file extension.

