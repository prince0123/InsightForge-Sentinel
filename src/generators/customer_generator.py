"""
============================================================
InsightForge Sentinel
Customer Generator
============================================================

Generates enterprise customer master data.

Author : InsightForge
Version : 0.1
"""

from faker import Faker
import pandas as pd
import random


class CustomerGenerator:

    def __init__(self, count: int = 1000):

        self.count = count
        self.fake = Faker("en_IN")

    def generate(self) -> pd.DataFrame:

        customers = []

        for i in range(1, self.count + 1):

            customer = {

                "customer_id": f"CUST{i:06}",

                "first_name": self.fake.first_name(),

                "last_name": self.fake.last_name(),

                "email": self.fake.email(),

                "phone": self.fake.msisdn()[:10],

                "gender": random.choice(
                    ["Male", "Female"]
                ),

                "city": self.fake.city(),

                "state": self.fake.state(),

                "created_date": self.fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )

            }

            customers.append(customer)

        return pd.DataFrame(customers)