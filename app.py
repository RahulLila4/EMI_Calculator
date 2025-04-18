from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = total_payment = total_interest = None
    principal = annual_rate = tenure = None
    interest_list = []
    principal_list = []

    if request.method == 'POST':
        principal = float(request.form['principal'])
        annual_rate = float(request.form['rate'])
        tenure = int(request.form['tenure'])

        monthly_rate = annual_rate / (12 * 100)
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
        total_payment = emi * tenure
        total_interest = total_payment - principal

        balance = principal
        for _ in range(tenure):
            interest = balance * monthly_rate
            principal_component = emi - interest
            balance -= principal_component
            interest_list.append(round(interest, 2))
            principal_list.append(round(principal_component, 2))

    return render_template('index.html',
                           emi=emi,
                           total_payment=total_payment,
                           total_interest=total_interest,
                           principal=principal,
                           interest_list=interest_list,
                           principal_list=principal_list,
                           tenure=tenure)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
