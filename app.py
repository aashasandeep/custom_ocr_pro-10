import streamlit as st
import easyocr
from PIL import Image, ImageDraw
import numpy as np
import cv2
import time  # For the loading effect

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #FF4B4B;
            text-align: center;
        }
        .sub-title {
            font-size: 20px;
            font-weight: bold;
            color: #444;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

def draw_boxes(image, results):
    """Draw bounding boxes and text labels on the image."""
    img = image.copy()
    draw = ImageDraw.Draw(img)

    for (bbox, text, prob) in results:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))

        # Draw bounding box
        draw.rectangle([top_left, bottom_right], outline="red", width=2)

        # Overlay extracted text
        draw.text((top_left[0], top_left[1] - 10), text, fill="red")

    return img

def main():
    # App Title
    st.markdown('<p class="main-title">📄 OCR Text Extraction App</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Extract text from images with bounding boxes</p>', unsafe_allow_html=True)

    # Sidebar for uploading an image
    st.sidebar.header("📂 Upload Lab Report Image")
    uploaded_file = st.sidebar.file_uploader("Choose an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Load the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert to numpy array
        image_np = np.array(image)

        # Loading spinner while processing
        with st.spinner("🔍 Extracting text... Please wait."):
            time.sleep(2)  # Simulate processing delay
            reader = easyocr.Reader(['en'])
            results = reader.readtext(image_np)

        # Draw bounding boxes
        image_with_boxes = draw_boxes(image, results)

        # Display the modified image
        st.image(image_with_boxes, caption="Text Detection Output", use_container_width=True)

        # Display extracted text
        st.subheader("📜 Extracted Text:")
        extracted_text = "\n".join([text[1] for text in results])

        if extracted_text:
            st.text_area("Detected Text:", extracted_text, height=200)
        else:
            st.warning("⚠️ No text detected in the image!")

        # Download button for extracted text
        st.download_button(
            label="📥 Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
