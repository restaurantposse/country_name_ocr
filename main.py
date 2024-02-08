import pytesseract
import pandas as pd
from PIL import Image

df = pd.read_csv('bing-europe-countries.csv')

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = Image.open('img/img_1.png')
country_name = pytesseract.image_to_string(img).strip()
selected_rows = df.loc[df['Country'] == country_name]

if not selected_rows.empty:
    print(f"""
        Country: {selected_rows['Country'].values[0]}
        Capital: {selected_rows['Capital'].values[0]}
        Currency: {selected_rows['Currency'].values[0]}
        Population: {selected_rows['Population'].values[0]}
        GDP (Billion USD): {selected_rows['GDP (Billion USD)'].values[0]}
        """)
else:
    print(f"Country '{country_name}' does not exist")

