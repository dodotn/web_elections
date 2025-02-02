Program web elections vytvára csv súbor z výsledkov volieb do PS ČR v roku 2017. Pres spustenie je nutne nainštalovať knižnice beatifulsoap a requests. Sú uvedené v súbore requirements.txt
Postup inštalácie knižníc:
python -m pip install beautifulsoup4
python -m pip install requests

 Program sa spúšťa v tvare python projekt3.py <url_okresu> <output_file>.
Ukážka behu:

C:\>python projekt3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101" cheb.csv
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554499&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Aš
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554502&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Dolní Žandov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554511&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Drmoul
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554529&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Františkovy Lázně
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554545&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Hazlov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554553&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Hranice
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554481&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Cheb
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=538795&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Krásná
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554596&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Křižovatka
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554600&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Lázně Kynžvart
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554618&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Libá
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554626&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Lipová
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554634&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Luby
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554642&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Mariánské Lázně
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554651&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Milhostov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=538906&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Milíkov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554677&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Mnichov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554693&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Nebanice
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554707&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Nový Kostel
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539554&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Odrava
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=538922&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Okrouhlá
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539473&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Ovesné Kladruby
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554740&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Plesná
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=538817&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Podhradí
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=538868&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Pomezí nad Ohří
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=577979&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Poustka
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539538&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Prameny
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554812&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Skalná
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539112&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Stará Voda
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=555631&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Teplá
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554855&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Trstěnice
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539023&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Třebeň
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=554880&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Tři Sekery
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539619&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Tuřany
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539481&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Valy
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539279&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Velká Hleďsebe
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=578002&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Velký Luh
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539376&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Vlkovice
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539074&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Vojtanov
🔹 Spracovávam obec: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=5&xobec=539431&xvyber=4101
 DEBUG - Zistený názov obce: Obec: Zádub-Závišín
