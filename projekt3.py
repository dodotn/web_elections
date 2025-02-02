"""
projekt3.py: třetí projekt do Engeto Online Python Akademie

author: Jozef Drga
email: dodo.tn@seznam.cz
"""




import requests
from bs4 import BeautifulSoup
import csv
import sys
import re

def get_municipality_links(url: str) -> list:
    """Discover the links to municipality from page of district."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a', href=True)
    municipality_links = []
    for link in links:
        if not ('ps311' in link['href'] and 'xobec' in link['href']):
            continue
        link_to_add = 'https://www.volby.cz/pls/ps2017nss/' + link['href']
        if link_to_add not in municipality_links:
            municipality_links.append(link_to_add)
            
    return municipality_links

def is_valid_url(url: str) -> bool:
    """Detect invalid url."""
    return re.match(r'^(http|https)://', url) is not None

def scrape_election_data(municipality_links: list, output_file: str) -> None:
    """Scrape election data from a list of municipality links and save to CSV."""
    all_data = []
    header = ['Kód obce', 'Názov obce', 'Voliči v zozname', 'Odovzdane obalky', 'Platné hlasy']
    party_names = set()  

    temp_results = []
    for municipality_url in municipality_links:
        print(f"🔹 Spracovávam obec: {municipality_url}")
        try:
            response = requests.get(municipality_url)
            response.raise_for_status()
            municipality_soup = BeautifulSoup(response.text, 'html.parser')

           
            name_tag = None
            name_tags = municipality_soup.find_all('h3')  
            if name_tags is not None:
                name_tags = list(name_tags)  
                if len(name_tags) > 2:
                    name_tag = name_tags[2]
                    
            
            if not name_tag:
                print(f"Upozornenie: Názov obce sa nenašiel pre {municipality_url}")
                print(f"Výpis HTML časti:\n{municipality_soup.prettify()[:1000]}\n")  # Pomôže s debugom
                name = "Neznámá obec"
            else:
                name = name_tag.text.strip()
                print(f" DEBUG - Zistený názov obce: {name}")

            # 🔹 Oprava získavania základných údajov
            basic_data_table = municipality_soup.find('table', {'class': 'table'})
            rows = basic_data_table.find_all('tr') if basic_data_table else []
            if rows:
                data_cells = rows[2].find_all('td')
                code = municipality_url.split('xobec=')[-1].split('&')[0]  
                voters = data_cells[3].text.strip().replace('\xa0', '').replace(' ', '')
                envelopes = data_cells[4].text.strip().replace('\xa0', '').replace(' ', '')
                valid_votes = data_cells[7].text.strip().replace('\xa0', '').replace(' ', '')

                row_data = {'Kód obce': code, 'Názov obce': name, 'Voliči v zozname': voters, 'Odovzdane obalky': envelopes,'Platné hlasy': valid_votes}

                # 🔹 Oprava získavania výsledkov strán
                party_table = municipality_soup.find_all('table')[-1]
                party_rows = party_table.find_all('tr')[2:] if party_table else []
                for party_row in party_rows:
                    party_columns = party_row.find_all('td')
                    if len(party_columns) > 2:
                        party_name = party_columns[1].text.strip()  
                        votes = party_columns[2].text.strip().replace('\xa0', '').replace(' ', '')
                        if party_name == '-':
                            continue
                        row_data[party_name] = votes
                        party_names.add(party_name)  

                temp_results.append(row_data)

        except Exception as e:
            print(f"Chyba pri spracovaní obce: {municipality_url}")
            print(f"Detail chyby: {e}")
            continue

    # 🔹 Usporiadame hlavičku
    sorted_party_names = sorted(party_names)
    header.extend(sorted_party_names)

    # 🔹 Naplníme tabuľku správnymi dátami
    for row in temp_results:
        sorted_row = [
            row.get('Kód obce', ''),
            row.get('Názov obce', ''),
            row.get('Voliči v zozname', ''),
            row.get('Odovzdane obalky', ''),
            row.get('Platné hlasy', '')
        ] + [row.get(party, '0') for party in sorted_party_names]  

        print(f"DEBUG - Správne uložený riadok: {sorted_row}")  
        all_data.append(sorted_row)

    # 🔹 Uloženie do CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')  
        writer.writerow(header)  
        writer.writerows(all_data)  

    print(f"Údaje boli uložené do súboru {output_file}.")

#
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("📌 Použitie: python projekt3.py <url_okresu> <output_file>")
        sys.exit(1)  # Ukončí program s chybovým kódom

    url = sys.argv[1]
    output_file = sys.argv[2]

  
    if not is_valid_url(url):
        print(f" Chyba: '{url}' nie je platná URL adresa. Program sa ukončuje.")
        sys.exit(1)  #

    municipality_links = get_municipality_links(url)
    scrape_election_data(municipality_links, output_file)