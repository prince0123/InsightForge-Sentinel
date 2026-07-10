🧠 Sentinel Brain

This is what makes our product different.

Instead of thinking in terms of utilities, think in terms of capabilities.

Capability	Purpose
Understand Dataset	Profiler
Understand Columns	Business Type Analyzer
Understand Keys	Primary Key Analyzer
Understand Quality	Validation Engine
Understand Business Rules	Rule Engine
Explain Findings	Recommendation Engine
Communicate Results	Reporting Engine
🔌 Plugin Architecture

Every analyzer follows the same contract.

Instead of everyone writing different code styles, we'll define a common interface.

For Version 1.0, every analyzer should:

Accept a pandas.DataFrame
Return a dictionary with:
Analyzer name
Status
Summary
Results
Recommendations

Example:

{
    "analyzer": "PrimaryKeyAnalyzer",
    "status": "Success",
    "summary": "1 likely primary key found",
    "results": [
        {
            "column": "Order_ID",
            "confidence": 92,
            "reasons": [
                "No NULL values",
                "High uniqueness"
            ]
        }
    ],
    "recommendations": [
        "Investigate duplicate Order_ID values."
    ]
}

This consistency will make reporting much easier.