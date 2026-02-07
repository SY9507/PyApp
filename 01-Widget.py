import streamlit as st

import os, time

print(f"✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}")

st.title("다양한 widget들")

model = st.selectbox("모델선택", ("GPT-3", "GPT-4", "GPT-5"))

st.markdown(f"model: :green[{model}]")

name = st.text_input("이름이 무엇입니까?")
st.markdown(f"이름: :red[{name}]")


button = st.button("버튼을 눌러보세요")
if button:
    st.write(":blue[버튼] 이 눌렸습니다 :sparkles:")

st.markdown('---')
num1 = st.number_input('숫자1 입력',
    min_value=10, max_value=100, step=5)
num2 = st.number_input('숫자2 입력',
    min_value=10, max_value=100, step=5)

btn_calc = st.button('계산을 합니다')

if btn_calc:
    st.markdown(f"""
            {num1} + {num2} = {num1 + num2}
            
            {num1} - {num2} = {num1 - num2}
            """)