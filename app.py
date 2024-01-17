from functions import *


st.header("Make a Post using Gemini")

topic = st.text_input("Enter the Topic")

prompt = prompt1

if st.button("Get the Post"):
    st.session_state.response = gemini(prompt, topic)
    st.write(f"```{st.session_state.response}")
    st.session_state.image_urls = get_images(topic)
    st.session_state.image = st.session_state.image_urls[0]
    st.image(st.session_state.image, caption="Image", use_column_width=True)

try:
    st.session_state.text_to_overlay = st.session_state.response

    col1, col2, col3 = st.columns(3)

    # Add a slider to the first column for x value in percentage
    with col1:
        x_percent = st.slider("X Value (%)", min_value=0, max_value=100, value=50)

    # Add a slider to the second column for y value in percentage
    with col2:
        y_percent = st.slider("Y Value (%)", min_value=0, max_value=100, value=50)

    # Add a slider to the third column for text size
    with col3:
        text_size = st.slider("Text Size", min_value=10, max_value=100, value=30)

    # Add a color picker for text color
    text_color = st.color_picker("Text Color", "#000000")


    output_path = "output_image.jpg"
    img = overlay_text_on_image(st.session_state.image, st.session_state.text_to_overlay, output_path, x_percent, y_percent, text_size, text_color)

    st.image(img, caption="Image with Text Overlay.", use_column_width=True)
    st.write(f"```{st.session_state.response}")
except:
    pass

