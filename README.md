

## **Core Data Quality Dimensions**

### **1. Accuracy Issues**
- **Spelling mistakes and typos**: Misspelled words in text fields
- **Incorrect values**: Wrong information due to human error or system issues
- **Transcription errors**: Mistakes during manual data entry
- **Data drift and decay**: Information becoming inaccurate over time
- **Factual errors**: Contradictory information across systems

### **2. Completeness Problems**
- **Missing mandatory fields**: Required data fields left blank
- **Partial records**: Incomplete customer profiles or transaction records
- **Empty attributes**: Fields that should contain data but are null
- **Insufficient data coverage**: Inadequate representation of data categories

### **3. Consistency Issues**
- **Format inconsistency**: Same data type in different formats
  - Country names: "United States" vs "USA" vs "US" vs "U.S.A."
  - Date formats: "DD-MM-YYYY" vs "MM/DD/YYYY" vs "YYYY-MM-DD"
  - Phone numbers: "(555) 123-4567" vs "555-123-4567" vs "5551234567"
- **Unit inconsistency**: Weight in kilograms vs pounds
- **Case sensitivity variations**: "Female"/"FEMALE"/"female" vs "F"/"f"
- **Abbreviation inconsistency**: "Street" vs "St." vs "St"

### **4. Uniqueness and Duplication Issues**
- **Exact duplicates**: Identical records across the dataset
- **Fuzzy duplicates**: Similar but not identical records (e.g., "John Smith" vs "Jon Smith")
- **Cross-system duplicates**: Same entity appearing in multiple systems
- **Primary key violations**: Non-unique identifiers

## **Domain-Specific Standardization Errors**

### **5. Geographic Data Issues**
- **Country code inconsistencies**: 
  - Alpha-2 codes: "US" vs "USA"
  - Full names vs abbreviations: "Germany" vs "DE" vs "Deutschland"
  - Legacy vs current names: "Yugoslavia" vs current Balkan countries
- **State/Province variations**: "California" vs "CA" vs "Calif."
- **Address format inconsistencies**: Different address line structures
- **Postal code variations**: ZIP+4 vs 5-digit ZIP codes

### **6. Personal Information Issues**
- **Name format variations**: "John A. Smith" vs "Smith, John A." vs "J.A. Smith"
- **Gender representation**: "Male"/"Female" vs "M"/"F" vs "1"/"0"
- **Phone number formats**: International vs domestic formatting
- **Email format inconsistencies**: Case variations, domain spellings

### **7. Business Data Standardization**
- **Industry code variations**: NAICS vs SIC codes vs custom classifications
- **Currency representations**: "$100.00" vs "USD 100" vs "100 dollars"
- **Status codes**: "Active"/"Inactive" vs "A"/"I" vs "1"/"0"
- **Product categorization**: Different naming conventions across systems

## **Data Type and Format Issues**

### **8. Data Type Inconsistencies**
- **Mixed data types**: Numbers stored as text, dates as strings
- **Invalid data types**: Text in numeric fields, impossible dates
- **Precision variations**: Decimal places inconsistency
- **Boolean representations**: True/False vs 1/0 vs Y/N

### **9. Pattern and Syntax Violations**
- **Email format violations**: Missing "@" symbol, invalid domains
- **Invalid date formats**: February 30th, invalid leap year dates
- **Credit card number format errors**: Incorrect check digits, wrong length
- **Social security number issues**: Invalid format, impossible combinations

### **10. Range and Constraint Violations**
- **Out-of-range values**: Ages over 150, negative quantities where impossible
- **Business rule violations**: Return dates before purchase dates
- **Logical inconsistencies**: Child older than parent
- **Threshold violations**: Values exceeding acceptable limits

## **Structural and Relationship Issues**

### **11. Referential Integrity Problems**
- **Orphaned records**: Child records without corresponding parent records
- **Missing foreign key references**: References to non-existent master data
- **Broken relationships**: Links between tables that no longer exist
- **Cascade deletion failures**: Dependent records not properly handled

### **12. Schema and Structure Issues**
- **Column misalignment**: Data in wrong columns due to import errors
- **Schema drift**: Structure changes affecting data interpretation
- **Metadata inconsistencies**: Column definitions not matching actual data
- **Field length violations**: Data exceeding defined field sizes

## **Temporal and Lifecycle Issues**

### **13. Timeliness and Freshness Problems**
- **Stale data**: Information not updated within required timeframes
- **Outdated records**: Historical data inappropriately used as current
- **Data decay**: Information becoming less accurate over time
- **Synchronization delays**: Data not updated simultaneously across systems

### **14. Data Lifecycle Issues**
- **Orphaned data from deleted entities**: Data remaining after parent deletion
- **Retention policy violations**: Data kept beyond required periods
- **Archive inconsistencies**: Improper data archiving or retrieval
- **Zombie data**: Data from terminated employees or closed accounts

## **Security and Privacy Concerns**

### **15. PII Data Quality Issues**
- **Exposed sensitive information**: PII in non-secure fields
- **Inconsistent data masking**: Some PII masked, others not
- **Cross-contamination**: PII appearing in unexpected locations
- **Consent management**: Data without proper consent tracking

### **16. Data Classification Problems**
- **Misclassified sensitivity levels**: Incorrect data classification
- **Inconsistent protection**: Same data type protected differently
- **Access control mismatches**: Permissions not matching data sensitivity

## **Integration and Processing Issues**

### **17. Data Integration Problems**
- **Merge conflicts**: Conflicting data during system integration
- **Transformation errors**: Mistakes during data processing
- **Encoding issues**: Character encoding problems across systems
- **Data lineage breaks**: Lost track of data source and transformations

### **18. Cross-System Inconsistencies**
- **Synchronization failures**: Updates not propagated across systems
- **Version conflicts**: Different versions of same data in different systems
- **Master data mismatches**: Inconsistent master data across applications

## **Advanced Quality Issues**

### **19. Statistical Anomalies**
- **Outliers**: Values significantly different from expected ranges
- **Distribution anomalies**: Unexpected data distribution patterns
- **Correlation breaks**: Expected relationships between variables lost
- **Seasonal pattern violations**: Data not following expected temporal patterns

### **20. Metadata Quality Issues**
- **Missing documentation**: Insufficient metadata for understanding data
- **Incorrect data lineage**: Wrong source attribution
- **Outdated descriptions**: Metadata not reflecting current data state
- **Classification errors**: Wrong categorization of data elements


