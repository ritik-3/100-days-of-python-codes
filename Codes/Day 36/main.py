import requests
from newsapi import NewsApiClient
import smtplib #("working on it")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TSI = "TIME_SERIES_INTRADAY"
INTV = "60min"
APP_KEY_STOCK = "api key"
NEWS_API_KEY = "api key"
news_test = True

# Alpha Vantage API URL and parameters
api_url_stock = "https://www.alphavantage.co/query"
parameters_stock = {
    "function": TSI,
    "symbol": STOCK,
    "interval": INTV,
    "apikey": APP_KEY_STOCK
}

# Fetch stock data
response_stock = requests.get(api_url_stock, params=parameters_stock)
response_stock.raise_for_status()
stock_data = response_stock.json()

# Check if the necessary time series data is available
if "Time Series (60min)" not in stock_data:
    print("Error: Could not retrieve stock data")
else:
    # Extract the time series data (sorted by date)
    time_series = stock_data["Time Series (60min)"]
    time_series_list = list(time_series.items())

    # Get the most recent two trading periods
    if len(time_series_list) >= 2:
        latest_period = time_series_list[0][1]  # Most recent time period
        previous_period = time_series_list[1][1]  # Second most recent period

        # Extract the closing prices
        latest_close = float(latest_period["4. close"])
        previous_close = float(previous_period["4. close"])

        # Calculate the percentage difference
        price_diff = latest_close - previous_close
        percentage_change = (price_diff / previous_close) * 100

        print(f"Latest close: {latest_close}")
        print(f"Previous close: {previous_close}")
        print(f"Percentage change: {percentage_change:.2f}%")

        # Check if the percentage difference is greater than 5%

        #if abs(percentage_change) >= 5:
        if news_test == True:
            print("Significant change detected. Fetching news...")

            # NewsAPI URL and parameters
            api_url_news = "https://newsapi.org/v2/everything"
            parameters_news = {
                "q": COMPANY_NAME,  # Search query for the company name
                "sortBy": "relevancy",
                "apiKey": NEWS_API_KEY,
                "language": "en"
            }

            # Fetch news data
            response_news = requests.get(api_url_news, params=parameters_news)
            response_news.raise_for_status()
            news_data = response_news.json()

            # Check if articles are available
            if news_data["totalResults"] > 0:
                articles = news_data["articles"][:3]  # Get the top 3 articles

                # Print the top 3 news articles
                for i, article in enumerate(articles, start=1):
                    print(f"\nArticle {i}:")
                    print(f"Title: {article['title']}")
                    print(f"Description: {article['description']}")
                    print(f"URL: {article['url']}")
            else:
                print("No news articles found.")
        else:
            print("No significant change.")
    else:
        print("Not enough data to compare.")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

