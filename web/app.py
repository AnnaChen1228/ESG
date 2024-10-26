from flask import Flask, render_template,request,jsonify
import requests
import os
from dotenv import load_dotenv
import preprocessing as preprocessing

app = Flask(__name__)
load_dotenv()
DIFY_API_URL=os.getenv('DIFY_API_URL')
WORKFLOW_DIFY_API_KEY=os.getenv('RULE_DIFY_API_KEY')

REPORT_DIFY_API_KEY=os.getenv('REPORT_DIFY_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/generator_reporter')
def generator_reporter():
    return render_template('generator_reporter.html')

@app.route('/check_reporter')
def check_reporter():
    return render_template('check_reporter.html')

@app.route('/gonvernment_rule')
def gonvernment_rule():
    return render_template('gonvernment_rule.html')

@app.route('/rule', methods=['POST'])
def dify_rule():
    user_message = request.json.get('message')  # 取得前端傳送的訊息
    print(user_message)
    try:
        response = requests.post(
            DIFY_API_URL,
            headers={
                'Authorization': f'Bearer {WORKFLOW_DIFY_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'inputs': {'query': user_message},
                'response_mode': 'blocking',
                'user': 'abc-123'
            }
        )

        if response.status_code != 200:
            app.logger.error(f"Error: Received status code {response.status_code}")
            return jsonify({'response': '無法獲得有效的回應'}), 500

        try:
            response_data = response.json()
            workflow_response = response_data.get('data', {}).get('outputs', {}).get('text', '無法獲得回應')
            print(workflow_response)
            response=preprocessing.pre_rule(workflow_response)
            print(response)
            return jsonify(response),200
        except (requests.exceptions.JSONDecodeError, KeyError) as e:
            app.logger.error(f"Error parsing response: {e}")
            return jsonify({'response': 'API 回應的格式無效'}), 500

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error during API request: {e}")
        return jsonify({'response': f"Error: {str(e)}"}), 500
    
# @app.route('/report', methods=['POST'])
# def dify_report():
#     user_message = request.json.get('message')  # 取得前端傳送的訊息
#     print(user_message)
#     try:
#         response = requests.post(
#             DIFY_API_URL,
#             headers={
#                 'Authorization': f'Bearer {REPORT_DIFY_API_KEY}',
#                 'Content-Type': 'application/json'
#             },
#             json={
#                 'inputs': {'query': user_message},
#                 'response_mode': 'blocking',
#                 'user': 'abc-123'
#             }
#         )

#         if response.status_code != 200:
#             app.logger.error(f"Error: Received status code {response.status_code}")
#             return jsonify({'response': '無法獲得有效的回應'}), 500

#         try:
#             response_data = response.json()
#             workflow_response = response_data.get('data', {}).get('outputs', {}).get('text', '無法獲得回應')
#             print(workflow_response)
#             response=preprocessing.pre_rule(workflow_response)
#             return jsonify(response)
#         except (requests.exceptions.JSONDecodeError, KeyError) as e:
#             app.logger.error(f"Error parsing response: {e}")
#             return jsonify({'response': 'API 回應的格式無效'}), 500

#     except requests.exceptions.RequestException as e:
#         app.logger.error(f"Error during API request: {e}")
#         return jsonify({'response': f"Error: {str(e)}"}), 500
    
# @app.route('/write_rule')
# def write_rule():
#     return render_template('write_rule.html')

# @app.route('/reporter')
# def reporter():
#     return render_template('reporter.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
