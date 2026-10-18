import os
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# --- Model load (relative path + cache) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'stock_prediction_model.keras')

@st.cache_resource
def get_model():
    return load_model(MODEL_PATH)

model = get_model()

st.header('Stock Market Prediction')

stock = st.text_input('Enter Stock Symbol', 'GOOG')
start = '2012-01-01'
end = '2022-12-31'

data = yf.download(stock, start, end)

# Naye yfinance me MultiIndex columns aate hain, unhe flatten karo
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

if data.empty:
    st.error('Is symbol ka data nahi mila. Symbol check karke dobara try karo.')
    st.stop()

st.subheader('Stock Price Trend Analysis')
st.write(data)

split = int(len(data) * 0.80)
data_train = pd.DataFrame(data.Close[:split])
data_test = pd.DataFrame(data.Close[split:])

# Scaler sirf training data par fit karo
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(data_train)

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scale = scaler.transform(data_test)

st.subheader('Stock Price with 50-Day Moving Average')
ma_50_days = data.Close.rolling(50).mean()
fig1 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r', label='MA 50')
plt.plot(data.Close, 'g', label='Price')
plt.legend()
st.pyplot(fig1)

st.subheader('Stock Price with 50-Day and 100-Day Moving Average')
ma_100_days = data.Close.rolling(100).mean()
fig2 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r', label='MA 50')
plt.plot(ma_100_days, 'b', label='MA 100')
plt.plot(data.Close, 'g', label='Price')
plt.legend()
st.pyplot(fig2)

st.subheader('Stock Price with 100-Day and 200-Day Moving Average')
ma_200_days = data.Close.rolling(200).mean()
fig3 = plt.figure(figsize=(8, 6))
plt.plot(ma_100_days, 'r', label='MA 100')
plt.plot(ma_200_days, 'b', label='MA 200')
plt.plot(data.Close, 'g', label='Price')
plt.legend()
st.pyplot(fig3)

x = []
y = []
for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i, 0])

x, y = np.array(x), np.array(y)

predict = model.predict(x)

scale = 1 / scaler.scale_
predict = predict * scale
y = y * scale

st.subheader('Original Price vs Predicted Price')
fig4 = plt.figure(figsize=(8, 6))
plt.plot(y, 'g', label='Original Price')
plt.plot(predict, 'r', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig4)
