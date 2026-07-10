🏗️ Module Architecture

This is the heart of Sentinel.

                 Sentinel

                     │

    ┌────────────────────────────────────┐

                    Core

    └────────────────────────────────────┘

                     │

         File Connector Layer

                     │

      Preprocessing Layer

                     │

        Dataset Profiler

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

   Analyzer       Analyzer      Analyzer

 Primary Key      Business       Statistics

                  Type

                     │

             Validation Engine

                     │

              Rule Engine

                     │

           Trust Score Engine

                     │

             Recommendation Engine

                     │

            Reporting Engine

                     │

        Console

        JSON

        Power BI

        API

        Power Automate