DEBUG - Správne uložený riadok: ['554499', 'Obec: Aš', '9766', '4289', '4254', '1707', '3', '94', '15', '10', '4', '13', '10', '515', '153']
DEBUG - Správne uložený riadok: ['554502', 'Obec: Dolní Žandov', '943', '532', '528', '188', '4', '10', '5', '0', '2', '4', '1', '56', '16']
DEBUG - Správne uložený riadok: ['554511', 'Obec: Drmoul', '769', '486', '481', '181', '3', '22', '3', '0', '0', '1', '1', '51', '11']
DEBUG - Správne uložený riadok: ['554529', 'Obec: Františkovy Lázně', '4700', '2905', '2886', '967', '5', '75', '16', '5', '11', '15', '19', '328', '142']
DEBUG - Správne uložený riadok: ['554545', 'Obec: Hazlov', '1239', '638', '626', '234', '0', '26', '0', '2', '0', '1', '0', '100', '10']
DEBUG - Správne uložený riadok: ['554553', 'Obec: Hranice', '1677', '706', '698', '289', '2', '3', '1', '2', '2', '2', '2', '75', '14']
DEBUG - Správne uložený riadok: ['554481', 'Obec: Cheb', '23954', '12225', '12153', '4189', '44', '291', '70', '9', '16', '31', '29', '1489', '380']
DEBUG - Správne uložený riadok: ['538795', 'Obec: Krásná', '474', '264', '262', '138', '0', '1', '1', '0', '0', '0', '0', '30', '7']
DEBUG - Správne uložený riadok: ['554596', 'Obec: Křižovatka', '210', '118', '118', '55', '0', '2', '0', '0', '0', '0', '0', '7', '1']
DEBUG - Správne uložený riadok: ['554600', 'Obec: Lázně Kynžvart', '1228', '613', '608', '210', '1', '14', '1', '0', '1', '2', '2', '77', '13']
DEBUG - Správne uložený riadok: ['554618', 'Obec: Libá', '592', '301', '297', '112', '0', '2', '0', '0', '0', '2', '1', '37', '2']
DEBUG - Správne uložený riadok: ['554626', 'Obec: Lipová', '586', '299', '297', '115', '4', '4', '1', '1', '0', '1', '1', '45', '10']
DEBUG - Správne uložený riadok: ['554634', 'Obec: Luby', '1809', '852', '843', '346', '2', '34', '1', '2', '3', '2', '2', '98', '18']
DEBUG - Správne uložený riadok: ['554642', 'Obec: Mariánské Lázně', '10572', '5720', '5675', '1741', '6', '198', '37', '8', '6', '11', '14', '538', '255']
DEBUG - Správne uložený riadok: ['554651', 'Obec: Milhostov', '244', '82', '82', '54', '0', '0', '1', '0', '1', '0', '0', '5', '0']
DEBUG - Správne uložený riadok: ['538906', 'Obec: Milíkov', '223', '141', '141', '35', '2', '6', '0', '0', '0', '1', '1', '19', '1']
DEBUG - Správne uložený riadok: ['554677', 'Obec: Mnichov', '335', '137', '135', '33', '0', '8', '2', '0', '0', '1', '1', '17', '3']
DEBUG - Správne uložený riadok: ['554693', 'Obec: Nebanice', '278', '162', '159', '50', '0', '1', '0', '0', '1', '1', '0', '20', '4']
DEBUG - Správne uložený riadok: ['554707', 'Obec: Nový Kostel', '410', '221', '221', '80', '1', '17', '0', '0', '0', '0', '8', '28', '7']
DEBUG - Správne uložený riadok: ['539554', 'Obec: Odrava', '185', '99', '99', '34', '0', '0', '0', '0', '0', '1', '1', '12', '2']
DEBUG - Správne uložený riadok: ['538922', 'Obec: Okrouhlá', '199', '108', '107', '37', '0', '2', '1', '0', '0', '1', '0', '15', '0']
DEBUG - Správne uložený riadok: ['539473', 'Obec: Ovesné Kladruby', '97', '52', '52', '12', '0', '2', '0', '1', '0', '1', '0', '1', '1']
DEBUG - Správne uložený riadok: ['554740', 'Obec: Plesná', '1565', '723', '719', '281', '0', '4', '1', '0', '1', '0', '4', '85', '44']
DEBUG - Správne uložený riadok: ['538817', 'Obec: Podhradí', '164', '79', '79', '33', '0', '4', '0', '1', '0', '1', '2', '10', '1']
DEBUG - Správne uložený riadok: ['538868', 'Obec: Pomezí nad Ohří', '206', '132', '131', '42', '0', '3', '3', '0', '0', '0', '0', '11', '7']
DEBUG - Správne uložený riadok: ['577979', 'Obec: Poustka', '122', '80', '79', '23', '0', '2', '0', '0', '0', '0', '1', '12', '0']
DEBUG - Správne uložený riadok: ['539538', 'Obec: Prameny', '92', '59', '57', '18', '1', '1', '0', '0', '0', '1', '0', '14', '1']
DEBUG - Správne uložený riadok: ['554812', 'Obec: Skalná', '1511', '777', '770', '325', '3', '18', '1', '0', '1', '1', '0', '107', '13']
DEBUG - Správne uložený riadok: ['539112', 'Obec: Stará Voda', '389', '196', '196', '60', '0', '4', '1', '0', '1', '1', '1', '37', '6']
DEBUG - Správne uložený riadok: ['555631', 'Obec: Teplá', '2365', '1058', '1046', '340', '3', '50', '4', '0', '1', '3', '2', '128', '22']
DEBUG - Správne uložený riadok: ['554855', 'Obec: Trstěnice', '301', '165', '165', '60', '0', '2', '1', '0', '0', '0', '1', '25', '1']
DEBUG - Správne uložený riadok: ['539023', 'Obec: Třebeň', '326', '206', '203', '79', '1', '7', '0', '0', '1', '0', '1', '29', '2']
DEBUG - Správne uložený riadok: ['554880', 'Obec: Tři Sekery', '748', '393', '384', '129', '0', '14', '2', '0', '1', '2', '0', '38', '6']
DEBUG - Správne uložený riadok: ['539619', 'Obec: Tuřany', '110', '73', '73', '33', '1', '0', '0', '0', '1', '0', '0', '5', '1']
DEBUG - Správne uložený riadok: ['539481', 'Obec: Valy', '384', '241', '240', '100', '0', '8', '3', '0', '0', '0', '1', '29', '10']
DEBUG - Správne uložený riadok: ['539279', 'Obec: Velká Hleďsebe', '1816', '1039', '1027', '331', '2', '28', '6', '1', '2', '2', '1', '100', '38']
DEBUG - Správne uložený riadok: ['578002', 'Obec: Velký Luh', '127', '67', '66', '20', '0', '2', '0', '0', '1', '1', '0', '7', '0']
DEBUG - Správne uložený riadok: ['539376', 'Obec: Vlkovice', '104', '72', '72', '24', '0', '6', '1', '0', '1', '1', '0', '6', '1']
DEBUG - Správne uložený riadok: ['539074', 'Obec: Vojtanov', '168', '102', '102', '50', '0', '1', '1', '0', '0', '0', '1', '16', '2']
DEBUG - Správne uložený riadok: ['539431', 'Obec: Zádub-Závišín', '274', '165', '164', '49', '1', '13', '1', '0', '0', '0', '0', '20', '7']
Údaje boli uložené do súboru cheb.csv.