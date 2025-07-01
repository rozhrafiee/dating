from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzy_logic import get_decision

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/decision', methods=['POST'])
def make_decision():
    try:
        # Get data from frontend
        data = request.json
        
        # Validate input data
        required_fields = [
            'trust', 'kindness', 'emotional_stability', 
            'financial_stability', 'attention', 'effort',
            'physical_attraction', 'princess_treatment'
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
            if not 0 <= data[field] <= 10:
                return jsonify({'error': f'{field} must be between 0 and 10'}), 400
        
        # Get decision from fuzzy logic system
        result = get_decision(data)
        
        return jsonify({
            'decision': result,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)