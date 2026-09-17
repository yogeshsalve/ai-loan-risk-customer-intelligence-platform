import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker


fake = Faker("en_IN")

random.seed(42)
np.random.seed(42)
Faker.seed(42)


OUTPUT_DIR = "data/sample"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

NUM_CUSTOMERS = 1000
NUM_LOANS = 2500
NUM_REPAYMENTS = 20000
NUM_CREDIT_RECORDS = 3000
NUM_INTERACTIONS = 5000


# --------------------------------------------------
# Loan Products
# --------------------------------------------------

loan_products = pd.DataFrame([
    {
        "product_id": "LP001",
        "product_name": "Personal Loan",
        "product_type": "PERSONAL",
        "interest_rate": 14.5,
        "min_amount": 50000,
        "max_amount": 500000,
        "max_tenure_months": 60,
    },
    {
        "product_id": "LP002",
        "product_name": "Auto Loan",
        "product_type": "AUTO",
        "interest_rate": 10.5,
        "min_amount": 100000,
        "max_amount": 1500000,
        "max_tenure_months": 84,
    },
    {
        "product_id": "LP003",
        "product_name": "Home Loan",
        "product_type": "HOME",
        "interest_rate": 8.5,
        "min_amount": 500000,
        "max_amount": 5000000,
        "max_tenure_months": 240,
    },
    {
        "product_id": "LP004",
        "product_name": "Business Loan",
        "product_type": "BUSINESS",
        "interest_rate": 16.0,
        "min_amount": 100000,
        "max_amount": 2000000,
        "max_tenure_months": 120,
    },
    {
        "product_id": "LP005",
        "product_name": "Gold Loan",
        "product_type": "GOLD",
        "interest_rate": 12.0,
        "min_amount": 20000,
        "max_amount": 1000000,
        "max_tenure_months": 36,
    },
])


# --------------------------------------------------
# Branches
# --------------------------------------------------

branches = []

cities = [
    ("Mumbai", "Maharashtra", "West"),
    ("Pune", "Maharashtra", "West"),
    ("Nashik", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Bengaluru", "Karnataka", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Delhi", "Delhi", "North"),
    ("Jaipur", "Rajasthan", "North"),
    ("Kolkata", "West Bengal", "East"),
    ("Chennai", "Tamil Nadu", "South"),
]

for i, (city, state, region) in enumerate(cities, start=1):
    branches.append({
        "branch_id": f"BR{i:03d}",
        "branch_name": f"{city} Main Branch",
        "city": city,
        "state": state,
        "region": region,
    })

branches = pd.DataFrame(branches)


# --------------------------------------------------
# Customers
# --------------------------------------------------

customers = []

employment_types = [
    "SALARIED",
    "SELF_EMPLOYED",
    "BUSINESS_OWNER",
]

for i in range(1, NUM_CUSTOMERS + 1):

    city, state, _ = random.choice(cities)

    customers.append({
        "customer_id": f"C{i:06d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": fake.date_of_birth(
            minimum_age=21,
            maximum_age=65
        ),
        "gender": random.choice(["M", "F"]),
        "city": city,
        "state": state,
        "employment_type": random.choice(employment_types),
        "monthly_income": random.randint(20000, 250000),
        "customer_since": fake.date_between(
            start_date="-8y",
            end_date="-30d"
        ),
    })

customers = pd.DataFrame(customers)


# --------------------------------------------------
# Loans
# --------------------------------------------------

loans = []

