# 📈 Stock Market Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-LSTM-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A machine learning web application that predicts stock market prices using historical data and deep learning models (LSTM). Built with Python, Streamlit, and Keras.

---

## 🖥️ Demo




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

## 📖 About the Project

This project is a **Stock Market Price Prediction** web application that leverages **Long Short-Term Memory (LSTM)** neural networks to forecast future stock prices based on historical market data. Users can enter any stock ticker symbol (e.g., `TSLA`, `AAPL`, `GOOG`) and instantly visualize historical trends, moving averages, and model-predicted prices through an interactive dashboard.

The application fetches real-time stock data using **Yahoo Finance (yfinance)**, preprocesses it with MinMaxScaler, and feeds it into a trained LSTM model to generate future price predictions.

---

## ✨ Features

- 🔍 **Live Stock Data** — Fetches real-time and historical OHLCV data via `yfinance`
- 📋 **Stock Trend Table** — Displays historical data: Open, High, Low, Close, Volume
- 📈 **50-Day Moving Average Chart** — Visualizes short-term price momentum
- 📊 **50-Day & 100-Day Moving Average Chart** — Mid-term trend comparison
- 📉 **100-Day & 200-Day Moving Average Chart** — Long-term trend analysis
- 🤖 **LSTM-Based Prediction** — Deep learning model trained on historical closing prices
- 🔴 **Original vs Predicted Price Chart** — Clear visual of actual vs model-predicted prices
- 🌐 **Streamlit Web Interface** — Clean and interactive UI, no frontend coding needed
- 🧪 **Any Stock Supported** — Works with any valid ticker (e.g., `TSLA`, `AAPL`, `GOOG`, `RELIANCE.NS`)

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
├── app.py                         # Main Streamlit application
├── Stock Predictions Model.keras  # Pre-trained LSTM model
├── assets/                        # Screenshots for README
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
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
User enters Stock Ticker (e.g., TSLA)
        ↓
Fetch Historical Data via yfinance
        ↓
Display OHLCV Data Table
        ↓
Compute & Plot Moving Averages (50, 100, 200-day)
        ↓
Preprocess Data (MinMaxScaler + sliding window)
        ↓
Load Pre-trained LSTM Model
        ↓
Generate & Plot Predicted vs Original Price
```

1. **Data Collection** — Historical stock data is downloaded using `yfinance`.
2. **Data Table** — Raw OHLCV (Open, High, Low, Close, Volume) data is displayed.
3. **Moving Averages** — 50-day, 100-day, and 200-day moving averages are computed and plotted.
4. **Preprocessing** — Closing prices are normalized with `MinMaxScaler` and reshaped into 100-day sequences.
5. **Prediction** — The pre-trained LSTM model generates predicted prices.
6. **Visualization** — A final chart overlays the original vs predicted closing prices.

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
2. Enter a **stock ticker symbol** in the input box (e.g., `TSLA`, `AAPL`, `GOOG`, `RELIANCE.NS`)
3. The app will display:
   - 📋 Historical OHLCV data table
   - 📈 Stock Price with **50-Day Moving Average**
   - 📊 Stock Price with **50-Day & 100-Day Moving Average**
   - 📉 Stock Price with **100-Day & 200-Day Moving Average**
   - 🔴 **Original Price vs Predicted Price** chart

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Reyaz**


---

> ⚠️ **Disclaimer**: This project is for **educational purposes only**. Stock market predictions made by this model should **not** be used for actual financial investment decisions.

---

⭐ If you found this project helpful, please consider giving it a **star** on GitHub!
