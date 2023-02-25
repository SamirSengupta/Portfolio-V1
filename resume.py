from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import requests
from io import BytesIO

# get profile picture
profile_pic_url = 'https://media.licdn.com/dms/image/D4D03AQGTuF62saxbiw/profile-displayphoto-shrink_800_800/0/1669709675567?e=1682553600&v=beta&t=OUnLlbCIQWYNygSHkV6ZfsBKmfOu6R8UOHcv3Tbtadg'
response = requests.get(profile_pic_url)
profile_pic = Image.open(BytesIO(response.content))

# resize profile picture
size = (300, 300)
profile_pic = profile_pic.resize(size)

# create circular mask
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)
del draw

# apply mask to profile picture
output = ImageOps.fit(profile_pic, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)

# display profile picture
st.image(output, caption='', width=150, use_column_width=False)

st.write('# Samir Sengupta')


# Add contact information
st.write('**Contact Information:**')
st.write('- Mumbai (Mira Road)')
st.write('- +91-8356075699')
st.write('- Samir843301003@gmail.com')


# Add about section
st.write('## About')
st.write('I am pursuing my bachelor\'s degree in the field of Data Science currently in the final semester. I have experience of real-time projects and have completed a few projects dealing with the EDA and Data Cleaning process and built a few regressions as well as classification-based projects during my academics. I have expertise in data visualization and representation which can provide good insights and sound information about the data.')

# Add education section
st.write('## Education')
col1, col2 = st.columns([1, 4])
with col1:
    st.write('**Bachelor of Science in Data Science,**')
    st.write('KES Shroff College, Mumbai')
    st.write('3 Years (2020-2023)')
with col2:
    st.write('**Higher Secondary School,**')
    st.write('Reena Mehta Jr College, Mumbai')
    st.write('2 Years (2018-2020)')
    st.write('**Secondary School,**')
    st.write('St. Thomas High School, Mumbai')
    st.write('Completed in 2018')

# Add projects section
st.write('## Projects')
st.write('- Built a chatbot with GUI')
st.write('- Twitter Sentimental Analysis')
st.write('- Movie Recommendation System')
st.write('- Alexa Bot')

# Add certifications section
st.write('## Certifications')
st.write('- Advanced Excel')
st.write('- Arduino Programming')
st.write('- Blockchain Technology')
st.write('- Recommender System')

# Add skills section
st.write('## Skills & Abilities')
st.write('### Technical Skills')
st.write('- Programming Languages & Essentials: C++, Python, R Programming, MySQL, Tableau, Power Bi, HTML, CSS And JavaScript, Adv Excel.')
st.write('### Areas of Interest')
st.write('- SQL')
st.write('- Machine Learning')
st.write('- Natural Language Processing')
st.write('- Deep Learning')
st.write('- Software Engineering')
st.write('- Networking')
st.write('- Cloud Computing')
st.write('- Data Analytics')

# Add personal abilities section
st.write('## Personal Abilities')
st.write('- Ability to make sound decisions')
st.write('- Good communication and organizing skills')
st.write('- Ability to make people understand the situation quickly')
st.write('- Pragmatic and effective risk management.')
st.write('- Quick decision maker.')
st.write('- Proficient in both spoken and written English.')
st.write('- Skilled in creative writing.')

# Add language section
st.write('## Languages')
st.write('- English (Fluent)')
st.write('- Hindi (Native)')
st.write('- Bengali (Intermediate)')
st.write('- Gujarati (Intermediate)')

st.write('## Hobbies')
st.write('- Reading')
st.write('- Writing')
st.write('- Music')

# Add social media links section
st.write('## Social Media Links')

# Create columns for each social media link
col1, col2, col3 = st.columns(3)

# Add LinkedIn link
with col1:
    st.markdown('<a href="https://www.linkedin.com/in/samir-sengupta-081493214/" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col2:
    st.markdown('<a href="https://github.com/SamirSengupta" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

# Add Twitter link
with col3:
    st.markdown('<a href="https://twitter.com/Samiir__20" target="_blank" style="text-decoration:none;"><img src="https://png.pngtree.com/png-vector/20221018/ourmid/pngtree-twitter-social-media-round-icon-png-image_6315985.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Twitter</p>', unsafe_allow_html=True)

# Add footer
st.write('---')
st.write('© Samir Sengupta  |  Last updated: February 2023')
