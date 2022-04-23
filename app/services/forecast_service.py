import os
import pickle
from datetime import datetime

import pandas as pd

from app.services.transaction_service import get_all_transactions_for_store


def get_forecast(store_id, start_date, end_date):
    # Convert start_date and end_date to datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    last_record_date = datetime.strptime('2017-08-15', '%Y-%m-%d')

    # Calculate number of periods
    periods = (end_date - last_record_date).days

    # Calculate number of records to return
    num_records = ((end_date - start_date)).days - 1

    # Load model
    filename = f'store_{store_id}.pkl'
    model = pickle.load(open(os.path.dirname(__file__) +
                        '/../models/' + filename, 'rb'))

    # Get dataframe of transactions for store
    transactions = get_all_transactions_for_store(store_id)
    df = pd.DataFrame(transactions)

    # Create forecast
    future = model.make_future_dataframe(df=df, periods=periods)
    forecast = model.predict(df=future)

    # Drop residual1 column from forecast
    forecast = forecast.drop(columns=['residual1'], axis=1)

    # Convert forecast to array of dicts
    forecast_dict = forecast.to_dict('records')

    return forecast_dict[-num_records:]
