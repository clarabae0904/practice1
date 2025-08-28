# Main.py
# 🦈 NASA Hackathon 실전 연습 코드

import pandas as pd
import numpy as np
import folium

# 1) 가짜 데이터 만들기 (상어 10마리의 위치 - 경도, 위도)
coords = np.random.rand(10, 2) * [360, 180] - [180, 90]
df = pd.DataFrame(coords, columns=["Longitude", "Latitude"])

print("🐋 상어 위치 데이터 (샘플):")
print(df)

# 2) 데이터 분석: 상어 무리의 중심 좌표 구하기
mean_long = df["Longitude"].mean()
mean_lat = df["Latitude"].mean()
print("\n📍 상어 무리 중심 좌표:")
print(f"Longitude: {mean_long:.2f}, Latitude: {mean_lat:.2f}")

# 3) 지도 시각화
# 지도 중심을 평균 좌표로 설정
m = folium.Map(location=[mean_lat, mean_long], zoom_start=2)

# 개별 상어 위치 표시 (파란 점)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5, color="blue"
    ).add_to(m)

# 평균 위치 표시 (빨간 점)
folium.Marker(
    location=[mean_lat, mean_long],
    popup="Shark Cluster Center",
    icon=folium.Icon(color="red")
).add_to(m)

# 4) HTML로 저장
m.save("sharks_map.html")
print("\n🌍 지도 저장 완료: sharks_map.html (더블클릭해서 열어보세요)")