for i in range(1, NUM_LOANS + 1):

    customer = customers.sample(1).iloc[0]
    product = loan_products.sample(1).iloc[0]
    branch = branches.sample(1).iloc[0]

    application_date = fake.date_between(
        start_date="-5y",
        end_date="-30d"
    )

    approval_date = application_date + timedelta(
        days=random.randint(1, 10)
    )

    disbursement_date = approval_date + timedelta(
        days=random.randint(1, 5)
    )

    loan_amount = random.randint(
        int(product["min_amount"]),
        int(product["max_amount"])
    )

    loans.append({
        "loan_id": f"L{i:07d}",
        "customer_id": customer["customer_id"],
        "product_id": product["product_id"],
        "branch_id": branch["branch_id"],
        "application_date": application_date,
        "approval_date": approval_date,
        "disbursement_date": disbursement_date,
        "loan_amount": loan_amount,
        "interest_rate": product["interest_rate"],
        "tenure_months": random.randint(
            12,
            int(product["max_tenure_months"])
        ),
        "loan_status": random.choice([
            "ACTIVE",
            "CLOSED",
            "ACTIVE",
            "ACTIVE",
            "DEFAULT"
        ]),
    })

loans = pd.DataFrame(loans)


# --------------------------------------------------
# Credit History
# --------------------------------------------------

credit_history = []

for i in range(1, NUM_CREDIT_RECORDS + 1):

    customer = customers.sample(1).iloc[0]

    credit_history.append({
        "credit_id": f"CR{i:07d}",
        "customer_id": customer["customer_id"],
        "credit_score": random.randint(300, 900),
        "total_accounts": random.randint(1, 15),
        "active_accounts": random.randint(0, 10),
        "overdue_accounts": random.randint(0, 5),
        "credit_utilization": round(
            random.uniform(0.05, 0.95),
            2
        ),
        "record_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
    })

credit_history = pd.DataFrame(credit_history)


# --------------------------------------------------
# Repayments
# --------------------------------------------------

repayments = []

for i in range(1, NUM_REPAYMENTS + 1):

    loan = loans.sample(1).iloc[0]

    due_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    dpd = random.choices(
        [0, 5, 15, 30, 60, 90, 120],
        weights=[55, 15, 10, 8, 5, 4, 3]
    )[0]

    payment_date = due_date + timedelta(days=dpd)

    due_amount = random.randint(2000, 50000)

    if dpd >= 90:
        paid_amount = random.choice([
            0,
            int(due_amount * 0.25),
            int(due_amount * 0.5)
        ])
        payment_status = "OVERDUE"
    elif dpd > 0:
        paid_amount = due_amount
        payment_status = "LATE"
    else:
        paid_amount = due_amount
        payment_status = "ON_TIME"

    repayments.append({
        "repayment_id": f"R{i:08d}",
        "loan_id": loan["loan_id"],
        "customer_id": loan["customer_id"],
        "due_date": due_date,
        "payment_date": payment_date,
        "due_amount": due_amount,
        "paid_amount": paid_amount,
        "payment_status": payment_status,
        "dpd": dpd,
    })

repayments = pd.DataFrame(repayments)


# --------------------------------------------------
# Customer Interactions
# --------------------------------------------------

interactions = []

channels = [
    "CALL",
    "EMAIL",
    "SMS",
    "BRANCH",
    "APP",
]

interaction_types = [
    "PAYMENT_REMINDER",
    "LOAN_QUERY",
    "COMPLAINT",
    "GENERAL_QUERY",
    "COLLECTION",
]

outcomes = [
    "RESOLVED",
    "PENDING",
    "ESCALATED",
]

for i in range(1, NUM_INTERACTIONS + 1):

    customer = customers.sample(1).iloc[0]

    interactions.append({
        "interaction_id": f"I{i:07d}",
        "customer_id": customer["customer_id"],
        "interaction_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "channel": random.choice(channels),
        "interaction_type": random.choice(interaction_types),
        "interaction_outcome": random.choice(outcomes),
    })

interactions = pd.DataFrame(interactions)


# --------------------------------------------------
# Save Files
# --------------------------------------------------

datasets = {
    "customers": customers,
    "loan_products": loan_products,
    "branches": branches,
    "loans": loans,
    "repayments": repayments,
    "credit_history": credit_history,
    "customer_interactions": interactions,
}

for name, df in datasets.items():

    path = os.path.join(
        OUTPUT_DIR,
        f"{name}.csv"
    )

    df.to_csv(path, index=False)

    print(
        f"{name}: {len(df):,} records → {path}"
    )

print("\nData generation completed successfully.")