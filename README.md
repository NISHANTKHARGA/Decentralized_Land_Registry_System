 Blockchain-Based Land Registry System
📋 Project Overview
A decentralized land registry system built on blockchain technology that ensures secure, transparent, and immutable record-keeping of land ownership and transactions. Each land record is stored as a block in the blockchain, linked cryptographically to previous records, making it tamper-proof and verifiable.

✨ Key Features
🔗 Blockchain Implementation: Custom blockchain implementation with cryptographic hashing (SHA-256)

📝 Record Management: Add and retrieve land records linked to UID numbers

🔍 History Tracking: View complete history of any land/property by UID number

✅ Data Validation: Strict validation for UID numbers, names, ages, and land descriptions

📊 Blockchain Viewer: Visual representation of the entire blockchain with block details

🔐 Immutable Records: Once added, records cannot be modified or deleted

🌐 Web Interface: User-friendly web interface for all operations

📱 Responsive Design: Works on desktop, tablet, and mobile devices

🔎 Search Functionality: Search records by UID number

📈 Statistics Dashboard: View blockchain statistics and metrics

🛠️ Technology Stack
Backend: Python Flask

Frontend: HTML5, CSS3, JavaScript

Blockchain: Custom implementation

Hashing: SHA-256 (via hashlib)

Templates: Jinja2

Development Server: Flask built-in server

land-registry-blockchain/
│
├── app.py                          # Main Flask application
├── requirements.txt                 # Python dependencies
│
├── templates/                       # HTML templates
│   ├── index.html                   # Landing page
│   ├── blockchain.html              # Blockchain viewer
│   ├── record.html                   # Single record view
│   ├── patient_records.html          # Patient history view
│   ├── error.html                     # Error page
│   ├── 404.html                       # 404 error page
│   └── 500.html                       # 500 error page
│
└── README.md                         # Project documentation

🚀 Installation & Setup
Prerequisites
Python 3.7 or higher

pip (Python package manager)

Web browser (Chrome, Firefox, etc.)

Step-by-Step Installation

1. Clone the repository
git clone https://github.com/NISHANTKHARGA/Decentralized_Land_Registry_System.git
cd land-registry-blockchain

2. Create a virtual environment (recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install flask
Or create a requirements.txt file:
Flask==2.3.2
Then run:
pip install -r requirements.txt

4. Run the application
python app.py

5. Access the application
Open your web browser and navigate to:
 http://127.0.0.1:5000

💻 Usage Guide
1. Adding a New Land Record
Navigate to the homepage

Fill in the "Add New Land Record" form:

Full Name: Owner's name (letters and spaces only)

Age: Owner's age (18-120 years)

Land History: Description, survey number, location, etc.

UID number: number

Click "Add Record to Blockchain"

The record will be added as a new block and you'll be redirected to view the blockchain

2. Viewing Blockchain
Click "View Complete Blockchain" on the homepage

See all blocks with details:

Timestamp

Owner information

Land details

Cryptographic hashes

Block status (Genesis/Latest/Verified)

3. Searching Records by UID
Enter a UID number in the search form

Click "Get Person land History"

View all records associated with that Aadhar number

4. API Endpoints
The system also provides RESTful API endpoints:

GET /api/blockchain - Get entire blockchain as JSON

POST /api/add_record - Add record via JSON

GET /stats - Get blockchain statistics

GET /verify - Verify blockchain integrity

🔒 Data Validation Rules
Field	Validation Rules
Name	Only letters and spaces, minimum 2 characters
Age	Between 18 and 120 years
UID number, numbers only
Land Description	Minimum 10 characters
🔗 Blockchain Structure
Each block contains:

Timestamp: When the record was created

Name: Owner's name

Age: Owner's age

UID: number

Land: Land description/history

Previous Hash: Hash of the previous block

Current Hash: SHA-256 hash of current block

🧪 Testing
Sample Data (Optional)
To add sample data for testing, uncomment the sample data section in app.py:
# Sample data with UID numbers
sample_records = [
    ("John Doe", "123456789012", 35, "Land parcel #123, 2 acres, agricultural land"),
    ("Jane Smith", "987654321098", 42, "Land parcel #456, 1.5 acres, residential plot"),
    ("Bob Johnson", "123456789012", 35, "Land parcel #789, 3 acres, commercial zone")
]

Test Cases
1. Add valid record: All fields correctly filled

2. Add invalid UID: Test by entering letter in place of number

3. Add invalid age: Test with age <18 or >120

4. Search existing UID number: Should return records

5. Search non-existent UID number: Should show error

6. View empty blockchain: When no records added

🌐 Browser Compatibility
Chrome (latest)

Firefox (latest)

Safari (latest)

Edge (latest)

Opera (latest)

Mobile browsers (iOS Safari, Chrome for Android)

🔐 Security Features
Cryptographic Hashing: Each block is secured with SHA-256

Immutable Chain: Blocks are linked cryptographically

Input Validation: All user inputs are validated

Error Handling: Comprehensive error handling

No Data Modification: Once added, records cannot be changed

📊 Performance Considerations
Blockchain Size: Stored in memory (for demo purposes)

For Production: Consider using a database

Hash Calculation: O(n) for verification

Search: Linear search (can be optimized with indexing)

🚧 Limitations & Future Improvements
Current Limitations
Blockchain stored in memory (lost on server restart)

No user authentication

Linear search for records

Single-node blockchain

Planned Improvements
Persistent storage (database)

User authentication and roles

Merkle trees for efficient verification

P2P network for distributed blockchain

Smart contracts for automated transactions

Digital signatures for verification

Export/Import blockchain data

Multi-language support

🤝 Contributing
echo "# Decentralized_Land_Registry_System" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/NISHANTKHARGA/Decentralized_Land_Registry_System.git
git push -u origin main


📧 Contact
Project Maintainer: Nishant Kumar Kharga

Email: nishantkumarkharga9818@gmail.com

GitHub: https://github.com/NISHANTKHARGA

Project Link: https://github.com/NISHANTKHARGA/Decentralized_Land_Registry_System.git

🙏 Acknowledgments
Blockchain concept by Satoshi Nakamoto

Flask framework documentation

Contributors and testers

📚 Additional Resources
Blockchain Explained

Flask Documentation

SHA-256 Algorithm

🐛 Known Issues
Browser refresh may lose blockchain data (in-memory storage)

Very long land descriptions may break table layout

No export functionality for blockchain data

📞 Support
For support, email: nishantkumarkharga9818@gmail.com or create an issue on GitHub.