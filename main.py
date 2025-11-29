from tldextract import extract
from collector import *
from filter import *


def tweetfeed_filtering():
    collected_domains = get_domains_from_file("https://www.dominios.es/sites/dominios/files/2025-07/alt_es_202506xls.csv")
    domains_for_filtering = get_suspicious_domains_tweetfeed()

    for domain in collected_domains:
        domain_extraction = extract(domain, include_psl_private_domains=True)
        subdomain, main_domain, tld = domain_extraction.subdomain, domain_extraction.domain, domain_extraction.suffix

        have_match, match = filtering_proccess(main_domain, domains_for_filtering)
        if have_match:
            print(f"Domain |{domain}| matched with {match}")
        # else:
        #     print(f"El dominio |{domain}| no ha hecho match")


if __name__ == '__main__':
    tweetfeed_filtering()
