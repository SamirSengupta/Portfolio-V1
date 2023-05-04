import streamlit as st
from PIL import Image, ImageDraw, ImageOps

# get profile picture
profile_pic = Image.open("Profile.jpg")
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


# Add education section
st.write('## Education')
education_list = [    {'degree': 'BACHELOR OF DATA SCIENCE', 'institution': 'KES Shroff College, Mumbai', 'duration': '3 Years (2020-2023)'},    {'degree': 'HIGHER SECONDARY SCHOOL', 'institution': 'Reena Mehta Jr College, Mumbai', 'duration': '2 Years (2018-2020)'},    {'degree': 'SECONDARY SCHOOL', 'institution': 'St. Thomas High School, Mumbai', 'duration': 'Completed in 2018'}]

# Create a table with the education information
table = "| Degree | Institution | Duration |\n| ------ | ----------- | -------- |\n"
for education in education_list:
    table += f"| {education['degree']} | {education['institution']} | {education['duration']} |\n"

st.write(table, markdown=True)



# Add projects section
st.write('## Projects')
st.write('- Movie Recommendation System')
st.write('- Twitter Sentimental Analysis')

# Add certifications section
st.write('## Certifications')
st.write('- Advanced Excel')
st.write('- Arduino Programming')
st.write('- Blockchain Technology')
st.write('- Machine Learning')
st.write('- PowerBi')

# Add skills section
st.write('## Skills & Abilities')
st.write('- Back-End Development')
st.write('- Data Analytics')
st.write('- Data Visualization')
st.write('- Front-End Development')
st.write('- Machine Learning')
st.write('- Networking')
st.write('- Python')
st.write('- Statistics')

# Add personal abilities section
st.write('## Personal Abilities')
st.write('- Ability to make sound decisions')
st.write('- Good communication and organizing skills')
st.write('- Ability to make people understand the situation quickly')
st.write('- Quick decision maker.')

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
st.write('© Samir Sengupta  |  Last updated: May 2023')
