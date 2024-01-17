# Gemini Post Generator

Gemini is a Python-based tool that generates social media posts using Google's GenerativeAI. The tool provides a streamlined interface to create engaging Facebook posts with customizable templates.

## Features

- **Google GenerativeAI Integration:** Utilizes the power of Google GenerativeAI to generate creative and engaging social media posts.

- **Flexible Templates:** Offers two customizable templates for generating Facebook posts, allowing you to tailor the content to your specific topic.

- **Image Integration:** Retrieves relevant images from Unsplash to complement your generated post.

- **Text Overlay on Images:** Enhances generated images by overlaying text at specified positions with customizable settings.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install Python:**
    Ensure that you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **API Key Configuration:**
    Obtain your Google GenerativeAI API key from [Google Maker Suite](https://makersuite.google.com/app/apikey) and replace `YOU_API_KEY` in `functions.py` with your actual API key.

5. **Unsplash API Key:**
    Replace `YOUR_UNSPLASH_API_KEY` in `functions.py` with your Unsplash API key.

## Usage

1. Run the application using:
    ```bash
    streamlit run app.py
    ```

2. Enter a topic and click the "Get the Post" button to generate a Facebook post.

3. Adjust the sliders and color picker to overlay text on the generated image.

4. View the final output and the post text.

## Examples

Here's an example usage of Gemini to create a Facebook post:

```python
python app.py
