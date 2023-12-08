from bs4 import BeautifulSoup
import openpyxl

# Read HTML file
with open('Amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1qlj3vrpms3m32klujlujtgcs8 s-latency-cf-section puis-card-border')

# Open an Excel file
excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active

# Write headers to Excel sheet
excel_sheet.append(['Product_Name', 'Product_Price', 'Product_Reviews'])

# Loop through each div and extract information
for div in divs:
    # Find h2 with class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"
    h2 = div.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4')
    Product_Name = h2.text.strip() if h2 else ""

    # Find span with class="a-price-whole"
    span = div.find('span', class_='a-price-whole')
    Product_Price = span.text.strip() if span else ""

    # Find i with class="a-icon a-icon-star-small a-star-small-3-5 aok-align-bottom"
    i = div.find('i', class_='a-icon a-icon-star-small a-star-small-3-5 aok-align-bottom')
    Product_Reviews = i.text.strip() if i else ""

    # Write data to Excel sheet
    excel_sheet.append([Product_Name, Product_Price, Product_Reviews])

# Save Excel file
excel_file.save('output.xlsx')
