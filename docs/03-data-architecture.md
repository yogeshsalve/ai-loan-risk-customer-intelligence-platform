SOURCE
  │
  ▼
ADLS GEN2
  │
  ▼
┌─────────────────┐
│     BRONZE      │
│ Raw Delta Data  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     SILVER      │
│ Cleaned Data    │
│ Validated Data  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      GOLD       │
│ Business Data   │
│ Customer 360    │
└────────┬────────┘
         │
    ┌────┼────────────┐
    ▼    ▼            ▼
   BI    ML          DQ
    │    │            │
    │    ▼            ▼
    │  Risk        Monitoring
    │ Prediction
    │
    └────────┬──────────────┐
             ▼              ▼
           API             AI/RAG
             │              │
             └──────┬───────┘
                    ▼
                 React