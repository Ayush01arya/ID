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
        rt = ['210111558','220112205','22011238','21912061', '210111965', '210121548', '22042547', '22041240', '22031218', '22011461', '21011412',
              '22041700', '22011540', '220421444',
              '220112002', '21032521', '220122649', '22151289', '220111918', '220113220', '220112917', '210111825',
              '22041609', '22032998', '220112002',
              '22032554', '21012214', '210111457', '22012365', '21042160', '22041950', '22041226', '21042084',
              '220421290', '210121694', '22011777', '21581104',
              '22011558', '220111056', '220112077', '220122477', '22581216', '220111968', '220121041', '220411555',
              '220221217',
              '22041049', '21031021', '220111267', '220112325', '210111264', '220111964', '22041926', '220112301',
              '220112242', '22382339', '22022028',
              '22041926', '21581117', '21581112', '22012642', '220112965', '20141209', '220122662', '22012117',
              '210111598', '220122267', '220122474',
              '210111660', '21011397', '21042694', '220121785', '220122561', '22012914', '22031728', '21042224',
              '22012715', '22011737', '22042354',
              '22012863', '220112213', '21042013', '21582153', '21011121', '21031407', '22042472', '22031248',
              '21071014', '21011825', '22041116', '210121548', '22382321',
              '22031742', '220111373', '22382357', '22031555', '220122513', '220311008', '220123244', '220112441',
              '21911001', '220112867', '22012425', '21012985',
              '220122589', '220112238', '226121775', '22041935', '220122589', '220421767', '210121663', '220112489',
              '220421151', '220121707', '21011179', '21472094',
              '220111417', '220411160', '220411477', '220421303', '220121701', '21582047', '220122848', '21042151',
              '22031732', '220121207', '210121141', '21472147',
              '21582190', '220112605', '21011044', '22041169', '21041263', '22011853', '21042340', '21581076',
              '22032818', '220122804','21072014','21472159',
              '21151046', '20472169', '21912049', '22031939', '22041134', '21582109', '22042286', '22011701',
              '220112639', '220411094', '22041893',
              '22011290', '22011975', '22012614', '220112655', '210121901', '220121054', '210111048', '220113098',
              '22381133', '220112522', '220112748',
              '22011543', '22012686', '22014925', '220111040', '220411557', '22012814', '21041375', '21582082',
              '21472101', '22042015', '21581191', '22012904',
              '220122300', '21032039', '210121108', '21382279', '21582103', '21042136', '220111633', '21712145',
              '220123223', '220121018', '21011045', '220111512',
              '22962011', '220112597', '210111706', '210111706', '21032532', '21012681', '21011470', '220121779',
              '210111538', '21011834', '220411799', '21011848', '21012237',
              '21032233', '22012275', '220411280', '210111335', '220111976', '22012615', '21011994', '21032040',
              '21912044', '220121920', '21012925', '220111021', '220121614',
              '22041169', '21031320', '21011045', '22012567', '20472181', '22012450', '220112669', '220411755',
              '21472116', '220411249', '22011288''220121920',
              '220122151', '220113238', '21471010', '22382152', '220122167', '220112321', '21012837', '220122380',
              '22041786', '22041110', '22041818', '220421291',
              '21041420', '22011428', '220122775', '220122079', '220111031', '220112040', '220112035', '210121622',
              '220112867', '22032974', '21032087', '220121858']
        studentid = st.text_input("Enter your Student ID ")
        if(studentid in rt):
            st.success("Valid NSS Volunteer Kindly ! Fill all the Details ")
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
                    year = st.selectbox('In Which Year you are ? ', ('1', '2', '3'))
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
                    email = st.text_input("Enter your E-mail address")

                    # Custom font style and font size
                    myFont = ImageFont.truetype('arialbd.TTF', 28)
                    I1.text((266, 185), f"{fullname}", font=myFont, fill=(0, 0, 0))
                    I1.text((266, 231), f"{course}", font=myFont, fill=(0, 0, 0))
                    myFont22 = ImageFont.truetype('Rhuma.ttf', 27)
                    I1.text((552, 276), f"{nssid}", font=myFont22, fill=(0, 0, 0))
                    myFont = ImageFont.truetype('arial.TTF', 25)
                    I1.text((552, 328), f"{session}", font=myFont, fill=(0, 0, 0))
                    I1.text((552, 380), f"{studentid}", font=myFont, fill=(0, 0, 0))
                    I1.text((1264, 40), f"{phonenumber}", font=myFont, fill=(0, 0, 0))
                    I1.text((1264, 92), f"{blood}", font=myFont, fill=(0, 0, 0))
                    I1.text((1264, 144), f"{email}", font=myFont, fill=(0, 0, 0))
                    I1.text((1264, 198), f"{add}, India", font=myFont, fill=(0, 0, 0))
                    if (studentid == '210111558' or studentid == '210111660' or studentid == '21042224'):
                        myFont2 = ImageFont.truetype('Indian.otf', 25)
                        I1.text((1264, 299), "For All Event", font=myFont2, fill=(255, 0, 0))
                    else:
                        I1.text((1264, 299), "I#N#V#A#L#I#D", font=myFont, fill=(0, 0, 0))
                    # Display edited image

                    # Save the edited image
                    img.save(f"{studentid}.png")
                    if (
                            fullname and course and nssid and session and studentid and phonenumber and blood and email and add):
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
                st.error("Enter your Student ID")
        else:
            st.info("Enter your correct student ID !")
        #print(studentid)

    else:
        print("joker")


else:
    print("./zebra.jpg")





