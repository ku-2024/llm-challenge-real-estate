import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 데이터를 저장할 리스트
apt_data = []

# 페이지 크롤링 함수
def crawl_page(page_num):
    '''
    페이지 번호를 입력받아 해당 페이지의 아파트 정보를 크롤링하는 함수
    '''
    url = f"https://www.aldongsan.com/aptlist.php?localid=1100000000&order=totalCnt&orderType=desc&page={page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    apt_list = soup.find('ul', class_='aptListUl')
    
    if apt_list:
        for li in apt_list.find_all('li', class_='aptLiItem'):
            # 아파트 이름에서 태그 제거 및 쌍따옴표 제거
            apt_name = li.find('span', class_='aptName').get_text(strip=True)
            apt_name = apt_name.replace('"', '')
            # 총 세대수에서 숫자만 추출
            total_households = li.find('span', class_='totalHouseholdCount').text.strip()
            total_households = int(re.sub(r'[^\d]', '', total_households))  # 숫자만 추출해서 정수로 변환
            
            # 첫 입주시기 처리
            completion_date = li.find('span', class_='completionYearMonth').text.strip()
            completion_date = pd.to_datetime(completion_date, format='%Y년 %m월')  # 날짜 형식 변환
            
            location = li.find('span', class_='cortarAddress').text.strip()
            
            apt_data.append({
                'name': apt_name,
                'total_households': total_households,
                'completion_date': completion_date,
                'location': location
            })

# 여러 페이지 크롤링
for page_num in range(1, 452):
    crawl_page(page_num)
    print(f"Page {page_num} crawled.")

# 데이터를 데이터프레임으로 변환
df = pd.DataFrame(apt_data)

# CSV 파일로 저장
df.to_csv('data/apartments.csv', index=False, encoding='utf-8-sig')
print("Data saved to apartments.csv")