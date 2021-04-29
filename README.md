
# Ceramics Shop Analysis

***

Understanding the body of products that constitute your store, and what insights can be derived from your products, is important for any business.

_In this project I aim to understand how the ceramics from a large Ceramics shop in London can be grouped, how they can be priced, and how they can be categorised based on prior analysis. The insights would allow for this shop to better understand how they can present their products, or how they can best market their products_

__Method:__

1. Scrape through the shop's body of approx 1000 pots.
2. Parse HTML using BeautifulSoup into a DataFrame.
3. Cluster the data using KPrototypes on ~8 features. Check the quality of clustering using embedding methods such as TSNE and PCA. Generate a list of classes.
4. Build a number of regressors to predict the price of an item of ceramics.
5. Build a classification model to predict an items class.
6. Use a neural network to compare the results of a neural network trained to predict the above based on the thumbnail image of an item.
7. Long term: scrape the data monthly to generate a list of sales. Use time series to predict future sales.
8. Report on the results to the business to deliver impactful results

__Results:__

1. __5 classes__ of pots generated.
2. __XX%__ accuracy in predicting the price of an item from numerical and categorical features.
3. __XX%__ accuracy in predicting the class of an item. This can be used for __marketing__ strategies by the shop.
4. __XX__ sales predicted for the time period __YY__.
5. __XX%__ accuracy in predicting the price of an item using a trained neural network.
