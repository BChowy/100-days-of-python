import requests
from datetime import datetime
import smtplib
import time

# got it from https://www.latlong.net/
ABHA_LONG = 42.499481
ABHA_LAT = 18.217051

EMAIL = "example.gmail.com"
PASSWORD = "ABCD1234()"


def check_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return ((ABHA_LAT - 5 <= iss_latitude <= ABHA_LAT + 5)
            and (ABHA_LONG - 5 <= iss_longitude <= ABHA_LONG + 5))


def is_night():
    parameters = {
        "lat": ABHA_LAT,
        "long": ABHA_LONG,
        "formatted": 0,  # to get the time in unix format
    }
    # Require parameters of longitude and latitude
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # in case there's a mistake, raise an error
    data = response.json()

    # split it by "T", take the second part, split it by ":", take the first part which is the hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(to_addrs=EMAIL,
                            from_addr=EMAIL,
                            msg="SUBJECT:Look at the sky\n\nThe International Space Station is close")


while True:
    if is_night() and check_iss_location():
        send_email()
    time.sleep(60)
