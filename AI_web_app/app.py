from api.AI import AIAPI
import streamlit as st


@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")


def main():
    api = get_api()

    st.title("2023 HAI 여름방학 Web APP 개발 과제")

    st.subheader("Image to Text")
    st.markdown("- ocr을 이용해 이미지를 텍스트로 바꿔줍니다\n- AI를 이용해 텍스트를 요약합니다")
    query = st.file_uploader("Input Image")
    if query:
        st.image(query)
        response = api.query_image2text(query)
        st.markdown("**OCR result**")
        st.code(f"{response}", language="python")
        
        title, summary = api.query_text2text(response)

        st.markdown("**AI Summary**")
        st.markdown("- **Title**")
        st.code(f"{title}", language="csv")
        st.markdown("- **Summary**")
        st.code(f"{summary}", language="csv")
        
        
    st.subheader("Text Summary")
    st.markdown("- AI를 이용해 텍스트를 요약합니다")
    query = st.text_input('Input Text', "여기에 텍스트 입력", key="text2text")
    title, summary = api.query_text2text(query)

    st.markdown("**AI Summary**")
    st.markdown("- **Title**")
    st.code(f"{title}", language="csv")
    st.markdown("- **Summary**")
    st.code(f"{summary}", language="csv")
    
    
    st.subheader("Text Translate")
    st.markdown("- AI를 이용해 텍스트를 다른 언어로 번역합니다")
    text = st.text_input('Input Text', "여기에 텍스트 입력", key="translate")
    lang = st.radio(label="Language", options=["Korean", "English", "Japanese", "Chinese"])
    translate = api.query_translate(text, lang)
    st.code(f"{translate}", language="csv")
        
if __name__ == '__main__':
    main()
