import requests
import json

'''
사용 전, 파일의 51번째 줄에 사용자의 API KEY를 입력해주세요
'''

# 날씨 예측(3시간 간격)
def get_weather_forecast(city, api_key):
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=kr"
    response = requests.get(url)
    return response.json()

#기온과 체감 온도를 바탕으로 다양한 옷차림을 추천
def recommend_clothing(temperature):
    
    clothes = []

    if temperature >= 28:
        clothes = ["반팔", "반바지", "선크림", "모자"]
    elif 23 <= temperature < 28:
        clothes = ["반팔", "얇은 셔츠", "얇은 긴팔티", "반바지", "면바지"]
    elif 20 <= temperature < 23:
        clothes = ["얇은 가디건", "긴팔티", "셔츠", "블라우스", "후드티", "면바지", "슬랙스", "7부 바지"]
    elif 17 <= temperature < 20:
        clothes = ["얇은 니트", "얇은 가디건", "얇은 재킷", "바람막이", "후드티", "맨투맨", "슬랙스", "긴바지"]
    elif 12 <= temperature < 17:
        clothes = ["재킷", "가디건", "야상", "맨투맨", "후드티", "청바지", "면바지"]
    elif 9 <= temperature < 12:
        clothes = ["재킷", "야상", "점퍼", "트렌치 코트", "청바지", "면바지", "니트"]
    elif 5 <= temperature < 9:
        clothes = ["(울)코트", "가죽 자켓", "청바지", "기모바지", "니트"]
    else:  # 기온이 5도 미만일 경우
        clothes = ["패딩", "두꺼운 코트", "장갑", "목도리", "스카프", "내복"]

    return clothes
#일교차가 큰 경우 경고 메시지를 출력하는 함수
def check_temperature_range(min_temp, max_temp):
    
    temp_difference = max_temp - min_temp
    
    if temp_difference >= 10:
        return "오늘은 일교차가 큽니다. 저녁에 외부 활동이 있다면 겉옷을 챙기는 것을 추천합니다:)"
    else:
        return "오늘은 일교차가 크지 않습니다:)"

def main():
    city = input("날씨를 알고 싶은 도시를 영문으로 입력하세요 (예: Seoul,KR): ")
    apikey = "User_API_Key"  # 실제 API 키로 변경하기!!!

    # 날씨 예측 데이터를 가져옴
    data = get_weather_forecast(city, apikey)

    print(f"***{data['city']['name']}의 날씨***")

    # 3시간 간격으로 예측된 기온 데이터에서 최저 기온과 최고 기온 계산
    temperatures = [entry['main']['temp'] for entry in data['list']]
    min_temp = min(temperatures)  # 최저 기온
    max_temp = max(temperatures)  # 최고 기온

    # 날씨 상태
    print("날씨는 ", data["list"][0]["weather"][0]["description"], "입니다.")

    # 현재 온도 (첫 번째 3시간 예측 데이터)
    current_temp = data['list'][0]['main']['temp']
    print("현재 온도는 ", current_temp, "°C,")

    print("최저 기온은 ", min_temp, "°C,")
    print("최고 기온은 ", max_temp, "°C 입니다.")

    # 기온에 따른 겉옷 추천
    clothing_suggestion = recommend_clothing(current_temp)
    print("추천 옷차림: ", ", ".join(clothing_suggestion))

    # 일교차에 따른 경고 메시지 출력
    temperature_warning = check_temperature_range(min_temp, max_temp)
    print(temperature_warning)

if __name__ == '__main__':
    main()