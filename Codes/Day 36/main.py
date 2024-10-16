import requests
from newsapi import NewsApiClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject,body):
    my_email = "examplemail@email.com"
    password = "APP_PASSWORD"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = my_email
    message["To"] = "examplemail@email.com"

    body_part = MIMEText(body, "plain", "utf-8")

    message.attach(body_part)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="examplemail@email.com",
            msg=message.as_string()

        )


#params for Stock
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TSI = "TIME_SERIES_INTRADAY"
INTV = "60min"
APP_KEY_STOCK = "API KEY"
NEWS_API_KEY = "API KEY"
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
        arrow = "🔺" if percentage_change > 0 else "🔻"
        formatted_percentage = f"{arrow}{abs(percentage_change):.2f}%"

        print(f"Latest close: {latest_close}")
        print(f"Previous close: {previous_close}")
        print(f"Percentage change: {percentage_change:.2f}%")

        # Check if the percentage difference is greater than 5%
        if abs(percentage_change) >= 5:
        # if news_test == True:
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

                # Store all articles in a list
                news_list = []
                for i, article in enumerate(articles, start=1):
                    title = article['title']
                    description = article['description']
                    
                    formatted_article = f"""
                                            {COMPANY_NAME}: {formatted_percentage}
                                            Headline: {title}
                                            Brief: {description}
"""
                    news_list.append(formatted_article)

                # Combine all articles into one email body
                email_body = "\n\n".join(news_list)
                subject = f"Stock News for {COMPANY_NAME}"
                
                # Send all news in one email
                send_mail(subject=subject, body=email_body)
            else:
                print("No news articles found.")
        else:
            print("No significant change.")
    else:
        print("Not enough data to compare.")
