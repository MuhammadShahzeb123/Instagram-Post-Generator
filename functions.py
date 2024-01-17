import streamlit as st
import google.generativeai as  genai
import requests
from PIL import Image
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO

topic = None

prompt1 = f"""I'm going to train you to turn social media posts into reusable templates. You will be given a template and you should return the following:

A Post for facebook usually between 200-300 Characters and nothing more. (Don't include you saying, "Here is the Post or any other thing because your response will be directly used.")

Here are your guidelines:
• Remove details that are too specific.
• Remove or replace details that are too specific, including colloquialisms, idioms, or unique expressions.
• Fill up the Placeholders according to the Topic and make it readable for a 3rd Grader.
• If the post is too specific to make general enough for other topics, just recommend to skip it or only return templates for the hook, not the full post
• The post MUST have a list related to the post.
• Make sure to bullet point the list using `•`. This will help me a lot

Here is what you must NOT do:
• Don't create a single line post. (Always use New Lines for better reading)
• Don't simply throw a Quote from any noble person
• Don't Include Double Qutations 
• Don't use Jargons

Here is an example Post: 

"You don't need a website.
You don't need a podcast.
You don't need a product.
You don't need a team.

You just need to understand how to get email addresses. That's it."


These are the Templates you need. You MUST create the post like this. You MUST NOT repurpose the post and give it to me. Search about the Topic I have given to you and Then fill in the blanks yourself.
##Template1:
"You don't need [thing 1]
You don't need [thing 2]
You don't need [thing 3]
You don't need [thing 4]

You just need [action] for [outcome]"

##Template 2:"Stop trying to:

[Short-Term Outcome]

[Short-Term Outcome]

[Short-Term Outcome]

Instead, just focus on [Action Step].

The rest will take care of itself."

You can change these Variables Accourding to the Topic. I want you to search about the Topic I will give you and fill in all these Black and Variables

Do you understand?

If yes, then:

I am gonna give you a Topic and you have to generate the post for Facebook according to instructions above. You can use any of the templates and fill out the blank also. I don't want you to give me a repurposed Template and left the blanks for me to fill out. Here is the Topic: """




def gemini(prompt: str, topic: str) -> str:
    genai.configure(api_key="YOUR_API_KEY") # get the API key from https://makersuite.google.com/app/apikey . It is FREE YOU_API_KEY

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config={
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        },
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ],
    )
    prompt_main = "Topic: " + topic + prompt
    response = model.generate_content(prompt_main)
    print(response.text)
    return response.text

UNSPLASH_API_KEY = "YOUR_API_KEY"
api_url = "https://api.unsplash.com/photos/random"

def get_images(query, count=3):
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_API_KEY}"
    }

    params = {
        "query": query,
        "count": count
    }

    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_urls = [photo["urls"]["regular"] for photo in data]
        return image_urls
    else:
        st.error(f"Error: {response.status_code}")
        return []


import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO

def overlay_text_on_image(image_url, text, output_path, x_percent, y_percent, text_size, text_color, brightness_factor=0.2):
    # Download the image from the URL
    response = requests.get(image_url)
    
    # Read the image from the response content
    img = Image.open(BytesIO(response.content))

    # Get image dimensions
    img_width, img_height = img.size

    # Convert percentage values to pixel coordinates
    x = int(x_percent / 100 * img_width)
    y = int(y_percent / 100 * img_height)

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Choose a font with the specified size
    font = ImageFont.truetype("Montserrat-Bold.ttf", size=text_size)

    # Add text to the image with the specified color
    draw.text((x, y), text, font=font, fill=text_color)

    # Adjust brightness only for the image, not the text
    enhancer = ImageEnhance.Brightness(img)
    img_brightness_adjusted = enhancer.enhance(1 - brightness_factor)

    # Convert the image to RGB mode before saving
    img_brightness_adjusted = img_brightness_adjusted.convert("RGB")

    # Save the modified image with JPEG format
    img_brightness_adjusted.save(output_path, format="JPEG")

    return img_brightness_adjusted
