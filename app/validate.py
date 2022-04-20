import pandas as pd
import numpy as np
from neuralprophet import NeuralProphet

from transaction_service import get_transactions_for_store_date_range


# Function to calculate the mean absolute percentage error (MAPE) of the model
def get_mape(actual, predicted):
    return np.mean(np.abs((actual - predicted) / actual)) * 100


# Get training data
result = get_transactions_for_store_date_range(1, '2013-01-01', '2017-06-30')
# Get control data
control = get_transactions_for_store_date_range(1, '2017-07-01', '2017-07-31')

# Convert control data list of dicts to array of the y values
actual = np.array([x['y'] for x in control])

# Convert training data to Panda DataFrame
df = pd.DataFrame(result)

# Create NeuralProphet model
m = NeuralProphet()
m.fit(df, freq="D")

# Create forecast to match our control data period (2017-07-01 to 2017-07-31)
future = m.make_future_dataframe(df=df, periods=31)
forecast = m.predict(df=future)

# Convert forecast to array of the yhat1 values
predicted = np.array([x['yhat1'] for x in forecast.to_dict('records')])

mape = get_mape(actual, predicted)

print("The mean absolute percentage error: ", round(mape, 5), "%")