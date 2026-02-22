from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import hashlib

app = Flask(__name__)

# list to store blockchain
blockchain = []

# Patient record class
class PatientRecord:
    def __init__(self, name, uid, age, land):
        self.timestamp = datetime.now()
        self.name = name
        self.age = age
        self.uid = uid
        self.land = land
        self.previous_hash = self.calculate_previous_hash()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the hash of the current record"""
        hash_data = str(self.timestamp) + self.name + str(self.uid) + str(self.age) + self.land + str(self.previous_hash)
        return hashlib.sha256(hash_data.encode()).hexdigest()

    def calculate_previous_hash(self):
        """Get the hash of the previous block in the blockchain"""
        if len(blockchain) > 0:
            previous_record = blockchain[-1]
            return previous_record.hash
        else:
            return "0" * 64  # Return 64 zeros for genesis block

    def to_dict(self):
        """Convert record to dictionary for easy serialization"""
        return {
            'timestamp': self.timestamp,
            'name': self.name,
            'age': self.age,
            'uid': self.uid,
            'land': self.land,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }

# Context processor to make current datetime available in all templates
@app.context_processor
def utility_processor():
    return {'now': datetime.now}

# Route to add new record to blockchain
@app.route('/add_record', methods=['POST'])
def add_record():
    try:
        # Get form data
        name = request.form['name']
        age = request.form['age']
        land = request.form['land']
        uid = request.form['uid']

        # Validate input
        if not all([name, age, land, uid]):
            return "Error: All fields are required!", 400

        # Create a new patient record
        record = PatientRecord(name, uid, age, land)

        # Add the patient record to the blockchain
        blockchain.append(record)

        # Redirect to view the blockchain after adding
        return redirect(url_for('view_blockchain'))
    
    except Exception as e:
        return f"Error adding record: {str(e)}", 500

# Route to get specific patient record from blockchain
@app.route('/get_records', methods=['GET'])
def get_record():
    try:
        uid = request.args.get('uid')
        
        if not uid:
            return "Error: UID is required!", 400
        
        # Search for the record with matching UID
        for block in blockchain:
            if str(block.uid) == str(uid):
                return render_template('record.html', record=block)
        
        return f'Record not found for UID: {uid}', 404
    
    except Exception as e:
        return f"Error retrieving record: {str(e)}", 500

# Route to display the entire blockchain
@app.route('/view_blockchain', methods=['GET'])
def view_blockchain():
    try:
        return render_template('blockchain.html', blockchain=blockchain)
    except Exception as e:
        return f"Error viewing blockchain: {str(e)}", 500

# Route to get complete history of a patient by UID
@app.route('/get_history', methods=['GET'])
def get_history():
    try:
        uid = request.args.get('uid')
        
        if not uid:
            return "Error: UID is required!", 400
        
        # Collect all records with matching UID
        history = []
        for block in blockchain:
            if str(block.uid) == str(uid):
                history.append(block)
        
        if len(history) >= 1:
            return render_template('patient_records.html', all_records=history, uid=uid)
        else:
            return f'No records found for UID: {uid}', 404
    
    except Exception as e:
        return f"Error retrieving history: {str(e)}", 500

# Route to get blockchain statistics
@app.route('/stats', methods=['GET'])
def get_stats():
    """Return blockchain statistics as JSON"""
    try:
        unique_uids = len(set(str(block.uid) for block in blockchain))
        stats = {
            'total_blocks': len(blockchain),
            'unique_uids': unique_uids,
            'latest_block': len(blockchain),
            'genesis_block': blockchain[0].to_dict() if blockchain else None,
            'latest_block_data': blockchain[-1].to_dict() if blockchain else None
        }
        return stats
    except Exception as e:
        return {'error': str(e)}, 500

# Route to verify blockchain integrity
@app.route('/verify', methods=['GET'])
def verify_blockchain():
    """Verify the integrity of the blockchain"""
    try:
        verification_results = []
        is_valid = True
        
        for i in range(len(blockchain)):
            current_block = blockchain[i]
            
            # Verify current block's hash
            calculated_hash = current_block.calculate_hash()
            if calculated_hash != current_block.hash:
                is_valid = False
                verification_results.append({
                    'block_index': i,
                    'status': 'INVALID',
                    'issue': 'Hash mismatch',
                    'uid': current_block.uid
                })
            
            # Verify previous hash linkage (except genesis block)
            if i > 0:
                previous_block = blockchain[i-1]
                if current_block.previous_hash != previous_block.hash:
                    is_valid = False
                    verification_results.append({
                        'block_index': i,
                        'status': 'INVALID',
                        'issue': 'Broken chain linkage',
                        'uid': current_block.uid
                    })
            
            if i == 0 and current_block.previous_hash != "0" * 64:
                is_valid = False
                verification_results.append({
                    'block_index': i,
                    'status': 'INVALID',
                    'issue': 'Invalid genesis block',
                    'uid': current_block.uid
                })
        
        return {
            'is_valid': is_valid,
            'total_blocks': len(blockchain),
            'verification_details': verification_results
        }
    
    except Exception as e:
        return {'error': str(e)}, 500

# Route to clear blockchain (for testing purposes)
@app.route('/clear_blockchain', methods=['POST'])
def clear_blockchain():
    """Clear the entire blockchain (use with caution)"""
    try:
        global blockchain
        blockchain = []
        return redirect(url_for('view_blockchain'))
    except Exception as e:
        return f"Error clearing blockchain: {str(e)}", 500

# Route to get block by index
@app.route('/block/<int:index>', methods=['GET'])
def get_block_by_index(index):
    """Get a specific block by its index"""
    try:
        if 0 <= index < len(blockchain):
            block = blockchain[index]
            return render_template('record.html', record=block)
        else:
            return f"Block index {index} not found. Total blocks: {len(blockchain)}", 404
    except Exception as e:
        return f"Error retrieving block: {str(e)}", 500

# API endpoint to add record via JSON (for programmatic access)
@app.route('/api/add_record', methods=['POST'])
def api_add_record():
    """API endpoint to add record using JSON"""
    try:
        data = request.get_json()
        
        if not data:
            return {'error': 'No JSON data provided'}, 400
        
        # Validate required fields
        required_fields = ['name', 'age', 'land', 'uid']
        for field in required_fields:
            if field not in data:
                return {'error': f'Missing required field: {field}'}, 400
        
        # Create and add record
        record = PatientRecord(
            name=data['name'],
            uid=data['uid'],
            age=data['age'],
            land=data['land']
        )
        
        blockchain.append(record)
        
        return {
            'message': 'Record added successfully',
            'block_index': len(blockchain) - 1,
            'record': record.to_dict()
        }, 201
    
    except Exception as e:
        return {'error': str(e)}, 500

# API endpoint to get blockchain data
@app.route('/api/blockchain', methods=['GET'])
def api_get_blockchain():
    """API endpoint to get blockchain data as JSON"""
    try:
        blockchain_data = [block.to_dict() for block in blockchain]
        # Convert datetime objects to strings for JSON serialization
        for block in blockchain_data:
            block['timestamp'] = block['timestamp'].isoformat()
        
        return {
            'total_blocks': len(blockchain_data),
            'blockchain': blockchain_data
        }
    except Exception as e:
        return {'error': str(e)}, 500

# Landing page route
@app.route('/')
def index():
    """Render the landing page"""
    return render_template('index.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500

# Run the application
if __name__ == '__main__':
    # Add some sample data for testing (optional)
    # Uncomment the following lines to add sample data when starting the app
    
    """
    # Sample data for testing
    sample_records = [
        ("John Doe", "UID001", 35, "Land parcel #123, 2 acres, agricultural land"),
        ("Jane Smith", "UID002", 42, "Land parcel #456, 1.5 acres, residential plot"),
        ("Bob Johnson", "UID001", 35, "Land parcel #789, 3 acres, commercial zone")
    ]
    
    for name, uid, age, land in sample_records:
        record = PatientRecord(name, uid, age, land)
        blockchain.append(record)
    """
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)