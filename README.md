🧮 EMI Calculator Web App

A simple and responsive **EMI (Equated Monthly Installment) Calculator** built using **Python Flask**, with dynamic chart visualization using **Chart.js**. This tool helps users calculate their monthly EMI, total repayment amount, and interest payable based on user inputs.

---

🚀 Features

- Input loan principal, annual interest rate, and tenure (in months)
- Instant EMI, total interest, and total repayment calculations
- Clean, responsive UI using HTML + CSS
- Visual breakdown using **interactive line charts**
- Integrated logo for branding
- Deployable via **Render** with ease

---

🖼️ Preview

![image](https://github.com/user-attachments/assets/a218f888-3236-4868-874a-d3bde59781bd)

---

🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Chart.js)
- **Backend**: Python (Flask)
- **Deployment**: Render

---

💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/EMI_Calculator.git
cd EMI_Calculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the application
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

🌐 Deployment on Render

1. Push this project to your GitHub
2. Create a new Web Service on [Render](https://render.com/)
3. Use the following setup:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
4. Make sure `render.yaml` is present for configuration

> Docs: [Render Port Binding Guide](https://render.com/docs/web-services#port-binding)

---

 📁 Project Structure

```
EMI_Calculator/
├── static/
│   └── smg_logo.png
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── render.yaml
└── README.md

```

 ✨ To-Do / Future Features

- Amortization table with monthly breakdown
- Option to download results as PDF/Excel
- Add dark mode
- Currency formatting and regional support

---

 🙌 Author

Built by Rahul Lila. Contributions and suggestions are welcome!
