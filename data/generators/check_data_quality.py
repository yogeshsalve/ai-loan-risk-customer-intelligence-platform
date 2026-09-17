import pandas as pd


customers = pd.read_csv(
    "data/sample/dirty/customers.csv"
)

loans = pd.read_csv(
    "data/sample/dirty/loans.csv"
)

credit_history = pd.read_csv(
    "data/sample/dirty/credit_history.csv"
)

repayments = pd.read_csv(
    "data/sample/dirty/repayments.csv"
)


print("\n===== CUSTOMERS =====")

print(
    "Duplicate customer IDs:",
    customers["customer_id"].duplicated().sum()
)

print(
    "Missing income:",
    customers["monthly_income"].isna().sum()
)

print(
    "Missing city:",
    customers["city"].isna().sum()
)


print("\n===== LOANS =====")

print(
    "Negative loan amounts:",
    (loans["loan_amount"] < 0).sum()
)

print(
    "Invalid loan status:",
    (loans["loan_status"] == "INVALID").sum()
)

print(
    "Duplicate loan IDs:",
    loans["loan_id"].duplicated().sum()
)


print("\n===== CREDIT HISTORY =====")

print(
    "Invalid credit scores:",
    (
        (credit_history["credit_score"] < 300)
        |
        (credit_history["credit_score"] > 900)
    ).sum()
)

print(
    "Missing credit scores:",
    credit_history["credit_score"].isna().sum()
)


print("\n===== REPAYMENTS =====")

print(
    "Negative payments:",
    (repayments["paid_amount"] < 0).sum()
)

print(
    "Negative DPD:",
    (repayments["dpd"] < 0).sum()
)

print(
    "Unknown payment status:",
    (
        repayments["payment_status"] == "UNKNOWN"
    ).sum()
)

print(
    "Duplicate repayment IDs:",
    repayments["repayment_id"].duplicated().sum()
)