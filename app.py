import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


st.set_page_config(page_title="GEHU NSS BTL", page_icon='nss-logo.png')
st.info("This Site is only for GEHU NSS UNIT for Bhimtal Campus only")

st.image("GEHU-logo 2.png",width=200)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'NSS DEV CELL'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>NSS ID CARD</h1>", unsafe_allow_html=True)
# import PIL module


# Front Image
uploaded_file = st.file_uploader("insert your photo")
if uploaded_file is not None:
    if (uploaded_file):
        filename = Image.open(uploaded_file)
        filenamew = filename.resize((202, 247))
        # filename2.show()
        # Back Image
        filename1 = 'ID_CARD.png'

        # Open Front Image
        frontImage = filenamew
        # Open Background Image
        background = Image.open(filename1)

        # Convert image to RGBA
        frontImage = frontImage.convert("RGBA")

        # Convert image to RGBA
        background = background.convert("RGBA")

        studentid = st.text_input("Enter your Student ID ")
        if (studentid):
            background.paste(frontImage, (50, 180), frontImage)

            # Save this image
            background.save(f"pen", format="png")
            img = Image.open(f'pen')

            # Call draw Method to add 2D graphics in an image
            I1 = ImageDraw.Draw(img)
            name = st.text_input("Enter your First Name ")
            name2 = st.text_input("Enter your Last Name ")
            fullname = f"{name.upper()} {name2.upper()}"
            if (name and name2):
                year = st.selectbox('In Which Year you are ? ',('1', '2', '3'))
                if (year == '1'):
                    nssid = f"{name[0] + name2[0]}FY{studentid}"
                    print(nssid)
                    # print("")
                elif (year == '2'):
                    nssid = f"{name[0] + name2[0]}SY{studentid}"
                elif (year == '3'):
                    nssid = f"{name[0] + name2[0]}TY{studentid}"
                elif (year == '4'):
                    nssid = f"{name[0] + name2[0]}FY{studentid}"
                else:
                    print("Invalid")
                course = st.text_input("Enter your Course Name ")
                session = st.text_input("Enter your session (eg :-2021-2025)")

                phonenumber = st.text_input("Enter your Phone Number ")
                add = st.text_input("Enter your Address(only city and State )")
                blood = st.text_input("Enter you Blood Group ")
                email = st.text_input("Enmter your E-mail address")

                # Custom font style and font size
                myFont = ImageFont.truetype('arialbd.TTF', 28)
                I1.text((266, 185), f"{fullname}", font=myFont, fill=(0, 0, 0))
                I1.text((266, 231), f"{course}", font=myFont, fill=(0, 0, 0))
                myFont = ImageFont.truetype('arial.TTF', 25)
                I1.text((552, 276), f"{nssid}", font=myFont, fill=(0, 0, 0))
                I1.text((552, 328), f"{session}", font=myFont, fill=(0, 0, 0))
                I1.text((552, 380), f"{studentid}", font=myFont, fill=(0, 0, 0))
                I1.text((1264, 40), f"{phonenumber}", font=myFont, fill=(0, 0, 0))
                I1.text((1264, 92), f"{blood}", font=myFont, fill=(0, 0, 0))
                I1.text((1264, 144), f"{email}", font=myFont, fill=(0, 0, 0))
                I1.text((1264, 198), f"{add}, India", font=myFont, fill=(0, 0, 0))
                if(studentid=='210111558' or studentid=='210111660' or studentid=='21042224'):

                    I1.text((1264, 299), "For All Event", font=myFont, fill=(0, 0, 0))
                else:
                    I1.text((1264, 299), "only for 13-02-2023", font=myFont, fill=(0, 0, 0))
                # Display edited image

                # Save the edited image
                img.save(f"{studentid}.png")
                if(fullname and course and nssid and session and studentid and phonenumber and blood and email and add):
                    st.image(f"{studentid}.png", caption='Download Your NSS ID CARD')
                    with open(f"{studentid}.png", "rb") as file:
                        btn = st.download_button(
                            label="Download image",
                            data=file,
                            file_name=f"{studentid}.png",
                            mime="image/png"
                        )
                else:
                    st.error("Fill all the details ...")
            else:
                st.error("Enter you name")
        else:
            st.info("Enter your Student ID")
    else:
        print("joker")


else:
    print("./zebra.jpg")





