from neuralprophet import NeuralProphet
import pandas as pd
from transaction_service import get_all_transactions_for_store, get_transactions_for_store_date_range

result = get_all_transactions_for_store(1)
# result = get_transactions_for_store_date_range(
#     1, '2013-01-01', '2013-01-31')
df = pd.DataFrame(result)

m = NeuralProphet()
metrics = m.fit(df, freq="D")

future = m.make_future_dataframe(df=df, periods=30)
forecast = m.predict(df=future)

print(forecast.to_dict('records'))
# fig_forecast = m.plot(forecast)
# fig_forecast.show()
