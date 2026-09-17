# Data Dictionary

## customers

**Grain:** One record per customer.

| Column          | Type    | Description                      |
| --------------- | ------- | -------------------------------- |
| customer_id     | String  | Unique customer identifier       |
| first_name      | String  | Customer first name              |
| last_name       | String  | Customer last name               |
| date_of_birth   | Date    | Customer date of birth           |
| gender          | String  | Customer gender                  |
| city            | String  | Customer city                    |
| state           | String  | Customer state                   |
| employment_type | String  | Employment category              |
| monthly_income  | Decimal | Approximate monthly income       |
| customer_since  | Date    | Customer relationship start date |

---

## loan_products

**Grain:** One record per loan product.

| Column            | Type    | Description               |
| ----------------- | ------- | ------------------------- |
| product_id        | String  | Unique product identifier |
| product_name      | String  | Loan product name         |
| product_type      | String  | Product category          |
| interest_rate     | Decimal | Annual interest rate      |
| min_amount        | Decimal | Minimum loan amount       |
| max_amount        | Decimal | Maximum loan amount       |
| max_tenure_months | Integer | Maximum permitted tenure  |

---

## branches

**Grain:** One record per branch.

| Column      | Type   | Description              |
| ----------- | ------ | ------------------------ |
| branch_id   | String | Unique branch identifier |
| branch_name | String | Branch name              |
| city        | String | Branch city              |
| state       | String | Branch state             |
| region      | String | Business region          |

---

## loans

**Grain:** One record per loan.

| Column            | Type    | Description            |
| ----------------- | ------- | ---------------------- |
| loan_id           | String  | Unique loan identifier |
| customer_id       | String  | Customer reference     |
| product_id        | String  | Loan product reference |
| branch_id         | String  | Branch reference       |
| application_date  | Date    | Loan application date  |
| approval_date     | Date    | Loan approval date     |
| disbursement_date | Date    | Loan disbursement date |
| loan_amount       | Decimal | Disbursed loan amount  |
| interest_rate     | Decimal | Loan interest rate     |
| tenure_months     | Integer | Loan tenure            |
| loan_status       | String  | Current loan status    |

---

## repayments

**Grain:** One record per scheduled repayment.

| Column         | Type    | Description                 |
| -------------- | ------- | --------------------------- |
| repayment_id   | String  | Unique repayment identifier |
| loan_id        | String  | Loan reference              |
| customer_id    | String  | Customer reference          |
| due_date       | Date    | Scheduled payment date      |
| payment_date   | Date    | Actual payment date         |
| due_amount     | Decimal | Amount due                  |
| paid_amount    | Decimal | Amount paid                 |
| payment_status | String  | Payment status              |
| dpd            | Integer | Days past due               |

---

## credit_history

**Grain:** One credit snapshot per customer and observation date.

| Column             | Type    | Description                |
| ------------------ | ------- | -------------------------- |
| credit_id          | String  | Unique credit record       |
| customer_id        | String  | Customer reference         |
| credit_score       | Integer | Credit score               |
| total_accounts     | Integer | Total credit accounts      |
| active_accounts    | Integer | Active credit accounts     |
| overdue_accounts   | Integer | Number of overdue accounts |
| credit_utilization | Decimal | Credit utilization ratio   |
| record_date        | Date    | Credit snapshot date       |

---

## customer_interactions

**Grain:** One record per customer interaction.

| Column              | Type   | Description                   |
| ------------------- | ------ | ----------------------------- |
| interaction_id      | String | Unique interaction identifier |
| customer_id         | String | Customer reference            |
| interaction_date    | Date   | Interaction date              |
| channel             | String | Interaction channel           |
| interaction_type    | String | Type of interaction           |
| interaction_outcome | String | Interaction outcome           |
