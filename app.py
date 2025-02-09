import vertexai
import streamlit as st
from vertexai.preview.vision_models import ImageGenerationModel

## Config's
PROJECT_ID= "vital-cedar-443204-f3"
output_file= "output.png"

st.header("Image Generation using Google ImagGen 3.0")

with st.sidebar.header("Parameters"):
    prompt = st.sidebar.text_area("Please enter your prompt to generate image")

    vertexai.init(project=PROJECT_ID, location="us-central1")

    col_1, col_2 = st.columns(2)

    with col_1:
        num_of_images = st.sidebar.radio(
        "Specify No of Images to be Generated",
        ["**1**", "**2**"]  # You can add up more or decrease according to your requitements.
    )

    with col_2:
        aspect_ratio = st.sidebar.selectbox(
        "Please select the aspect",
        ["1:1", "9:16", "16:9", "3:4", "4:3"],
    )

    st.sidebar.write("---")

    generate_button_clicked =st.sidebar.button("Generate Image")


if generate_button_clicked:

    with st.spinner("Generating Image..."):
        ## Model
        model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

        images = model.generate_images(
            prompt= prompt,
            number_of_images= num_of_images,
            aspect_ratio= aspect_ratio,
            safety_filter_level= "block_some",
            
        )

        ## Save the Image
        images[0].save(location= output_file, include_generation_parameters=False)
        st.write(f"Created output image using {len(images[0]._image_bytes)} bytes")
        st.image(output_file)



