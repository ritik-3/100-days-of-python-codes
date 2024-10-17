import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from amadeus import Client, ResponseError

# Amadeus API credentials
amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

# Sheety API URL
sheety_url = 'https://api.sheety.co/your_project/your_sheet/sheet1'

# Email configuration
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
password = "YOUR_EMAIL_PASSWORD"  # Use app password if using Gmail with 2FA

# Fetch data from Sheety
response = requests.get(sheety_url)
if response.status_code == 200:
    sheet_data = response.json()
    
    # Store results for cities with cheaper flights
    cheaper_flights = []
    flight_details = []  # Store other price details for the email

    # Loop through each row in the sheet
    for row in sheet_data["sheet1"]:
        city = row["city"]
        iata_code = row["iataCode"]  # Use the IATA code directly from the sheet
        lowest_price = float(row['lowestPrice'])  # Convert to float for comparison
        
        print(f"Checking flights for City: {city} ({iata_code}), Lowest Price: {lowest_price}")
        
        # Call Amadeus API to find the flight price
        try:
            flight_response = amadeus.shopping.flight_offers_search.get(
                originLocationCode='JFK',  # Default airport (replace with your desired origin code)
                destinationLocationCode=iata_code,  # Use IATA code from the sheet
                departureDate='2024-11-01',  # Example date
                adults=1
            )
            
            # Process the flight data from Amadeus
            if flight_response.data:
                cheapest_flight = min(flight_response.data, key=lambda x: float(x['price']['total']))
                current_price = float(cheapest_flight['price']['total'])
                flight_details.append(f"Cheapest flight to {city} ({iata_code}): {current_price}")

                # Compare the current price with the lowest price from the sheet
                if current_price < lowest_price:
                    cheaper_flights.append({
                        "city": city,
                        "iataCode": iata_code,
                        "current_price": current_price,
                        "lowest_price": lowest_price
                    })
                    print(f"Found a cheaper flight to {city}: {current_price} (less than {lowest_price})")
            else:
                flight_details.append(f"No flights found for {city}")
                print(f"No flights found for {city}")
        except ResponseError as error:
            flight_details.append(f"Error fetching flights for {city}: {error}")
            print(f"Error fetching flights for {city}: {error}")

    # Prepare the email content
    subject = "Today's flight price report"
    body = "Cities with cheaper flights:\n"
    
    if cheaper_flights:
        for flight in cheaper_flights:
            body += f"City: {flight['city']} ({flight['iataCode']}) - Cheapest Price: {flight['current_price']} (Sheet Price: {flight['lowest_price']})\n"
    else:
        body += "No cheaper flights found.\n"
    
    body += "\nOther Prices:\n"
    body += "\n".join(flight_details)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print(f"Failed to fetch data from Sheety: {response.status_code}")
