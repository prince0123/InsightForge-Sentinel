"""
============================================================
InsightForge Sentinel
Profiler Engine
============================================================

Analyzes datasets before validation.

Author : InsightForge
Version : 0.1
"""

class DataProfiler:

    def profile(self, df: pd.DataFrame) -> dict:

        profile = {

            "rows": len(df),

            "columns": len(df.columns),

            "column_names": list(df.columns),

            "data_types": {
                col: str(dtype)
                for col, dtype in df.dtypes.items()
            },

            "missing_values": df.isnull().sum().to_dict(),

            "duplicate_rows": int(df.duplicated().sum()),

            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum()
                / 1024
                / 1024,
                2
            )

        }

        return profile