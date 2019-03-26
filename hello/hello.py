def send_simple_message(email, firstname):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org/messages",
        auth=("api", "b5e6c9e56fab046908f1e9273b944409-de7062c6-e7190b95"),
        files= [("attachment", ("hello.jpg", open("/Users/anastasiaaniwa/Desktop/CodeFirstGirls/Python/Competition_App/static/images/hello.jpg.jpg", "rb").read
        ()))],
        data={"from": "Excited User <postmaster@sandbox8ea045b272754b97a9a3b9100fd89d00.mailgun.org>",
        "to": [email],
        "subject": "Hello " + firstname,
        "text": "Welcome! ",
        "html": "<html><b>Welcome!</b></html>",
        })
