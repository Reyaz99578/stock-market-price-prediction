# stock-market-price-prediction
# 📈 Stock Market Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-LSTM-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A machine learning web application that predicts stock market prices using historical data and deep learning models (LSTM). Built with Python, Streamlit, and Keras.

---

 Demo

![App Screenshot](https://via.placeholder.com/900x400?text=Stock+Market+Price+Prediction+App)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [How It Works](#-how-it-works)
- [Model Details](#-model-details)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---
About the Project

This project is a **Stock Market Price Prediction** web application that leverages **Long Short-Term Memory (LSTM)** neural networks to forecast future stock prices based on historical market data. Users can enter any stock ticker symbol and visualize both historical trends and predicted prices through an interactive dashboard.

The application fetches real-time stock data using **Yahoo Finance (yfinance)**, preprocesses it, and feeds it into a trained LSTM model to generate future price predictions.

---

✨ Features

- 🔍 **Live Stock Data** — Fetches real-time and historical data via `yfinance`
- 📊 **Interactive Charts** — Visualizes closing price trends and moving averages (MA100, MA200)
- 🤖 **LSTM-Based Prediction** — Deep learning model trained on historical stock data
- 📉 **Prediction vs Actual Plot** — Side-by-side comparison of predicted vs actual prices
- 🌐 **Web Interface** — Clean and user-friendly UI built with Streamlit
- 🧪 **Any Stock Supported** — Works with any valid stock ticker (e.g., AAPL, TSLA, GOOG, RELIANCE.NS)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application framework |
| **Keras / TensorFlow** | LSTM model building and training |
| **yfinance** | Fetching historical stock data |
| **NumPy / Pandas** | Data manipulation and preprocessing |
| **Matplotlib** | Data visualization and charting |
| **Scikit-learn** | Data scaling (MinMaxScaler) |

---

## 📁 Project Structure

```
stock-market-price-prediction/
│
├── app.py                  # Main Streamlit application
├── Stock Predictions Model.keras  # Pre-trained LSTM model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Reyaz99578/stock-market-price-prediction.git
cd stock-market-price-prediction
```

2. **Create a virtual environment** *(recommended)*

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install the required packages**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, install manually:
> ```bash
> pip install streamlit yfinance keras tensorflow numpy pandas matplotlib scikit-learn
> ```

### Running the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## ⚙️ How It Works

```
User enters Stock Ticker
        ↓
Fetch Historical Data (yfinance)
        ↓
Data Preprocessing (MinMaxScaler, sliding window)
        ↓
Load Pre-trained LSTM Model
        ↓
Generate Predictions
        ↓
Visualize Results (Streamlit Charts)
```

1. **Data Collection** — Historical stock data (up to 20 years) is downloaded using `yfinance`.
2. **Preprocessing** — The closing prices are normalized using `MinMaxScaler` and reshaped into sequences for LSTM input.
3. **Prediction** — The pre-trained LSTM model predicts future prices.
4. **Visualization** — Results are plotted with moving averages (MA100, MA200) and a Predicted vs Actual chart.

---

## 🧠 Model Details

| Parameter | Value |
|---|---|
| **Model Type** | LSTM (Long Short-Term Memory) |
| **Input Features** | Closing Price |
| **Sequence Length** | 100 days |
| **Training Split** | 70% train / 30% test |
| **Optimizer** | Adam |
| **Loss Function** | Mean Squared Error (MSE) |
| **Framework** | Keras / TensorFlow |

The model was trained on historical data and saved as `Stock Predictions Model.keras`, which is loaded directly in the app to avoid retraining on each run.

---

## 📝 Usage

1. Open the app in your browser after running `streamlit run app.py`
2. Enter a **stock ticker symbol** in the input box (e.g., `GOOG`, `AAPL`, `TSLA`, `RELIANCE.NS`)
3. The app will display:
   - Raw historical stock data
   - **Moving Averages** — MA100 and MA200 trend lines
   - **Original Price vs MA100 vs MA200** chart
   - **Predicted Price vs Original Price** chart

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a **Pull Request**

---

## 👤 Author

**Reyaz**

---

> ⚠️ **Disclaimer**: This project is for **educational purposes only**. Stock market predictions made by this model should **not** be used for actual financial investment decisions.

---

⭐ If you found this project helpful, please consider giving it a **star** on GitHub!
