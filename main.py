import streamlit as st

st.set_page_config(
    page_title="MBTI 운동 추천",
    page_icon="🏃",
    layout="centered"
)

st.title("🏃 MBTI 운동 추천기")
st.markdown("""
나의 MBTI를 선택하면 ✨  
어울리는 운동 2가지를 추천해줄게!
""")

exercise_data = {
    "INTJ": ["🏋️ 웨이트 트레이닝", "🏃 마라톤"],
    "INTP": ["🧗 클라이밍", "🚴 사이클"],
    "ENTJ": ["🏆 크로스핏", "🏀 농구"],
    "ENTP": ["🥋 태권도", "⚽ 풋살"],
    "INFJ": ["🧘 요가", "🚶 파워 워킹"],
    "INFP": ["🏊 수영", "🚴 자전거 타기"],
    "ENFJ": ["💃 댄스", "🏐 배구"],
    "ENFP": ["🏸 배드민턴", "🕺 줌바"],
    "ISTJ": ["🏃 조깅", "🏋️ 웨이트 트레이닝"],
    "ISFJ": ["🚶 걷기", "🧘 필라테스"],
    "ESTJ": ["⚽ 축구", "🏋️ 크로스핏"],
    "ESFJ": ["🏐 배구", "🏸 배드민턴"],
    "ISTP": ["🧗 클라이밍", "🚵 MTB 자전거"],
    "ISFP": ["🏊 수영", "🧘 요가"],
    "ESTP": ["🏀 농구", "🥊 복싱"],
    "ESFP": ["💃 댄스", "⚽ 풋살"]
}

mbti = st.selectbox(
    "🔍 MBTI를 선택해봐!",
    list(exercise_data.keys())
)

if st.button("✨ 운동 추천 받기"):
    st.success(f"🎉 {mbti} 유형에게 추천하는 운동이야!")

    for i, exercise in enumerate(exercise_data[mbti], start=1):
        st.markdown(f"### {i}. {exercise}")

    st.balloons()

st.caption("🌟 MBTI는 참고용! 가장 중요한 건 내가 즐겁게 할 수 있는 운동이야 😊")
