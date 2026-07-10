# Folder Structure

```
IF001-Sentinel/

│

├── data/

│   ├── sample/

│   ├── raw/

│   └── generated/

│

├── docs/

│   ├── Architecture/

│   ├── ADR/

│   ├── Sprints/

│   ├── Roadmap/

│   └── Standards/

│

├── src/

│   ├── analyzers/

│   ├── connectors/

│   ├── preprocessing/

│   ├── profiling/

│   ├── reporting/

│   ├── rules/

│   ├── engine/

│   ├── utils/

│   └── main.py

│

├── tests/

│

├── requirements.txt

├── README.md

└── .gitignore
```

Every folder has one responsibility.

Modules should remain independent and reusable.