import streamlit as st
from PIL import Image
from io import BytesIO
import requests


def display_inspirational_text_and_image(image_url):
    # 从网络链接加载图片
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # 设置页面布局
    col1, col2 = st.columns([2, 1])

    # 在左侧列显示励志短文
    with col1:
        inspirational_text = """
        # 奖励尹烁琦1万元人民币

        鉴于尹烁琦在文谷优秀的表现:

        - 优秀足球运动员
        - 优秀篮球运动员
        - 优秀进步学生
        - 优秀宿舍长

        决定奖励1万元人民币
        """
        st.markdown(inspirational_text)

    # 在右侧列显示图片
    with col2:
        st.image(image, caption='优秀学员')


if __name__ == '__main__':
    st.set_page_config(page_title="Inspirational Text and Image")
    st.title("文谷重大好消息")

    # 图片链接
    image_url = "https://s21.ax1x.com/2024/07/26/pkbbmcV.jpg"

    display_inspirational_text_and_image(image_url)