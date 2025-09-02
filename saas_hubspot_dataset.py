import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# --------------------
# Parameters
# --------------------
NUM_CONTACTS = 200
NUM_COMPANIES = 50
NUM_DEALS = 100
NUM_TICKETS = 80
NUM_ENGAGEMENTS = 150

# --------------------
# Helper functions
# --------------------
def random_date(start_days_ago=365, end_days_ago=0):
    """Generate a random datetime between now - start_days_ago and now - end_days_ago"""
    start_date = datetime.now() - timedelta(days=start_days_ago)
    end_date = datetime.now() - timedelta(days=end_days_ago)
    return fake.date_time_between(start_date=start_date, end_date=end_date)

# --------------------
# Generate Companies
# --------------------
companies = []
for i in range(1, NUM_COMPANIES + 1):
    companies.append({
        "companyId": i,
        "name": fake.company(),
        "domain": fake.domain_name(),
        "industry": fake.job().split(" ")[-1] + " Tech",
        "createdate": random_date()
    })
companies_df = pd.DataFrame(companies)

# --------------------
# Generate Contacts
# --------------------
contacts = []
for i in range(1, NUM_CONTACTS + 1):
    company = random.choice(companies)
    contacts.append({
        "contactId": i,
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "companyId": company["companyId"],
        "jobtitle": fake.job(),
        "lifecyclestage": random.choice(["subscriber", "lead", "marketingqualifiedlead", "salesqualifiedlead", "opportunity", "customer"]),
        "createdate": random_date()
    })
contacts_df = pd.DataFrame(contacts)

# --------------------
# Generate Deals
# --------------------
deals = []
for i in range(1, NUM_DEALS + 1):
    company = random.choice(companies)
    contact = random.choice([c for c in contacts if c["companyId"] == company["companyId"]])
    deals.append({
        "dealId": i,
        "dealname": f"{random.choice(['Growth', 'Enterprise', 'Starter', 'Pro'])} Plan - {company['name']}",
        "amount": round(random.uniform(500, 50000), 2),
        "dealstage": random.choice(["appointmentscheduled", "qualifiedtobuy", "presentation", "decisionmakerboughtin", "contractsent", "closedwon", "closedlost"]),
        "companyId": company["companyId"],
        "contactId": contact["contactId"],
        "createdate": random_date()
    })
deals_df = pd.DataFrame(deals)

# --------------------
# Generate Tickets
# --------------------
ticket_subjects = [
    "Login page error 500",
    "User cannot reset password",
    "Dashboard button not clickable",
    "Salesforce sync failed",
    "Integration with Slack not working",
    "Report export CSV missing fields",
    "Email notifications not sending",
    "Request for dark mode option",
    "Billing page shows incorrect amount",
    "Permission denied for team member",
    "Two-factor authentication issue",
    "Form submission not saving data",
    "UI glitch on mobile app",
    "Zapier integration timeout error",
    "Subscription cancellation failed",
    "Error loading analytics report",
    "Feature request: custom roles",
    "Trial extension request",
    "Bug in user profile update",
    "Data not syncing across regions"
]

tickets = []
for i in range(1, NUM_TICKETS + 1):
    company = random.choice(companies)
    contact = random.choice([c for c in contacts if c["companyId"] == company["companyId"]])
    tickets.append({
        "ticketId": i,
        "subject": random.choice(ticket_subjects),
        "content": fake.text(max_nb_chars=120),
        "status": random.choice(["NEW", "OPEN", "WAITING_ON_CUSTOMER", "CLOSED"]),
        "priority": random.choice(["HIGH", "MEDIUM", "LOW"]),
        "companyId": company["companyId"],
        "contactId": contact["contactId"],
        "createdate": random_date()
    })
tickets_df = pd.DataFrame(tickets)

# --------------------
# Generate Engagements
# --------------------
engagement_types = ["EMAIL", "CALL", "MEETING", "NOTE"]
engagements = []
for i in range(1, NUM_ENGAGEMENTS + 1):
    contact = random.choice(contacts)
    engagements.append({
        "engagementId": i,
        "type": random.choice(engagement_types),
        "subject": fake.sentence(nb_words=6),
        "body": fake.paragraph(nb_sentences=3),
        "contactId": contact["contactId"],
        "companyId": contact["companyId"],
        "createdate": random_date()
    })
engagements_df = pd.DataFrame(engagements)

# --------------------
# Save to CSV
# --------------------
companies_df.to_csv("companies.csv", index=False)
contacts_df.to_csv("contacts.csv", index=False)
deals_df.to_csv("deals.csv", index=False)
tickets_df.to_csv("tickets.csv", index=False)
engagements_df.to_csv("engagements.csv", index=False)

print("✅ Fake HubSpot-style dataset generated: companies.csv, contacts.csv, deals.csv, tickets.csv, engagements.csv")
