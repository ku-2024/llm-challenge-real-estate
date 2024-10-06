# 위키동산
![Title](/src/title.png "Title")

![builtbydev](https://camo.githubusercontent.com/40f6e06565023f14c6cb7a60088f64ec4d01418d44ceedb80a1848e8365dfbe1/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6275696c742d62792d646576656c6f706572732e737667)

## 📜 Project Overview
나만의 공인중개사, 위키동산

> **‘위키’피디아 + 부‘동산’ 합성어로 아파트 실거주자들의 후기를 모아서 한 눈에 볼 수 있는 서비스**

[프로젝트 데모 영상](https://www.youtube.com/watch?v=ReRWocARLd8)

### 🎯 Objective
- 효율적인 리뷰 데이터 수집
- LLM을 활용한 리뷰 분류 및 요약
- 채팅을 통한 맞춤형 경험 제공

> **다양한 소스에서 수집한 리뷰를 하나로 모으고 분류하여, 믿을 수 있고 요약된 정보 제공**

### 🔑 Key Features
- 후기 수집
- 카테고리 분류
- 요약
- 채팅

## 🏘 Project Architecture
![Project Architecture](/src/project_architecture.jpg "Project Architecture")
<details>
  <summary>Frontend</summary>

  1. **첫 번째 페이지 (검색 페이지)**
  - 아파트에 대한 검색을 하면, 검색어가 포함된 아파트 목록을 보여줍니다. 예를 들어 “아이빌“이라는 단어를 검색하면, “아이빌“이 포함된 아파트들을 보여줍니다. 원하는 아파트 카드의 “더 보기” 버튼을 클릭하면, 해당 아파트의 설명 페이지로 이동합니다.

  2. **두 번째 페이지 (설명 페이지)**
  - 설명 페이지에서는 아파트의 이름, 주소, 세대수, 완공일과 같은 기본 정보를 확인할 수 있고, 각 평수에 대한 가격 정보도 제공됩니다. 페이지를 아래로 스크롤하면 8개의 카테고리로 LLM이 요약한 리뷰를 볼 수 있고, 사이드바에 있는 카테고리 버튼을 클릭하면 해당 카테고리를 쉽게 확인할 수 있습니다. 채팅창에서 AI 챗봇과 질문을 주고 받으며 도움을 받을 수 있습니다. 마지막으로, 위키동산 아이콘을 클릭하면 처음 검색 화면으로 돌아갑니다.
  
</details>

<details>
  <summary>Backend</summary>
  
  1. **데이터 크롤링**
  - BeautifulSoup4와 Requests를 사용하여 웹에서 아파트 정보 수집
  - 수집된 데이터를 CSV 파일 형태로 임시 저장 (추후 Database에 실시간으로 데이터 저장하는 Data Pipeline 구축 예정)
  2. **데이터베이스 설계**
  - MariaDB 데이터베이스 사용
  - SQLAlchemy ORM을 활용한 데이터 모델링
  - 주요 모델: 아파트 리뷰, 아파트 거래 정보, 아파트 기본 정보
  3. **API 서버**
  - FastAPI 프레임워크를 이용한 RESTful API 구현
  - 비동기 처리를 통한 고성능 API 엔드포인트 제공
  - 주요 기능: 데이터베이스 초기화, 대량 데이터 삽입, 아파트 정보 조회
  4. **데이터 처리 및 분석**
  - Pandas를 활용한 효율적인 데이터 전처리 및 분석
  - SQLAlchemy를 통한 데이터베이스 CRUD 작업 수행
  - 비동기 데이터베이스 세션을 활용한 효율적인 데이터 접근
    
</details>

<details>
  <summary>LLM</summary>
  
  - Label 섞여있는 데이터 Label별로 process
  - 각 아파트마다 Label별로 (0~7) 후기 폴더 안에 저장
  - LLM 업스테이지 solar-1-mini-chat 모델 사용
  - LLM에 2-shot example 주고 instruction 제공하는 프롬프트 엔지니어링 적용 (업스테이지 공식 깃허브 cookbook 참고)
  - 답변의 다양성, 일관성의 밸런스를 조절하기 위해 temperature, top_p 파라미터 조절
  - 후기 각각 레이블마다 나오고 아파트 폴더에 저장
  
</details>

## 🌟 Implementation Details

각 파트 별 디렉토리의 README 파일을 참고해주세요.

### Frontend
```
cd frontend
cd real-estate
yarn install
yarn start
```

### Backend
**Docker로 MariaDB 설치**
도커 설치
```
docker pull mariadb
docker run -p 3306:3306 --name llm-challenge -e MARIADB_ROOT_PASSWORD=1234 -d mariadb
```
- -p 3306:3306 : 호스트와 컨테이너 간의 포트를 연결 (host-port:container-port), 호스트에서 3306 포트 연결 시 컨테이너 3306 포트로 포워딩
- --name llm-challenge : 생성하려는 컨테이너의 이름을 `llm-challenge` 으로 지정
- -e MARIADB_ROOT_PASSWORD=1234 : 컨테이너 내 환경변수 설정. mariadb의 root 사용자의 암호 지정
- -d: 컨테이너를 백그라운드에서 실행
```
docker exec -it llm-challenge mariadb -uroot -p
MariaDB [(none)]> create database budongsan
```
**conda 가상환경 설정**
```
conda create -n llm_env python=3.9
conda activate llm_env
pip install -r requirements.txt
```
**실행**
```
cd ./backend
uvicorn main:app --reload --host 127.0.0.1 --port 5000
```

### LLM
```
pip install -r requirements.txt
```
../ 디렉토리에 1_Gracium_Label.csv 같은 전처리 안된 아파트 데이터 포함 후, 아래 실행
```
python process.py
python llm_generate.py
```

## 🔥 Future Work
- 데이터 실시간 업데이트: 새로 나오는 후기를 실시간으로 크롤링하여 LLM 모델 업데이트
- 지도 API: 아파트 탐색 시, 지도를 보며 위치 정보도 함께 탐색
- 챗봇: 원활한 후기 탐방을 위해 챗봇 구현 및 성능 향상
- 평점
- 데이터 추가


## 🙌 Team Members
![Team](/src/team.png "Team")

![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![mariadb](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![fastapi](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![sqlalchemy](https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![ppt](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white)
![figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)
![git](https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
