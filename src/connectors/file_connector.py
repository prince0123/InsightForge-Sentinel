"""
===========================================================
InsightForge Sentinel
File Connector Module
===========================================================

Author : InsightForge
Version: 0.1.0

Purpose:
Load CSV and Excel datasets into pandas DataFrames.

Supported Formats:
- CSV
- XLSX
- XLS

===========================================================
"""

from pathlib import Path
import csv
import pandas as pd


class FileConnector:

    SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".xls"]

    def load(self, file_path: str | Path) -> pd.DataFrame:
        """
        Load a dataset into a Pandas DataFrame.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"\nFile not found:\n{path}")

        extension = path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file format: {extension}"
            )

        if extension == ".csv":
            return self._load_csv(path)

        return self._load_excel(path)

    # -------------------------------------------------------
    # CSV Loader
    # -------------------------------------------------------

    def _load_csv(self, path: Path) -> pd.DataFrame:

        print("\nLoading CSV...")

        # Detect delimiter
        with open(path, "r", encoding="utf-8-sig") as file:

            sample = file.read(2048)
            file.seek(0)

            try:
                dialect = csv.Sniffer().sniff(sample)
                delimiter = dialect.delimiter
            except csv.Error:
                delimiter = ","

        print(f"Detected Delimiter : '{delimiter}'")

        # Read normally
        df = pd.read_csv(
            path,
            sep=delimiter,
            encoding="utf-8-sig"
        )

        # ----------------------------------------------------
        # Detect malformed CSV
        # Entire row stored as one string
        # ----------------------------------------------------

        if df.shape[1] == 1:

            print("Malformed CSV detected.")
            print("Attempting automatic repair...")

            with open(path, "r", encoding="utf-8-sig") as file:

                rows = []

                for line in file:

                    line = line.strip()

                    # Remove surrounding quotes
                    if line.startswith('"') and line.endswith('"'):
                        line = line[1:-1]

                    rows.append(line.split(","))

            header = rows[0]
            data = rows[1:]

            repaired_df = pd.DataFrame(
                data,
                columns=header
            )

            print("Repair Successful")
            print(f"Loaded Shape : {repaired_df.shape}")

            return repaired_df

        print(f"Loaded Shape : {df.shape}")

        return df

    # -------------------------------------------------------
    # Excel Loader
    # -------------------------------------------------------

    def _load_excel(self, path: Path) -> pd.DataFrame:

        print("\nLoading Excel...")

        df = pd.read_excel(path)

        print(f"Loaded Shape : {df.shape}")

        return df