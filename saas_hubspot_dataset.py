import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Number of records per dataset
NUM_COMPANIES = 50
NUM_CONTACTS = 200
NUM_DEALS = 150
NUM_TICKETS = 100
NUM_PRODUCTS = 20

# --- Companies ---
companies = []
for i in range(1, NUM_COMPANIES + 1):
    companies.append({
        "company_id": i,
        "company_name": fake.company(),
        "industry": random.choice(["SaaS", "Fintech", "Healthcare", "E-commerce", "EdTech"]),
        "annual_revenue": round(random.uniform(1_000_000, 100_000_000), 2),
        "num_employees": random.randint(10, 2000),
        "country": fake.country()
    })
companies_df = pd.DataFrame(companies)

# --- Contacts ---
contacts = []
for i in range(1, NUM_CONTACTS + 1):
    contacts.append({
        "contact_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "job_title": random.choice(["VP Sales", "Marketing Director", "RevOps Manager", "CRO", "CEO"]),
        "company_id": random.randint(1, NUM_COMPANIES)  # Link to company
    })
contacts_df = pd.DataFrame(contacts)

# --- Deals ---
deals = []
for i in range(1, NUM_DEALS + 1):
    deals.append({
        "deal_id": i,
        "deal_name": f"Deal {i}",
        "amount": round(random.uniform(5000, 500000), 2),
        "stage": random.choice(["Prospecting", "Demo Scheduled", "Negotiation", "Closed Won", "Closed Lost"]),
        "close_date": fake.date_this_year(),
        "company_id": random.randint(1, NUM_COMPANIES),  # Link to company
        "contact_id": random.randint(1, NUM_CONTACTS)   # Link to contact
    })
deals_df = pd.DataFrame(deals)

# --- Tickets ---
tickets = []
for i in range(1, NUM_TICKETS + 1):
    tickets.append({
        "ticket_id": i,
        "subject": fake.sentence(nb_words=6),
        "status": random.choice(["Open", "In Progress", "Closed", "Escalated"]),
        "priority": random.choice(["Low", "Medium", "High", "Urgent"]),
        "created_date": fake.date_this_year(),
        "company_id": random.randint(1, NUM_COMPANIES),  # Link to company
        "contact_id": random.randint(1, NUM_CONTACTS)   # Link to contact
    })
tickets_df = pd.DataFrame(tickets)

# --- Products ---
products = []
for i in range(1, NUM_PRODUCTS + 1):
    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize() + " Software",
        "price": round(random.uniform(100, 5000), 2),
        "category": random.choice(["CRM", "Analytics", "Security", "Marketing", "Finance"])
    })
products_df = pd.DataFrame(products)

# --- Save datasets as CSV ---
companies_df.to_csv("companies.csv", index=False)
contacts_df.to_csv("contacts.csv", index=False)
deals_df.to_csv("deals.csv", index=False)
tickets_df.to_csv("tickets.csv", index=False)
products_df.to_csv("products.csv", index=False)

print("✅ Fake SaaS HubSpot-style datasets generated successfully!")