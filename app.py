from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_emi(principal, annual_rate, tenure):
    monthly_rate = annual_rate / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    total_payment = emi * tenure
    total_interest = total_payment - principal
    return emi, total_payment, total_interest

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = total_payment = total_interest = None
    if request.method == 'POST':
        principal = float(request.form['principal'])
        annual_rate = float(request.form['rate'])
        tenure = int(request.form['tenure'])
        
        emi, total_payment, total_interest = calculate_emi(principal, annual_rate, tenure)
    
    return render_template('index.html', emi=emi, total_payment=total_payment, total_interest=total_interest)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use 5000 locally, Render's port in production
    app.run(host='0.0.0.0', port=port)
