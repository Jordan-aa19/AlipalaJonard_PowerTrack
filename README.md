# ⚡ PowerTrack — Crimson Circuit

## Electricity Consumption and Billing Management System

PowerTrack is a cloud-based electricity consumption and billing management system developed using Python Flask and Firebase Cloud Firestore. It provides a centralized platform for managing consumer information, monitoring electricity consumption, recording meter readings, calculating electricity bills, and tracking payment status.

The system features a modern Crimson Circuit interface designed to provide an interactive, responsive, and user-friendly experience.

## 🌐 Live Website

**Vercel Deployment:** https://jonardalipala-powertrack.vercel.app/

**GitHub Repository:** https://github.com/Jordan-aa19/jonardalipala-Powertrack

**Local Website:** http://127.0.0.1:5009/

## Project Objectives

- Provide centralized management of electricity consumer records.
- Monitor and record monthly electricity consumption.
- Automatically calculate electricity bills based on meter readings.
- Track paid, unpaid, and overdue electricity bills.
- Implement CRUD operations using Firebase Cloud Firestore.
- Maintain accurate and organized records through data validation.

## System Features

- Interactive management dashboard
- Consumer information management
- Meter reading management
- Electricity billing management
- Automatic electricity consumption calculation
- Automatic electricity bill calculation
- Payment status monitoring
- Create, Read, Update, and Delete (CRUD) operations
- Search and filter functionality
- Individual record viewing
- Duplicate record prevention
- Input validation
- Linked record protection
- Dark and light mode
- Card and table views
- Responsive website design
- CSV report export
- Optional sample data insertion
- Cloud deployment through Vercel

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Firebase Cloud Firestore | NoSQL cloud database |
| Firebase Admin SDK | Database connectivity |
| Python-dotenv | Environment configuration |
| HTML5 | Website structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend functionality |
| PyCharm | Development environment |
| GitHub | Source code management |
| Vercel | Cloud hosting and deployment |

## Database Structure

The system uses three interconnected Firebase Cloud Firestore collections.

### 1. Consumers

Collection name: `consumers`

Stores electricity consumer information.

| Field | Description |
|---|---|
| full_name | Consumer's full name |
| account_number | Unique account number |
| meter_number | Unique electricity meter number |
| address | Consumer address |
| contact_number | Contact number |
| email | Email address |
| consumer_type | Residential, Commercial, or Industrial |
| status | Active or Inactive |
| created_at | Record creation timestamp |
| updated_at | Record modification timestamp |

### 2. Meter Readings

Collection name: `meter_readings`

Stores electricity consumption records.

| Field | Description |
|---|---|
| consumer_id | Reference to the consumer |
| previous_reading | Previous meter reading |
| current_reading | Current meter reading |
| consumption_kwh | Calculated electricity consumption |
| reading_date | Meter reading date |
| billing_month | Billing month |
| rate_per_kwh | Electricity rate per kilowatt-hour |
| created_at | Record creation timestamp |
| updated_at | Record modification timestamp |

### 3. Bills

Collection name: `bills`

Stores electricity billing and payment information.

| Field | Description |
|---|---|
| consumer_id | Reference to the consumer |
| reading_id | Reference to the meter reading |
| billing_month | Billing period |
| consumption_kwh | Total electricity consumption |
| rate_per_kwh | Electricity rate |
| additional_charge | Additional billing charges |
| total_amount | Total electricity bill |
| due_date | Payment deadline |
| payment_status | Paid, Unpaid, or Overdue |
| payment_date | Actual payment date |
| created_at | Record creation timestamp |
| updated_at | Record modification timestamp |

## Database Relationship

Consumers → Meter Readings → Bills

Each consumer can have multiple monthly meter readings. Each meter reading can have one corresponding electricity bill.

The system prevents duplicate monthly meter readings and electricity bills.

An internal `_system` collection is used for Firestore transaction coordination.

## Electricity Billing Formula

**Electricity Consumption:**

Consumption (kWh) = Current Reading − Previous Reading

**Total Electricity Bill:**

Total Amount = (Consumption × Rate per kWh) + Additional Charges

### Sample Calculation

| Description | Value |
|---|---:|
| Previous reading | 1,000 kWh |
| Current reading | 1,150 kWh |
| Total consumption | 150 kWh |
| Rate per kWh | ₱11.50 |
| Additional charge | ₱50.00 |
| Total electricity bill | ₱1,775.00 |

The electricity rates used in this project are illustrative and intended for educational purposes.

## Installation and Local Setup

### Step 1: Open the Project

Open the PowerTrack project folder using PyCharm.

Python 3.11 or later is recommended.

### Step 2: Install Dependencies

Open the PyCharm terminal and execute:

```powershell
python -m pip install -r requirements.txt
```

### Step 3: Configure Firebase Firestore

1. Open https://console.firebase.google.com/.
2. Create or select a Firebase project.
3. Enable Cloud Firestore.
4. Open Project Settings.
5. Select Service Accounts.
6. Generate a new private key.
7. Save the downloaded JSON file in the project folder as `ServiceAccountKey.json`.

### Step 4: Configure Environment Variables

Create a `.env` file containing:

```env
GOOGLE_APPLICATION_CREDENTIALS=ServiceAccountKey.json
FLASK_DEBUG=false
PORT=5009
```

### Step 5: Insert Sample Data

Run the following command to populate Firestore with fictional sample records:

```powershell
python seed_data.py
```

The sample data generator is designed to provide:

