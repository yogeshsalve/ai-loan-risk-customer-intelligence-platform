# Data Quality Strategy

## 1. Objective

The platform implements automated data-quality validation before data is promoted from the Bronze layer to the Silver layer.

The objective is to identify invalid, incomplete, duplicated and inconsistent records before they affect downstream analytics, machine learning and AI workloads.

## 2. Data Quality Dimensions

The platform will validate:

* Completeness
* Uniqueness
* Validity
* Accuracy
* Consistency
* Referential Integrity
* Business Rules

## 3. Planned Rules

| Rule ID | Dataset        | Rule                                     | Severity |
| ------- | -------------- | ---------------------------------------- | -------- |
| DQ001   | customers      | customer_id must not be NULL             | Critical |
| DQ002   | customers      | customer_id must be unique               | Critical |
| DQ003   | customers      | monthly_income must be positive          | High     |
| DQ004   | loans          | loan_id must be unique                   | Critical |
| DQ005   | loans          | customer_id must exist in customers      | Critical |
| DQ006   | loans          | loan_amount must be greater than 0       | High     |
| DQ007   | loans          | loan_status must be valid                | Medium   |
| DQ008   | credit_history | credit_score must be between 300 and 900 | High     |
| DQ009   | repayments     | repayment_id must be unique              | Critical |
| DQ010   | repayments     | paid_amount must not be negative         | High     |
| DQ011   | repayments     | dpd must not be negative                 | High     |
| DQ012   | repayments     | payment_status must be valid             | Medium   |
| DQ013   | interactions   | customer_id must exist in customers      | High     |

## 4. Data Quality Flow

```text
Bronze
   |
   v
DQ Validation
   |
   +------------------+
   |                  |
   v                  v
Valid Records     Invalid Records
   |                  |
   v                  v
Silver           Quarantine
                      |
                      v
                DQ Results
                      |
                      v
                 Monitoring
```

## 5. Severity

### Critical

The record cannot safely continue to downstream processing.

Example:

* Missing primary key
* Duplicate primary key
* Broken referential integrity

### High

The record contains a significant business/data issue.

Example:

* Negative loan amount
* Invalid credit score

### Medium

The record may continue depending on business rules.

Example:

* Invalid status
* Missing optional attribute

## 6. Portfolio Implementation

The data-quality framework will eventually be implemented in Azure Databricks using PySpark.

The framework will:

1. Read Bronze data.
2. Execute configurable validation rules.
3. Separate valid and invalid records.
4. Write valid records to Silver.
5. Write invalid records to quarantine.
6. Store rule execution results.
7. Calculate data-quality scores.
8. Expose results through monitoring dashboards.
