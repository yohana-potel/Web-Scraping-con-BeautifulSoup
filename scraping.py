from bs4 import BeautifulSoup
import requests
import csv  # Asegúrate de importar csv si no lo tienes

url = 'https://www.universia.es'
seObtiene = requests.get(url)
html_doc = seObtiene.text

soup = BeautifulSoup(html_doc, 'html.parser')

careers_table = soup.find("table", {"class": "tabla_resultados"})
if careers_table:
    careers = careers_table.find_all("tr")[1:]  # skip the header row
    with open("careers.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "University", "Location"])  # header row
        for career in careers:
            columns = career.find_all("td")
            title = columns[0].text.strip()  # assume title is in the first column
            university = ""
            location = ""
            for column in columns[1:]:  # iterate over remaining columns
                if "Universidad" in column.text:
                    university = column.text.strip()
                elif "Madrid" in column.text:  # assume location is in a column with "Madrid"
                    location = column.text.strip()
            writer.writerow([title, university, location])
else:
    print("No careers table found")
