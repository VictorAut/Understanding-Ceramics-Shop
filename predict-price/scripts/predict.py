import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import PolynomialFeatures

# Load the model
with open('../models/price-predictor', 'rb') as file:
    model = pickle.load(file)

def predict_pot(pot):
    """Predicts a penguin's species based on dimensions."""

    # Create a dataframe matching the model's X order
	X = pd.DataFrame(columns=['height',
								'materials_Earthenware',
								'materials_Porcelain',
								'materials_Stoneware',
								'technique_Thrown',
								'firing_Gas',
								'firing_Raku',
								'firing_Wood',
								'decoration_Lustre',
								'decoration_Sgraffito',
								'decoration_Slip decoration',
								'decoration_Terra Sigillata',
								'length'])

	# Append the pot row to it

	X = X.append(pot, ignore_index=True)
	
	# Define a PolynomialFeatures transformer with degree=2 and include_bias=False
	poly = PolynomialFeatures(degree=2, include_bias=False)

	X_poly = poly.fit_transform(X)
	X_poly = pd.DataFrame(data=X_poly, columns=poly.get_feature_names(X.columns))

    # Return a prediction
    return np.exp(model.predict(X_poly)[0])