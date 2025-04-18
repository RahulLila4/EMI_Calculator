from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    total_payment = emi * tenure_months
    total_interest = total_payment - principal
    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = total_payment = total_interest = None
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            annual_rate = float(request.form['rate'])
            tenure = int(request.form['tenure'])

            emi, total_payment, total_interest = calculate_emi(principal, annual_rate, tenure)
        except ValueError:
            emi = total_payment = total_interest = "Invalid input"

    return render_template('index.html', emi=emi, total_payment=total_payment, total_interest=total_interest)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local
    app.run(host='0.0.0.0', port=port)
