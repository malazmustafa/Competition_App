import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org/messages",
        auth=("api", "b5e6c9e56fab046908f1e9273b944409-de7062c6-e7190b95"),
        data={"from": "Excited User <mailgun@sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org>",
        "to": ["anastasiaaniwa@gmail.com"],
        "subject": "Hello",
        "text": "Testing some mailgun awesomeness!"})
send_simple_message()
