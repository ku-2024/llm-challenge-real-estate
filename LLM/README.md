# LLM

## 1. 데이터셋 라벨 분류하기 (`process.py` 실행)

`process.py` 파일을 실행하여 원본 CSV 파일을 각 아파트 단지별로 라벨 분류한 데이터셋을 생성합니다.

### 입력 파일 형식
- `../` 경로에 `1_Gracium_Label.csv`, `2_Arteon_Label.csv` 등과 같이 `[숫자]_[아파트이름]_Label.csv` 형태의 파일이 있어야 합니다.
- 파일 내에 `Label` 컬럼이 존재하고, 각 라벨에 따라 데이터가 그룹화됩니다.

### 실행 후 확인
- `./processed_data/아파트이름/` 경로에 각 아파트 이름에 맞는 폴더가 생성되고, 폴더 내에 `Label_Group_번호.csv` 형식으로 라벨 분류된 데이터가 저장됩니다.  
- 예: `./processed_data/Gracium/Gracium_Label_Group_0.csv`

### 데이터셋 확인
생성된 `processed_data/아파트이름/` 폴더에 들어가 라벨별로 잘 분류되었는지 확인합니다. 만약 파일이 제대로 생성되지 않았거나 내용이 누락된 경우, 원본 CSV 파일의 `Label` 컬럼 값을 확인하고 재실행하세요.

---

## 2. LLM 요약 

- `llm_generate.py` 실행 전에 `.env` 파일에 API KEY를 설정합니다. `.env` 파일이 프로젝트 루트 디렉토리에 위치해야 합니다.

### `llm_generate.py` 실행
- `llm_generate.py` 파일을 실행하여 LLM을 통해 각 라벨에 대한 요약문을 생성합니다.  
- 요약문은 `./summary/아파트이름/` 폴더에 `Label_Summary_번호.txt` 형식으로 저장됩니다.

---

## 3. LLM 파라미터 및 Instruction 바꾸기

### Few Shot 및 Instruction 설정
- `llm_generate.py`의 `few_shot_prompt_template` 부분을 수정하여 Instruction 및 Few Shot 예제를 변경할 수 있습니다. 

### 파라미터 변경
- `summary = chain.invoke` 부분에서 `temperature`와 `top_p` 파라미터를 변경하여 조정 가능합니다.  
  - **temperature**: 확률 함수 스무딩 (낮추면 창의성 낮아지고 일관성 올라감).  
  - **top_p**: `temperature`로 결정된 확률들 중 누적으로 몇 퍼센트 단어까지 고려할지 결정 (예: 0.9면 90% 확률 안에 들어가는 단어들까지 고려).

---

## 4. 결과 확인 및 수정

- 생성된 요약문(`./summary/아파트이름/`)이 원하는 형태로 잘 생성되었는지 확인합니다.  
- 요약문이 기대와 다른 경우, `#3`을 다시 체크하고 수정합니다.
