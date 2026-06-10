import os
import streamlit as st
from openai import OpenAI
import base64
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

st.title('🎁 제품 홍보 포트서 생성기')
keyword = st.text_input("키워드를 입력하세요.")

if st.button('생성하기 🔥'): 
    with st.spinner("✨ 생성중..."):
        response =  client.responses.create(
                    model="gpt-4.1-mini",
                    instructions="입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                    input= keyword)
        result = response.output_text
        img = client.images.generate(
            model="gpt-image-1.5",
            prompt= result,
            n=1,
            size="1024x1024"
        )

    # api가 반환하는 이미지는 Base64로 인코딩된 이미지 문자열임. 
    # base64 라이브러리를 활용해. 디코딩해준 뒤 st.image에 전달
    image_bytes = base64.b64decode(img.data[0].b64_json)
    
    st.write(result)    
    st.image(image_bytes)
