## Member 2 Documentation: Data Types & Keeping Data Safe

* **Notebook:** `03_member2_data_types.ipynb`
* **Role:** Fixing Data Types
* **Project:** Renewable Energy GB (Group 2)

---

### 1. What I Did
I made sure every column had the right format so the code could read it properly. I turned dates into real timestamps and energy numbers into decimals without deleting any data.

---

### 2. Step-by-Step Changes

#### A. Fixing the Date & Time Column (`utc_timestamp`)
* **What I changed:** Turned plain text dates into proper UTC time formats using `pd.to_datetime(..., utc=True)`.
* **How I checked:** Counted how many dates failed to convert (`0` errors) and checked that the timezone was set to `UTC`.
* **Result:** Every timestamp is now in a clean, standard date-and-time format (`datetime64[us, UTC]`).

#### B. Fixing the Number Columns
* **What I changed:** Checked all 15 energy measurement columns (load, wind, solar, and price) and if any numbers were saved as text I removed extra spaces and commas then converted them to decimal numbers (`float64`) using `pd.to_numeric()`.
* **How I checked:** Printed the column types before and after running the code to verify the change.
* **Result:** Every measurement column is now stored as `float64` and ready for math and charts.

---

### 3. Why I Kept All Data Values
I chose *not* to delete any rows or change any numbers during my step not to:

1. **Keeping the Timeline Unbroken:**
   Energy data tracks changes hour by hour across all 50,401 rows so deleting rows creates gaps in time and since all timestamps converted cleanly I kept every single row.

2. **Not Interfering with Teammates' Work:**
   * **For Member 1 (Missing Data & Duplicates):** If I deleted blank values now Member 1 wouldn't know where data was originally missing and keeping blank cells as `NaN` lets them handle missing data properly.
   * **For Member 3 (Outliers & Unusual Numbers):** Very high numbers or `0.0` values (like zero solar power at night) are real data not errors and keeping exact numbers lets Member 3 decide what counts as an outlier.

3. **Saving Numbers Stored as Text:**
   Cleaning up commas and spaces first ensured real numbers weren't accidentally turned into blanks (`NaN`).

---

### 4. Current Status
* **Done:** All 16 columns have the right data types, and zero rows were lost.
* **Next Step:** Combine my work with Member 1 and Member 3, then save the final file to `data/processed/cleaned_data.csv`.
