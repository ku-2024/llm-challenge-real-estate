import os
import pandas as pd

# 상위 디렉토리 설정
input_base_dir = "../"  # CSV 파일들이 있는 경로
output_base_dir = "./processed_data/"

# 입력 파일을 반복적으로 탐색하고 처리
for file_name in os.listdir(input_base_dir):
    # 파일명이 숫자_단지명_Label.csv 패턴인지 확인
    if file_name.endswith("_Label.csv") and file_name.split("_")[0].isdigit():
        # 파일 경로 설정
        file_path = os.path.join(input_base_dir, file_name)
        
        # 단지명 추출 (숫자 제외, 예: 1_Gracium_Label.csv -> Gracium)
        complex_name = file_name.split("_")[1]
        
        # 출력 디렉토리 설정
        complex_output_dir = os.path.join(output_base_dir, complex_name)
        os.makedirs(complex_output_dir, exist_ok=True)  # 폴더가 없으면 생성

        # CSV 파일 불러오기
        try:
            data = pd.read_csv(file_path, on_bad_lines='skip')
        except Exception as e:
            print(f"파일 {file_path} 불러오기 중 오류 발생: {e}")
            continue

        # 데이터 확인
        print(f"파일 {file_name}의 데이터 미리보기:\n", data.head(), "\n")

        # Text 번호별로 데이터 분리 및 저장
        for label, group in data.groupby('Label'):
            # 각 Label에 해당하는 행만 추출하여 별도의 CSV 파일로 저장
            output_file = os.path.join(complex_output_dir, f"{complex_name}_Label_Group_{label}.csv")
            try:
                group.to_csv(output_file, index=False, encoding='utf-8-sig')
                print(f"Label {label}번에 해당하는 데이터를 {output_file}에 저장했습니다.")
            except Exception as e:
                print(f"파일 {output_file} 저장 중 오류 발생: {e}")
