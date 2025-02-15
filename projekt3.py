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
    """Získa odkazy na obce z okresnej stránky."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Chyba pri načítaní URL: {url}")
        print(f"Detail chyby: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    municipality_links = []
    for link in links:
        if not ('ps311' in link['href'] and 'xobec' in link['href']):
            continue
        link_to_add = 'https://www.volby.cz/pls/ps2017nss/' + link['href']
        if link_to_add not in municipality_links:
            municipality_links.append(link_to_add)
    
    #  Debug výpisy
    print(f"DEBUG - Nájdené odkazy na obce: {len(municipality_links)}")
    if municipality_links:
        print(f"Prvý odkaz: {municipality_links[0]}")

    return municipality_links


def get_municipality_data(municipality_url: str) -> dict:
    """Extrahuje údaje o konkrétnej obci."""
    try:
        response = requests.get(municipality_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Chyba pri načítaní obce: {municipality_url}")
        print(f"Detail chyby: {e}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    # 🔹 Extrahovanie názvu obce
    name = extract_municipality_name(soup, municipality_url)
    
    # 🔹 Extrahovanie základných údajov
    basic_data = extract_basic_data(soup, municipality_url)
    
    # 🔹 Extrahovanie volebných výsledkov
    election_results = extract_election_results(soup)

    # 🔹 Spojenie všetkých dát do jedného slovníka
    return {**basic_data, 'Názov obce': name, **election_results}


def extract_municipality_name(soup: BeautifulSoup, url: str) -> str:
    """Získa názov obce zo stránky."""
    name_tags = soup.find_all('h3')
    
    if len(name_tags) > 2:
        return name_tags[2].text.strip()
    
    print(f"Upozornenie: Názov obce sa nenašiel pre {url}")
    return "Neznámá obec"


def extract_basic_data(soup: BeautifulSoup, url: str) -> dict:
    """Získa základné údaje o obci."""
    basic_data_table = soup.find('table', {'class': 'table'})
    rows = basic_data_table.find_all('tr') if basic_data_table else []
    
    if not rows or len(rows) < 3:
        print(f"Upozornenie: Základné údaje sa nenašli pre {url}")
        return {}

    data_cells = rows[2].find_all('td')
    code = url.split('xobec=')[-1].split('&')[0]
    voters = clean_number(data_cells[3].text)
    envelopes = clean_number(data_cells[4].text)
    valid_votes = clean_number(data_cells[7].text)

    return {
        'Kód obce': code,
        'Voliči v zozname': voters,
        'Odovzdane obalky': envelopes,
        'Platné hlasy': valid_votes
    }


def extract_election_results(soup: BeautifulSoup) -> dict:
    """Získa volebné výsledky strán."""
    results = {}
    
    party_table = soup.find_all('table')[-1]
    party_rows = party_table.find_all('tr')[2:] if party_table else []
    
    for row in party_rows:
        columns = row.find_all('td')
        if len(columns) > 2:
            party_name = columns[1].text.strip()
            votes = clean_number(columns[2].text)
            if party_name != '-':
                results[party_name] = votes
    
    return results


def clean_number(value: str) -> str:
    """Odstráni medzery a neviditeľné znaky z čísla."""
    return value.strip().replace('\xa0', '').replace(' ', '')


def scrape_election_data(municipality_links: list) -> dict:
    """Spracuje volebné dáta a vráti v slovníku. """
    all_data = []
    party_names = set()

    # Získanie údajov pre každú obec
    for municipality_url in municipality_links:
        print(f" Spracovávam obec: {municipality_url}")
        municipality_data = get_municipality_data(municipality_url)
        
        if municipality_data:
            all_data.append(municipality_data)
            party_names.update(municipality_data.keys() - {'Kód obce', 'Názov obce', 'Voliči v zozname', 'Odovzdane obalky', 'Platné hlasy'})
    
    return party_names, all_data


def save_election_data(party_names: dict, municipality_data: list, output_file: str) -> dict:
    #  Usporiadanie stĺpcov v CSV
    sorted_party_names = sorted(party_names)
    header = ['Kód obce', 'Názov obce', 'Voliči v zozname', 'Odovzdane obalky', 'Platné hlasy'] + sorted_party_names

    #  Uloženie do CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(header)
        
        for row in municipality_data:
            sorted_row = [
                row.get('Kód obce', ''),
                row.get('Názov obce', ''),
                row.get('Voliči v zozname', ''),
                row.get('Odovzdane obalky', ''),
                row.get('Platné hlasy', '')
            ] + [row.get(party, '0') for party in sorted_party_names]
            
            writer.writerow(sorted_row)

    print(f" Údaje boli uložené do {output_file}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("📌 Použitie: python projekt3.py <url_okresu> <output_file>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    if not re.match(r'^(http|https)://', url):
        print(" Chybný URL formát. Prosím, zadajte platnú URL.")
        sys.exit(1)

    municipality_links = get_municipality_links(url)

    if not municipality_links:
        print(" Neboli nájdené žiadne odkazy na obce.")
        sys.exit(1)

    parties, db = scrape_election_data(municipality_links)
    save_election_data(parties, db, output_file)
