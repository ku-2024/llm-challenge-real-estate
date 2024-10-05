import os
import pandas as pd
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
upstage_api_key = os.getenv("UPSTAGE_API_KEY")

assert "UPSTAGE_API_KEY" in os.environ, "Please set the UPSTAGE_API_KEY environment variable"

llm = ChatUpstage(model="solar-1-mini-chat")


# label 설명 dictionary
label_descriptions = {
    "0": "환경(단지, 조경)",
    "1": "커뮤니티",
    "2": "동별 특징",
    "3": "주변 상권",
    "4": "교통",
    "5": "학군",
    "6": "소음",
    "7": "주차"
}


# 상위 입력 디렉토리 설정
base_input_dir = "./processed_data"
base_output_dir = "./summary"


few_shot_prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert in analyzing and summarizing user reviews related to apartment living environments. You should prioritize information related to residential environment, community facilities, and overall living experience, and avoid any biased or overly subjective statements. All summaries must be provided in Korean."
    ),
     (
        "user",
        """
        [Instruction]
        You are a helpful assistant that summarizes and provides comprehensive insights based on user reviews about various aspects of an apartment complex. The reviews are categorized into topics such as environment, community, or transportation. Your task is to summarize these reviews to provide clear and concise information related to the topic of '{label_description}'.

        [Context]
        Summarize the reviews below in a detailed and comprehensive manner, focusing on key points related to '환경(단지, 조경)', using a professional and neutral tone to aggregate the opinions, highlighting important features and general sentiments expressed in the reviews in more than 9 sentences to ensure all perspectives and nuances are adequately captured. Do not make a newline or line break.

        Reviews: '단지 내 조경이 매우 잘 되어 있어 사계절 내내 아름다운 풍경을 즐길 수 있습니다. 산책로가 단지 곳곳에 있어 자연을 느끼며 여유로운 산책을 즐기기 좋습니다. 봄에는 벚꽃이 만개하고 가을에는 단풍이 물들어 계절의 변화를 가까이에서 느낄 수 있습니다. 작은 공원과 정원이 단지 내 여러 곳에 자리 잡고 있어 아이들이 뛰어놀기에 안전합니다. 나무와 잔디가 잘 어우러져 있어 산책이나 운동을 하기에 매우 좋은 환경입니다. 아파트 내 조경이 마치 도심 속 작은 숲처럼 조성되어 있어 매우 쾌적합니다. 밤에는 조명이 아름답게 들어와 산책할 때 더욱 로맨틱한 분위기를 자아냅니다. 꽃과 나무가 어우러진 산책로는 입주민들이 함께 걷기에도 좋은 공간입니다. 단지 내 산책로와 벤치가 잘 정비되어 있어 이웃들과 자연스럽게 대화 나누기 좋습니다. 여름철에도 단지 내 그늘이 많아 시원하고 쾌적한 환경을 제공합니다. 아파트 정문 앞에 위치한 커다란 나무가 이 단지의 상징으로 자리 잡고 있습니다. 물이 흐르는 작은 연못이 있어 거주민들의 휴식 공간으로 인기가 높습니다. 아이들이 뛰어놀 수 있는 넓은 잔디밭이 있어 가족 단위로 생활하기에 좋습니다. 단지 내 다양한 나무와 꽃들이 심어져 있어 마치 작은 식물원을 연상케 합니다. 특히 여름철 단지 내 나무에서 들리는 새소리는 도심 속에서 느낄 수 없는 매력을 선사합니다. 산책로를 따라 조명이 설치되어 있어 저녁 산책이나 운동도 안전하게 할 수 있습니다. 단지 내 정원이 매우 정갈하게 관리되어 있어 항상 깨끗하고 쾌적한 느낌을 줍니다. 가을에는 단풍이 물들어 아름다운 단지 전경을 볼 수 있어 입주민들 사이에서 큰 호응을 얻고 있습니다. 단지 내에 꽃길이 조성되어 있어 봄이면 각종 꽃들이 만개하여 경관이 아름답습니다. 아파트를 둘러싼 나무들이 많아 도심 속에서도 자연과 함께 생활하는 기분을 느낄 수 있습니다.'

        Summary: '해당 아파트 단지는 조경이 잘 되어 있어 입주민들이 자연을 느끼며 생활하기에 매우 적합합니다. 단지 내에는 다양한 산책로와 휴식 공간이 마련되어 있어, 계절에 따라 변하는 아름다운 풍경을 즐길 수 있습니다. 특히 봄에는 벚꽃이 만개하여 산책로가 매우 아름다우며, 여름에는 푸른 나무들이 그늘을 제공해 쾌적한 환경을 유지합니다. 또한, 단지 내 작은 공원들이 곳곳에 있어 아이들이 안전하게 뛰어놀 수 있는 공간이 많습니다. 이러한 조경시설은 단지 내 거주민들의 만족도를 높이며, 이웃 간의 교류도 활발하게 이루어지게 합니다. 산책이나 운동을 좋아하는 사람들에게 특히 좋은 환경으로, 도심 속에서도 자연과 함께하는 생활을 할 수 있어 거주 만족도가 높습니다.'
        """
    ),
    (
        "user",
        """
        [Instruction]
        You are a helpful assistant that summarizes and provides comprehensive insights based on user reviews about various aspects of an apartment complex. The reviews are categorized into topics such as environment, community, or transportation. Your task is to summarize these reviews to provide clear and concise information related to the topic of '{label_description}'.

        [Context]
        Summarize the reviews below in a detailed and comprehensive manner, focusing on key points related to '커뮤니티', using a professional and neutral tone to aggregate the opinions, highlighting important features and general sentiments expressed in the reviews in more than 9 sentences to ensure all perspectives and nuances are adequately captured. Do not make a newline or line break.
        Reviews: '단지 내 커뮤니티 센터에 수영장과 헬스장이 잘 갖추어져 있어 운동을 좋아하는 사람들에게 좋습니다. 커뮤니티 센터에서는 다양한 문화 프로그램을 운영해 입주민 간 교류가 활발히 이루어집니다. 입주민들만 이용할 수 있는 카페와 독서실이 마련되어 있어 휴식과 학습 모두 가능한 공간입니다. 자녀들을 위한 키즈카페와 도서관이 단지 내에 있어 아이들이 놀면서 공부할 수 있는 환경입니다. 주말마다 열리는 요가 강좌와 문화교실이 인기가 많아 많은 입주민들이 참여하고 있습니다. 커뮤니티 센터 내 수영장은 어른과 아이 모두 이용할 수 있어 가족 단위로 오기 좋습니다. 매월 커뮤니티 내에서 열리는 플리마켓은 입주민들이 서로 교류할 수 있는 기회를 제공합니다. 입주민 전용 영화관이 있어 주말 저녁에 가족끼리 영화 보기에 좋습니다. 단지 내에 여러 개의 헬스장이 분산되어 있어 운동할 때 혼잡하지 않고 쾌적합니다. 커뮤니티 내 스터디 룸이 있어 학생들이 조용히 공부할 수 있는 공간이 마련되어 있습니다. 주민 커뮤니티 모임이 활성화되어 있어 새로운 입주민도 쉽게 이웃들과 친해질 수 있습니다. 입주민들을 위한 무료 강좌가 주기적으로 열려 다양한 취미를 가질 수 있습니다. 커뮤니티 내 테니스장과 골프 연습장이 있어 스포츠를 즐기기 좋아요. 입주민 전용 카페테리아가 있어 이웃들과 가볍게 커피를 마시며 대화하기 좋습니다. 아이들을 위한 놀이방과 어르신들을 위한 휴식 공간이 분리되어 있어 편리합니다. 단지 내 피트니스 센터가 최신식 장비로 잘 갖추어져 있어 운동을 즐기기 좋습니다. 커뮤니티 센터 내 독서실은 조용하고 깔끔하게 관리되어 있어 학생들 사이에서 인기가 높습니다. 단지 내 주민들의 건의사항을 반영해 지속적으로 커뮤니티 시설이 개선되고 있습니다. 주민들이 함께 참여할 수 있는 다양한 체육대회와 이벤트가 주기적으로 열려 단합이 잘 됩니다. 어린 자녀들을 위한 미술 교실과 음악 교실이 운영되어 자녀 교육에도 도움이 됩니다.'

        Summary: '단지 내 커뮤니티 시설은 다양한 연령대가 이용할 수 있도록 잘 갖추어져 있습니다. 수영장, 헬스장, 골프 연습장 등 다양한 운동 시설이 있어 건강한 생활을 도모할 수 있으며, 아이들을 위한 놀이터도 곳곳에 마련되어 있어 자녀를 키우는 가정에게 적합합니다. 또한, 커뮤니티 센터에서는 다양한 문화 프로그램과 주민 대상의 강좌도 운영되어 입주민 간 교류와 정보 공유의 장이 되고 있습니다. 독서실과 카페 같은 공간도 있어 학업이나 업무에 집중할 수 있는 장소로도 활용할 수 있습니다. 이러한 커뮤니티 시설은 주민들의 삶의 질을 높이며, 자주 이용하는 입주민들 사이에 친밀감을 형성하는데도 도움이 됩니다.'
        """
    ),
    (
        "user",
        """
        [Instruction]
        You are a helpful assistant that summarizes and provides comprehensive insights based on user reviews about various aspects of an apartment complex. The reviews are categorized into topics such as environment, community, or transportation. Your task is to summarize these reviews to provide clear and concise information related to the topic of '{label_description}'.

        [Context]
        Summarize the reviews below in a detailed and comprehensive manner, focusing on key points related to '{label_description}', using a professional and neutral tone to aggregate the opinions, highlighting important features and general sentiments expressed in the reviews in more than 9 sentences to ensure all perspectives and nuances are adequately captured. Do not make a newline or line break.

        Reviews:\n{combined_text}
        
        Summary:
        """
    )
])


