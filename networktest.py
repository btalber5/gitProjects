import os

hostname = "google.com"


def ping(host):

    response = os.system("ping -c 1 " + host)

    if response == 0:
        print hostname, "is up!"

    else:
        print hostname, "is down"


ping(hostname)