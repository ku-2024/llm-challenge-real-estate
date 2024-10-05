# backend

## Docker로 MariaDB 설치
우선 도커 설치
`docker pull mariadb`

`docker run -p 3306:3306 --name llm-challenge -e MARIADB_ROOT_PASSWORD=1234 -d mariadb`

* -p 3306:3306 : 호스트와 컨테이너 간의 포트를 연결 (host-port:container-port), 호스트에서 3306 포트 연결 시 컨테이너 3306 포트로 포워딩
* --name llm-challenge : 생성하려는 컨테이너의 이름을 test로 지정
* -e MARIADB_ROOT_PASSWORD=1234 : 컨테이너 내 환경변수 설정. mariadb의 root 사용자의 암호 지정
* -d: 컨테이너를 백그라운드에서 실행

`docker exec -it llm-challenge mariadb -uroot -p`

`MariaDB [(none)]> create database budongsan;`

## conda 가상환경 설정
`conda create -n llm_env python=3.9; conda activate llm_env;  `
`pip install -r requirements.txt`


## 실행
cd ./backend
uvicorn main:app --reload --host 127.0.0.1 --port 5000
