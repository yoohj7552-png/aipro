import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="🚀",
    layout="centered"
)

st.title("🌟 MBTI 진로 추천기")
st.markdown(
    """
    나의 MBTI를 선택하면 ✨  
    어울리는 진로 2가지와 추천 학과, 성격 특징을 알려줄게!
    """
)

career_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 분석적인 사람"
        },
        {
            "career": "📊 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "전략적으로 생각하는 사람"
        }
    ],
    "INTP": [
        {
            "career": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "호기심이 많고 문제 해결을 좋아하는 사람"
        },
        {
            "career": "🔬 연구원",
            "major": "자연과학계열",
            "personality": "탐구심이 강한 사람"
        }
    ],
    "ENTJ": [
        {
            "career": "🏢 기업 CEO",
            "major": "경영학과",
            "personality": "리더십이 뛰어난 사람"
        },
        {
            "career": "📈 프로젝트 매니저",
            "major": "산업공학과, 경영학과",
            "personality": "목표 달성에 적극적인 사람"
        }
    ],
    "ENTP": [
        {
            "career": "🚀 창업가",
            "major": "경영학과",
            "personality": "아이디어가 풍부한 사람"
        },
        {
            "career": "📢 마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "새로운 도전을 즐기는 사람"
        }
    ],
    "INFJ": [
        {
            "career": "🎓 상담교사",
            "major": "교육학과, 상담심리학과",
            "personality": "공감 능력이 뛰어난 사람"
        },
        {
            "career": "🧑‍⚕️ 심리상담사",
            "major": "심리학과",
            "personality": "타인의 성장을 돕고 싶은 사람"
        }
    ],
    "INFP": [
        {
            "career": "✍️ 작가",
            "major": "국문학과, 문예창작학과",
            "personality": "감수성이 풍부한 사람"
        },
        {
            "career": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "창의력이 뛰어난 사람"
        }
    ],
    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 것을 좋아하는 사람"
        },
        {
            "career": "🤝 인사담당자",
            "major": "경영학과",
            "personality": "배려심이 많은 사람"
        }
    ],
    "ENFP": [
        {
            "career": "🎤 콘텐츠 크리에이터",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지가 넘치고 표현력이 좋은 사람"
        },
        {
            "career": "📣 광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적인 아이디어를 좋아하는 사람"
        }
    ],
    "ISTJ": [
        {
            "career": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "책임감이 강한 사람"
        },
        {
            "career": "💰 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 체계적인 사람"
        }
    ],
    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊은 사람"
        },
        {
            "career": "👶 사회복지사",
            "major": "사회복지학과",
            "personality": "도움을 주는 것을 좋아하는 사람"
        }
    ],
    "ESTJ": [
        {
            "career": "📋 행정 관리자",
            "major": "행정학과",
            "personality": "조직 관리 능력이 뛰어난 사람"
        },
        {
            "career": "🏦 금융 전문가",
            "major": "경제학과",
            "personality": "현실적이고 계획적인 사람"
        }
    ],
    "ESFJ": [
        {
            "career": "🎓 초등교사",
            "major": "교육학과",
            "personality": "친절하고 협력적인 사람"
        },
        {
            "career": "💼 인사 관리자",
            "major": "경영학과",
            "personality": "사람들과 잘 어울리는 사람"
        }
    ],
    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "실용적이고 문제 해결을 좋아하는 사람"
        },
        {
            "career": "✈️ 항공정비사",
            "major": "항공정비 관련 학과",
            "personality": "손으로 직접 만드는 것을 좋아하는 사람"
        }
    ],
    "ISFP": [
        {
            "career": "🎨 그래픽 디자이너",
            "major": "시각디자인학과",
            "personality": "예술적 감각이 뛰어난 사람"
        },
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감성을 표현하는 것을 좋아하는 사람"
        }
    ],
    "ESTP": [
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람 만나는 것을 좋아하는 사람"
        },
        {
            "career": "🎬 방송 리포터",
            "major": "미디어커뮤니케이션학과",
            "personality": "순발력이 뛰어난 사람"
        }
    ],
    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화학과",
            "personality": "표현력이 뛰어난 사람"
        },
        {
            "career": "🎤 행사 기획자",
            "major": "관광경영학과",
            "personality": "사람들과 즐겁게 소통하는 사람"
        }
    ]
}

mbti = st.selectbox(
    "🔍 나의 MBTI를 선택해봐!",
    list(career_data.keys())
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"🎉 {mbti} 유형에게 추천하는 진로야!")

    for idx, item in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.markdown(f"**🎓 추천 학과**\n\n{item['major']}")
        st.markdown(f"**💡 잘 어울리는 성격**\n\n{item['personality']}")
        st.markdown("---")

    st.balloons()

st.caption("🌈 MBTI는 참고용일 뿐! 진로는 자신의 흥미와 적성을 함께 고려하는 것이 가장 중요해 😊")
