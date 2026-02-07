import streamlit as st

st.title("안녕하세요 Streamlit")

st.header("헤더를 입력할 수 있어요 :sunglasses:")

st.subheader("이것은 subheader 입니다")

st.text("일반적인 텍스트 출력")

sample_code = '''
def function():
    print('hello, world')
'''

st.code(sample_code)

st.markdown('streamlit은 **마크다운** 문법 지원합니다')

st.table([
    ['이름', '나이'],
    ['홍길동', '43'],
    ['뽀로로', '23'],
]
)

st.matrix(label='삼성전자', value = '151200원', )

st.title('write()')
st.write("Hello")
st.write(10, 20, 30)
st.write([1, 2, 3, 4])
st.write({"x": 100, "y": 3.14})