- 15 sample consumers
- 15 sample meter readings
- 15 sample electricity bills
- Residential, commercial, and industrial consumers
- Sample payment statuses
- Automatically calculated electricity bills

This step is optional. Existing sample records for the current billing month are reused to prevent duplication.

### Step 6: Run the Flask Application

```powershell
python app.py
```

Open the local website:

http://127.0.0.1:5009/

## Vercel Cloud Deployment

PowerTrack is deployed through Vercel using its connected GitHub repository.

### Deployment Configuration

| Configuration | Value |
|---|---|
| Project Name | jonardalipala-powertrack |
| Framework | Python Flask |
| Production Branch | main |
| Hosting Platform | Vercel |
| Database | Firebase Cloud Firestore |
| Deployment Type | Cloud-based |

### Vercel Environment Variables

Configure the following variables under Vercel Project Settings → Environment Variables.

| Variable | Value |
|---|---|
| FIREBASE_SERVICE_ACCOUNT | Complete Firebase service account JSON |
| FLASK_DEBUG | false |

To copy the Firebase service account JSON using PowerShell:

```powershell
Get-Content .\ServiceAccountKey.json -Raw | ConvertFrom-Json | ConvertTo-Json -Depth 100 -Compress | Set-Clipboard
```

Paste the copied JSON into the `FIREBASE_SERVICE_ACCOUNT` environment variable.

Save the configuration and redeploy the application.

The Firebase service account JSON must never be uploaded to the public GitHub repository.

## Firestore Connection Test

**Local Connection:**

http://127.0.0.1:5009/api/health

**Cloud Connection:**

https://jonardalipala-powertrack.vercel.app/api/health

A successful response should contain:

```json
{
    "ok": true
}
```

## Server Configuration

| Configuration | Value |
|---|---|
| Application | PowerTrack |
| Theme | Crimson Circuit |
| Local Host | 127.0.0.1 |
| Local Port | 5009 |
| Debug Mode | Disabled |
| Database | Firebase Cloud Firestore |
| Local Server | Flask |
| Cloud Server | Vercel |

## Project Structure

```text
PowerTrack/
├── app.py
├── firebase_config.py
├── seed_data.py
├── main.py
├── requirements.txt
├── vercel.json
├── README.md
├── .env
├── .env.example
├── .gitignore
├── ServiceAccountKey.json
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

The `.env` and `ServiceAccountKey.json` files are for local configuration only and must remain private.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/health | Check database connection |
| GET | /api/consumers | Retrieve consumers |
| POST | /api/consumers | Add consumer |
| GET | /api/meter_readings | Retrieve meter readings |
| POST | /api/meter_readings | Add meter reading |
| GET | /api/bills | Retrieve bills |
| POST | /api/bills | Create electricity bill |
| GET | /api/{collection}/{id} | View individual record |
| PUT | /api/{collection}/{id} | Update record |
| DELETE | /api/{collection}/{id} | Delete record |

## Security and Data Validation

The system implements the following database security and validation measures:

- Firebase service account authentication
- Environment variable configuration
- Required field validation
- Email and contact number validation
- Duplicate account and meter number prevention
- Duplicate monthly meter reading prevention
- Duplicate monthly bill prevention
- Nonnegative numerical input validation
- Payment date validation
- Firestore transaction-based operations
- Protection against deleting linked records

The following files and directories must be excluded from GitHub:

```gitignore
.env
ServiceAccountKey.json
.venv/
venv/
__pycache__/
.idea/
*.pyc
```

## Scope and Limitations

PowerTrack focuses on electricity consumer management, meter reading records, billing calculations, and payment status monitoring.

The system requires an internet connection to communicate with Firebase Cloud Firestore. Meter readings and payment information are entered manually.

The system does not include:

- Physical electricity meter integration
- Automatic hardware readings
- Online payment processing
- SMS payment notifications
- User login and role-based authentication

The Vercel deployment is intended for academic demonstration using fictional records. Firebase service account authentication protects database credentials but does not authenticate website visitors. Public access should be restricted until application-level authentication and authorization are implemented.

## System Testing

The following operations should be verified before final submission:

- Firebase Firestore connectivity
- Vercel website accessibility
- Adding, viewing, updating, and deleting consumer records
- Recording monthly meter readings
- Automatic electricity consumption calculation
- Automatic electricity bill calculation
- Updating payment status
- Searching and filtering records
- Preventing duplicate records
- Preventing invalid meter readings
- Protecting linked database records
- CSV report export
- Responsive website layout
- Dark and light mode functionality

## Academic Information

| Information | Details |
|---|---|
| Project Title | PowerTrack — Electricity Consumption and Billing Management System |
| System Theme | Crimson Circuit |
| Subject | Advanced Database |
| Activity | Final Practical Activity |
| Database | Firebase Cloud Firestore |
| Development Environment | PyCharm |
| Deployment Platform | Vercel |
| Academic Year | 2026–2027 |

## Conclusion

PowerTrack demonstrates the practical implementation of a cloud-based NoSQL database using Firebase Cloud Firestore and Python Flask.

It integrates interconnected database collections, CRUD operations, data validation, automated billing calculations, payment monitoring, and an interactive web interface into a centralized electricity consumption and billing management system.

Through GitHub and Vercel, the project also demonstrates source code management and cloud-based application deployment.

---

**⚡ PowerTrack — Crimson Circuit**

*Track Consumption. Manage Bills. Power Smarter.*
