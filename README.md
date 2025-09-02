# saas-dataset
Fake B2B SaaS start up using HubSpot

This project generates realistic, HubSpot-style CRM datasets for testing, analysis, or demonstrations.
It uses Python, pandas, and faker to output synthetic CSVs with properties and relationships modeled after HubSpot CRM objects.

📂 Generated CSV Files

The script produces the following files:

contacts.csv – fake people with HubSpot-style fields (e.g., firstname, lastname, email, jobtitle, lifecyclestage).

companies.csv – fake organizations with properties like name, industry, annualrevenue, numberofemployees.

deals.csv – sales deals tied to contacts and companies (fields like dealname, pipeline, dealstage, amount).

tickets.csv – support tickets related to customers, with realistic subjects (e.g., UI issues, integration errors, user permissions).

engagements.csv – activities such as calls, emails, and meetings linked to contacts and deals.

🔗 Relationships

Contacts belong to Companies (company_id).

Deals are associated with both Contacts and Companies.

Tickets are linked to Contacts (and optionally Deals).

Engagements are tied to Contacts and Deals.

🚀 Getting Started
1. Clone the Repository

'git clone https://github.com/YOUR-USERNAME/hubspot-fake-data.git
cd hubspot-fake-data'

2. Install Dependencies

'pip install -r requirements.txt'

3. Run the Script

'python generate_fake_hubspot_data.py'

4. Output

Generated CSV files will appear in the project root.

⚠️ Disclaimer

This dataset is entirely fake and generated for educational and testing purposes only.
It is not connected to HubSpot and does not contain any real customer data.
