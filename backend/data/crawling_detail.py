import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
import tqdm
import numpy as np 
from sqlalchemy import create_engine
import uuid

def generate_apt_code(apt_name, district):
    # UUID를 사용하여 고유한 코드 생성
    # district = ''.join(district.split(" ")[1:])
    # return f"{district}_{apt_name}" #_{str(uuid.uuid4())[:8]}"
    return str(uuid.uuid4())[:8]

def clean_value(column_name, value):
    if column_name == "total_buildings":
        return int(value.replace("개동", ""))
    elif column_name == "completion_date":
        return datetime.strptime(value, "%Y년 %m월").date()
    elif column_name == "address":

        # Handle cases where one or both parts (지번주소 or 도로명주소) are missing
        land_address = ""
        road_address = ""
        
        # Regular expression pattern to extract the addresses
        pattern = r'\[지번주소\]\s*(.*?)\s*\[도로명주소\]\s*(.*)'

        # Using re.search to find the matches
        match = re.search(pattern, value)

        if match:
            land_address = match.group(1).strip()  # First captured group for 지번주소
            road_address = match.group(2).strip()  # Second captured group for 도로명주소
            # print("Land Address:", land_address)
            # print("Road Address:", road_address)
            return {"land_address": land_address, "road_address": road_address}
        else:
            pass

        
    
    elif column_name == "latitude_longitude":
        # Extract latitude and longitude
        latitude = float(value.split("[위도]")[1].split("[경도]")[0].strip())
        longitude = float(value.split("[경도]")[1].strip())
        return {"latitude": latitude, "longitude": longitude}
    
    elif column_name == "max_floor" or column_name == "min_floor":
        return int(value.replace("층", ""))
    
    elif column_name == "parking_per_household":
        return float(value.replace("세대당", "").replace("대", "").strip())
    
    elif column_name == "area_list":
        # Remove "㎡" and return a list of areas
        return ','.join([area.replace("㎡", "") for area in value.split(", ")])
    
    else:
        return value.strip()

    

def scrape_apartment_list(page):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(f"Scraping page {page}")
    # Find all apartment listings
    apt_list = soup.find_all('li', class_='aptLiItem')
    # print(f"Found {len(apt_list)} apartments")
    for apt in apt_list:
        # print(f"Scraping apartment {apt.find('span', class_='aptName').text.strip()}")
        apt_name = apt.find('span', class_='aptName').text.strip()
        total_households = apt.find('span', class_='totalHouseholdCount').text.strip()
        completion_date = apt.find('span', class_='completionYearMonth').text.strip()
        district = apt.find('span', class_='cortarAddress').text.strip()
        apt_code = generate_apt_code(apt_name, district)
        # Get detail page link
        detail_link = apt.find('span', class_='aptName').find('a')['href']
        
        # print(f"Scraping detail page: {detail_link}")
        # Scrape detail page
        detail_data = scrape_apartment_detail(detail_link)
        
        # Append the scraped data to the list
        apartment_data.append({
            'apt_code': apt_code,
            'apt_name': apt_name,
            'total_households': int(total_households.replace('세대', '').replace(',', '')),
            'completion_date': datetime.strptime(completion_date, "%Y년 %m월"),
            'district': district,
            **detail_data
        })

# Function to scrape detailed apartment information
def scrape_apartment_detail(detail_url):
    response = requests.get(detail_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    cells = soup.find_all('li', class_='semiBodyCell')

    # Dictionary to store the results
    apartment_details = {}
    # Translation of Korean column names to English
    column_mapping = {
        "단지명": "apt_name",
        "세대수": "total_households",
        "총동수": "total_buildings",
        "첫입주시기": "completion_date",
        "주소": "address",
        "위도/경도": "latitude_longitude",
        "건설사": "construction_company",
        "난방": "heating_type",
        "최고층": "max_floor",
        "최저층": "min_floor",
        "세대당 주차수": "parking_per_household",
        "면적 목록": "area_list"
        }
    # Processing the results in scrape_apartment_detail
    for cell in cells:
        column_name_kr = cell.find('div', class_='semiItemHead').text.strip()  # Extract the column name in Korean
        value = cell.find('div', class_='semiItem').text.strip()  # Extract the corresponding value
        
        # Translate column name to English
        if column_name_kr in column_mapping:
            column_name_en = column_mapping[column_name_kr]
            
            # Process the value based on the column
            processed_value = clean_value(column_name_en, value)
            if isinstance(processed_value, dict):
                # If the processed value is a dictionary (for address, latitude_longitude), update the dictionary with multiple keys
                apartment_details.update(processed_value)  # Correctly update land_address and road_address
            else:
                # Otherwise, add the single processed value
                apartment_details[column_name_en] = processed_value


    
    return apartment_details

if __name__ == "__main__":
    # URL for scraping
    base_url = "https://www.aldongsan.com/aptlist.php?localid=1100000000&order=totalCnt&orderType=desc&page={}"
    detail_url_base = "https://www.aldongsan.com"

    # Initialize an empty list to store the data
    apartment_data = []
    TOTAL_PAGES = 451
    # Scrape multiple pages
    for page in tqdm.tqdm(range(1,TOTAL_PAGES+1)):  # Adjust page range as needed
        scrape_apartment_list(page)

    # Convert to DataFrame
    print("Converting to DataFrame")
    df = pd.DataFrame(apartment_data)
    # Assuming df is your pandas DataFrame
    # df = df.replace({np.nan:None})
    df = df.where(pd.notnull(df), None)
    df.drop(columns = ['address'], inplace=True)
    # print('null이 있는지? ',df.isnull().sum())
    # Save to a CSV or Excel file
    print("Saving to CSV")
    df.to_csv('./data/apartment_data.csv', index=False, na_rep='NULL')
