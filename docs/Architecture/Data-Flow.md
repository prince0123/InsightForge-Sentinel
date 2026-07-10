📈 Data Flow

Every dataset should travel through the exact same pipeline.

CSV

↓

Connector

↓

Preprocessor

↓

Profiler

↓

Analyzers

↓

Validation

↓

Trust Score

↓

Recommendations

↓

Reports

Every module receives a DataFrame and returns structured data.

No module should print directly.