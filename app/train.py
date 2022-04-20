import os
import pickle
import pandas as pd
from neuralprophet import NeuralProphet
from transaction_service import get_all_transactions_for_store
from store_service import get_all_stores

stores = get_all_stores()

for store in stores:
    store_id = store['id']

    # Get training data
    result = get_all_transactions_for_store(store_id)

    # Convert training data to Panda DataFrame
    df = pd.DataFrame(result)

    # Create NeuralProphet model
    model = NeuralProphet()
    metrics = model.fit(df, freq="D")

    filename = f'store_{store_id}.pkl'
    pickle.dump(model, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)) + '/models', filename), 'wb'))

    print(filename, 'saved to models')
