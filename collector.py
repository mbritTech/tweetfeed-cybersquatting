import csv
import requests

def get_domains_from_file(file_url):
    # utilizamos el fichero donde se encuentran los dominios
    domains_file = requests.get(file_url)

    # formateo el fichero linea a linea para extraer los dominios
    # utilizo el delimitador ";" para dividir los diferentes campos
    text = domains_file.text.splitlines()
    reader = csv.reader(text[4:], delimiter=";")

    domains_list = []
    for row in reader:
        domains_list.append(row[1])

    return domains_list

def get_suspicious_domains_tweetfeed():
    domains_list = requests.get("https://api.tweetfeed.live/v1/year/domain/phishing")
    domains_json = domains_list.json()

    suspicious_domains_for_filtering = []
    for domain in domains_json:
        suspicious_domains_for_filtering.append(domain["value"])

    return suspicious_domains_for_filtering

