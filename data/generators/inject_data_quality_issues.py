import os
import random

import numpy as np
import pandas as pd


random.seed(42)
np.random.seed(42)


SOURCE_DIR = "data/sample"
OUTPUT_DIR = "data/sample/dirty"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(filename):
    path = os.path.join(SOURCE_DIR, filename)
    return pd.read_csv(path)


def save_data(df, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Created: {path} | Records: {len(df):,}")


# ==========================================================
# CUSTOMERS
# ==========================================================

customers = load_data("customers.csv")

# 1. NULL monthly income
null_income_indexes = customers.sample(
    frac=0.02,
    random_state=42
).index

customers.loc[
    null_income_indexes,
    "monthly_income"
] = np.nan


# 2. NULL customer city
null_city_indexes = customers.sample(
    frac=0.01,
    random_state=43
).index

customers.loc[
    null_city_indexes,
    "city"
] = np.nan


# 3. Duplicate customers
duplicate_customers = customers.sample(
    n=20,
    random_state=44
)

customers = pd.concat(
    [customers, duplicate_customers],
    ignore_index=True
)


save_data(customers, "customers.csv")


# ==========================================================
# LOANS
# ==========================================================

loans = load_data("loans.csv")

# 4. Negative loan amounts
negative_loan_indexes = loans.sample(
    n=10,
    random_state=45
).index

loans.loc[
    negative_loan_indexes,
    "loan_amount"
] = -abs(
    loans.loc[
        negative_loan_indexes,
        "loan_amount"
    ]
)


# 5. Invalid loan status
invalid_status_indexes = loans.sample(
    n=10,
    random_state=46
).index

loans.loc[
    invalid_status_indexes,
    "loan_status"
] = "INVALID"


# 6. Orphan customer IDs
orphan_indexes = loans.sample(
    n=10,
    random_state=47
).index

loans.loc[
    orphan_indexes,
    "customer_id"
] = [
    f"C999{100 + i}"
    for i in range(len(orphan_indexes))
]


# 7. Duplicate loans
duplicate_loans = loans.sample(
    n=15,
    random_state=48
)

loans = pd.concat(
    [loans, duplicate_loans],
    ignore_index=True
)


save_data(loans, "loans.csv")


# ==========================================================
# CREDIT HISTORY
# ==========================================================

credit_history = load_data("credit_history.csv")


# 8. Invalid credit scores
invalid_score_indexes = credit_history.sample(
    n=20,
    random_state=49
).index

invalid_scores = [
    100,
    150,
    950,
    1000,
    1200,
    -10,
    -50,
]

credit_history.loc[
    invalid_score_indexes,
    "credit_score"
] = np.random.choice(
    invalid_scores,
    size=len(invalid_score_indexes)
)


# 9. NULL credit score
null_score_indexes = credit_history.sample(
    n=15,
    random_state=50
).index

credit_history.loc[
    null_score_indexes,
    "credit_score"
] = np.nan


save_data(
    credit_history,
    "credit_history.csv"
)


# ==========================================================
# REPAYMENTS
# ==========================================================

repayments = load_data("repayments.csv")


# 10. Negative paid amounts
negative_payment_indexes = repayments.sample(
    n=20,
    random_state=51
).index

repayments.loc[
    negative_payment_indexes,
    "paid_amount"
] = -abs(
    repayments.loc[
        negative_payment_indexes,
        "paid_amount"
    ]
)


# 11. Invalid DPD
invalid_dpd_indexes = repayments.sample(
    n=15,
    random_state=52
).index

repayments.loc[
    invalid_dpd_indexes,
    "dpd"
] = -5


# 12. Invalid payment status
invalid_payment_status_indexes = repayments.sample(
    n=15,
    random_state=53
).index

repayments.loc[
    invalid_payment_status_indexes,
    "payment_status"
] = "UNKNOWN"


# 13. Duplicate repayments
duplicate_repayments = repayments.sample(
    n=30,
    random_state=54
)

repayments = pd.concat(
    [repayments, duplicate_repayments],
    ignore_index=True
)


save_data(
    repayments,
    "repayments.csv"
)


# ==========================================================
# CUSTOMER INTERACTIONS
# ==========================================================

interactions = load_data(
    "customer_interactions.csv"
)


# 14. Orphan customer IDs
interaction_orphan_indexes = interactions.sample(
    n=10,
    random_state=55
).index

interactions.loc[
    interaction_orphan_indexes,
    "customer_id"
] = [
    f"C888{100 + i}"
    for i in range(len(interaction_orphan_indexes))
]


# 15. Invalid interaction outcome
invalid_outcome_indexes = interactions.sample(
    n=10,
    random_state=56
).index

interactions.loc[
    invalid_outcome_indexes,
    "interaction_outcome"
] = "UNKNOWN"


save_data(
    interactions,
    "customer_interactions.csv"
)


print("\n======================================")
print("DATA QUALITY ISSUE INJECTION COMPLETE")
print("======================================")