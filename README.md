# Text-to-Image-using-Google-Image-Generation-Models
This application uses Google Vertex AI - Google Image Generation models to convert the given text into images, also here we have capabilities to select a few ratio aspects and no of images to be generated.

# Image Generation using Google Imagen 3.0

This project is a simple Streamlit-based web application that generates images using Google Cloud's Imagen 3.0 model.

## Features

- Generates AI-generated images from text prompts.
- Supports multiple aspect ratios.
- Allows users to specify the number of images.
- Interactive Streamlit UI for an easy user experience.

## Installation and Setup

### Prerequisites

- Python 3.8+
- Google Cloud account with Vertex AI enabled
- Streamlit installed
- Google Cloud SDK installed and authenticated

### Set Up Google Cloud Authentication

Follow this link to setup local authorization to use Google Vertex AI Services: https://cloud.google.com/sdk/docs/initializing

## Installing Dependencies

Create a `requirements.txt` file with the following dependencies:

```sh
vertexai
streamlit
```

1. Clone the repository:
   ```sh
   git clone https://github.com/kakarlapudiakhilvarma1/Text-to-Image-using-Google-Image-Generation-Models.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Text-to-Image-using-Google-Image-Generation-Models
   ```
3. Create a virtual environment and activate it:
   ```sh
   conda create -p myenv python==3.10 -y
   conda activate myenv/   # On Windows 
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure you have set up authentication (as described above).
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Output Screenshots

![image](https://github.com/user-attachments/assets/51c585f0-6309-4c7e-b118-3e517a012237)

---
### Generated Image
![image](https://github.com/user-attachments/assets/54f036c1-2773-4df8-8aa7-3e7d3680f494)
---
![image](https://github.com/user-attachments/assets/6f11ecfb-d1cd-412c-bc17-5eff4cbcc81d)



## Notes

- Ensure your Google Cloud project has billing enabled to use Vertex AI's Imagen model.
- Customize the prompt and parameters in the script to experiment with different generations.
- Make sure `GOOGLE_APPLICATION_CREDENTIALS` is set before running the app.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests to improve the project.

---

Let me know if you need any modifications! 🚀