# 상위 디렉토리의 모든 하위 폴더를 탐색
for complex_name in os.listdir(base_input_dir):
    complex_input_dir = os.path.join(base_input_dir, complex_name)  # 하위 폴더 경로 설정
    complex_output_dir = os.path.join(base_output_dir, complex_name)  # 하위 폴더에 맞는 출력 경로 설정
    
    # 하위 폴더가 실제 폴더인지 확인 (파일이 아닌 폴더만 탐색)
    if not os.path.isdir(complex_input_dir):
        continue
    
    # 출력 폴더 생성
    os.makedirs(complex_output_dir, exist_ok=True)

    # 하위 폴더 내 CSV 파일들을 탐색하여 처리
    for label_file in os.listdir(complex_input_dir):
        # 파일이 Label_Group_ 패턴에 맞는지 확인
        if label_file.startswith(f"{complex_name}_Label_Group_") and label_file.endswith(".csv"):
            label_path = os.path.join(complex_input_dir, label_file)
            try:
                # CSV 파일 읽기
                data = pd.read_csv(label_path, sep=',', quotechar='"', on_bad_lines='skip')

                # 파일 이름에서 라벨 번호 추출
                label = label_file.split("_")[-1].split(".")[0]
                label_description = label_descriptions.get(label, "기타")  # label 설명 가져오기

                # "text" 열의 모든 텍스트를 결합
                combined_text = " ".join(data["text"].astype(str).tolist())

                # 템플릿, LLM, 파서를 사용하여 체인 생성
                chain = few_shot_prompt_template | llm | StrOutputParser()

                # 체인을 사용하여 요약 생성하고 결과 저장
                summary = chain.invoke({
                    "label": label,
                    "combined_text": combined_text,
                    "label_description": label_description,
                    "temperature": 0.25,  # 낮추면 robust, 높이면 창의력이라 생각하면 됨
                    "top_p": 0.85         # temp로 만든 확률을 어디까지 고려할지
                })

                # 요약 결과를 출력 디렉토리에 저장
                output_file = f"{complex_output_dir}/Label_Summary_{label}.txt"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(summary)

                print(f"Label {label}번에 대한 요약이 {output_file}에 저장되었습니다.")

            except Exception as e:
                print(f"파일 {label_file} 처리 중 오류 발생: {e}")

