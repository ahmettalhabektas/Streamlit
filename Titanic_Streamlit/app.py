import os
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
import pickle

# Set the page configuration
st.set_page_config(
    page_title="🚢 Titanic Survival Predictor 🚢",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About':
        """ ## Welcome to the Titanic Survival Predictor! 🌟
        This app uses AI to estimate your chances of survival on the Titanic. Feel free to contact me if you have any questions or feedback:
        - 📧 My email: [atalhabektas@gmail.com](mailto:atalhabektas@gmail.com)
        - 🔗 My LinkedIn: [Ahmet Talha Bektaş](https://www.linkedin.com/in/ahmet-talha-bekta%C5%9F-056844216)
        - 💻 My GitHub: [Ahmet Talha Bektaş](https://github.com/ahmettalhabektas)
        - 👨‍💻 My Kaggle: [Ahmet Talha Bektaş](https://www.kaggle.com/ahmettalhabektas)
        Made with 💖 by [Ahmet Talha Bektaş](https://www.linkedin.com/in/ahmet-talha-bekta%C5%9F-056844216)
        """
    }
)

# Hide a CSS class
st.markdown("""
<style>
css-cio0dv ea3mdgi1
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

try:
    st.write('Trying with back slashes')
    st.dataframe(pd.read_csv(r'.\\data\\titanic.csv'))
except:
    st.write('It didn\'t work with back slashes.')


try:
    st.write('Trying with forward slashes')
    st.dataframe(pd.read_csv(r'/data/titanic.csv'))
except:
    st.write('It didn\'t work with forward slashes.')




# Read the Titanic dataset
CSV_PATH="./titanic.csv"
titanic = pd.read_csv(CSV_PATH)

# Language selection
lang = st.selectbox("🌐 Please select a language", options=( "🇬🇧 English","🇹🇷 Türkçe"))
lang = lang.split(" ")[1]

if lang == "English":
    # English Content
    st.markdown("# Embark on a Titanic Adventure 🚢")
    st.write(
        "Welcome aboard the RMS Titanic, a legendary British passenger liner with a captivating story! Join us as we journey back in time to April 1912, "
        "when this magnificent ship set sail on its maiden voyage, only to meet a chilling fate. Brace yourself for some exciting Titanic trivia:"
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/St%C3%B6wer_Titanic.jpg/800px-St%C3%B6wer_Titanic.jpg", caption="RMS Titanic 📸")

    st.subheader("Get Ready for Some Titanic Trivia ℹ️:")
    st.markdown(
        "- Meet the Titanic, one of three Olympic-class ocean liners operated by the famous White Star Line. 🚢"
    )
    st.markdown(
        "- Picture this: April 14, 1912, a moonlit night, and suddenly, an iceberg! The Titanic's ill-fated encounter sent her plunging into the icy depths of the North Atlantic Ocean on April 15, 1912. ❄️🌊"
    )
    st.markdown(
        "- Hold onto your seats! More than 1,500 brave souls lost their lives in this heart-wrenching disaster, marking it as one of the most tragic peacetime maritime events in history. ☠️"
    )
    st.markdown(
        "- The Titanic was a marvel of its time, equipped with advanced safety features like watertight compartments and lifeboats. But, alas, there weren't enough lifeboats for everyone! 🆘🛶"
    )

    st.write(
        "Join us in exploring the incredible history of the Titanic, where adventure meets tragedy, and learn how you would have fared on this unforgettable voyage!"
    )


    st.markdown("# Titanic Survival Prediction 🧑‍🚀")
    st.write(
        "Welcome to the Titanic Survival Predictor! Let's take a journey into the AI world and predict your fate if you were on the Titanic. Exciting, right? 🚢"
    )

    with st.expander("How Does Our AI Model Work? ✨"):
        st.markdown("# How Does the AI Model Work? 🤖✨")

        st.write(
            "Welcome to the Titanic Survival Prediction! 🚢 These predictions are generated by an Artificial Intelligence model. Our model has an accuracy rate of approximately 80%, and we use the Random Forest classification algorithm to make predictions."
        )

        st.markdown(
            "The Random Forest classification algorithm is a versatile model created by combining numerous decision trees. 🌲🌲🌲 These trees are trained using random data samples and features. The model combines the predictions from these trees to produce results. 🌳🔮"
        )

        st.markdown(
            "The Random Forest algorithm is used to predict the survival of Titanic passengers. The model takes into account passengers' personal information, ticket class, gender, age, and more to make predictions. 🎫👫📆"
        )

        st.markdown(
            "However, please keep in mind that these predictions are merely estimates, and real-life outcomes can be influenced by various factors. While our model has an accuracy rate of approximately 80%, the results are not definitive and are for entertainment purposes only. 🎉🤪"
        )



    st.write(
        "Go ahead and fill out the form, then click the 'Submit' button to see your prediction! 🚀"
    )

    with st.expander("Feeling Adventurous? Fill Out the Form! 🚀",expanded=True):
        st.write(
            "🌟 Ahoy there! Welcome aboard the Titanic adventure! We're setting sail on a journey through time, and you're invited to be a part of it. "
            "Picture yourself as a passenger on the grand RMS Titanic. We'll use our AI magic to predict whether you'd survive this legendary voyage."
        )

        st.write(
            "🕰️ But before we embark on this thrilling quest, let's put on our virtual time-traveler hats and gather some essential information."
        )

        st.write(
            "📝 Fear not, it's not just a regular form; it's your ticket to the Titanic experience! Fill in your details like your name, age, gender, and more, "
            "and we'll do the rest. Will you make it to the lifeboats, or will you brave the icy waters of the North Atlantic? Let's uncover the adventure!"
        )

        st.write(
            "🚢 Keep in mind, this is all for fun and the love of adventure. Our AI model will make a prediction, but the real excitement lies in your imagination. Are you ready to set sail?"
        )

        success_control = False

    
            
        user_name_holder = ""
        user_surname_holder = ""
        pclass_holder = 1
        age_holder = 0
        sib_holder = 0
        sp_holder = 0
        par_holder = 0
        ch_holder = 0
        sex_holder = 0
        fare_holder = 0
        embarked_holder = 0
        deck_letter_holder = 0

 



        col1, col2 = st.columns(2)
        user_name = col1.text_input("Your First Name ✍️", max_chars=50, placeholder="Enter your first name",value=user_name_holder)
        user_surname = col2.text_input("Your Last Name ✍️", max_chars=50, placeholder="Enter your last name",value=user_surname_holder)

        pclass = st.radio("Choose Your Passenger Class 🚢", options=(1, 2, 3),index=pclass_holder-1)

        age = st.slider("Your Age 🎂", min_value=0, max_value=85, value=age_holder)

        sib = st.slider("Number of Siblings Aboard 👨‍👩‍👧‍👦", min_value=0, max_value=5, value=sib_holder)

        sp = st.slider("Number of Spouses Aboard 👩‍❤️‍👨", min_value=0, max_value=5, value=sp_holder)

        sib_sp = sib + sp

        par = st.slider("Number of Parents Aboard 👪", min_value=0, max_value=5, value=par_holder)

        ch = st.slider("Number of Children Aboard 👶", min_value=0, max_value=5, value=ch_holder)

        parch = par + ch

        num_family = parch + sib_sp + 1

        sex = st.selectbox("Your Gender 👩‍🦰👨‍🦱", options=("Female", "Male"), index=sex_holder)

        min_fare = titanic.loc[titanic["Pclass"] == pclass, "Fare"].min()
        max_fare = titanic.loc[titanic["Pclass"] == pclass, "Fare"].max()

        st.write("💰 The range of Fare is calculated based on your Passenger class")

        fare = st.slider(f"💷 Ticket Price in British Pounds (£) between {min_fare} and {max_fare}", min_value=float(min_fare), max_value=float(max_fare), value=float(fare_holder))

        embarked = st.selectbox("Port of Embarkation 🚢", options=("Cherbourg (C)", "Southampton (S)", "Queenstown (Q)"), index=embarked_holder)

        st.write("🚢 The Titanic has decks labeled from A (top) to F (bottom), with 'U' representing unknown decks. The available deck options are calculated based on your chosen passenger class.")

        deck_options = titanic.loc[titanic["Pclass"] == pclass, "Deck_letter"].unique().tolist()
        deck_letter = st.selectbox("Deck Letter 🚢", options=(deck_options), index=deck_letter_holder)

        submit, _, _, _, randomizer = st.columns(5)

        if submit.button("Submit ✅"):
            if age == 0:
                st.warning("Please fill in the required fields ⬆️")
            else:
                st.success("Submitted Successfully! 👍")
                success_control = True


        if success_control:
            # Create a dictionary with scalar values and specify an index
            data = {
                'Pclass': [pclass],
                'Age': [age],
                'SibSp': [sib_sp],
                'Parch': [parch],
                'Fare': [fare],
                'NumFamily': [num_family],
                'Sex_female': [0],
                'Sex_male': [0],
                'Embarked_C': [0],
                'Embarked_Q': [0],
                'Embarked_S': [0],
                'Deck_letter_A': [0],
                'Deck_letter_B': [0],
                'Deck_letter_C': [0],
                'Deck_letter_D': [0],
                'Deck_letter_E': [0],
                'Deck_letter_F': [0],
                'Deck_letter_G': [0],
                'Deck_letter_U': [0],
            }

            # Specify an index for the DataFrame
            index = [0]  # You can adjust the index as needed

            df = pd.DataFrame(data, index=index)

            embarked = embarked[0]
            df[f"Embarked_{embarked}"] = 1

            df[f"Sex_{sex.lower()}"] = 1

            df[f"Deck_letter_{deck_letter}"] = 1

            # Load the model from the pickle file
            with open('model.pkl', 'rb') as file:
                model = pickle.load(file)

            # Make predictions using the loaded model
            predictions = model.predict(df)

            # Specify the directory where your files are located
            alive_directory_path = "alive"
            dead_directory_path = "dead"

            # List all files in the directory
            alive_files = os.listdir(alive_directory_path)

            # Filter files to exclude directories (if any)
            alive_files = [file for file in alive_files if os.path.isfile(os.path.join(alive_directory_path, file))]

            # List all files in the directory
            dead_files = os.listdir(dead_directory_path)

            # Filter files to exclude directories (if any)
            dead_files = [file for file in dead_files if os.path.isfile(os.path.join(dead_directory_path, file))]

            image_place = st.empty()

            if predictions[0] == 0:
                st.write("🌊 Oh no! It seems you didn't make it to a lifeboat. But remember, it's all in good fun!")
                chosen_dead_file = os.path.join(dead_directory_path, random.choice(dead_files))
                image_place.image(chosen_dead_file, width=675)





                
            elif predictions[0] == 1:
                st.write("🎉 Congratulations! You've survived the Titanic adventure! Now, imagine the thrilling stories you'd have to tell!")
                          
                chosen_alive_file = os.path.join(alive_directory_path, random.choice(alive_files))
                image_place.image(chosen_alive_file, width=675)




            else:
                st.warning("A problem occured")



    st.write("I bet you're itching to uncover the secrets hidden in Titanic's data, right? Well, get ready for a thrilling data-driven adventure with some cool graphs!")

    with st.expander("Let's Dive into Data Visualization 📊"):
        st.write(
            "Hold onto your life jackets because we're about to embark on a thrilling adventure through Titanic's data!"
        )

        st.markdown(
            "🎉 **Discover the Titanic's Secrets**: Imagine being Sherlock Holmes on the Titanic! We'll uncover how passenger class, gender, and age played roles in who survived. Get ready to unveil the mysteries!"
        )

        st.markdown(
            "🚀 **Blast Off with Graphs**: Our secret weapon? Powerful graphs! They're like magic windows into the Titanic's history. Buckle up for a rocket ride!"
        )

        st.markdown(
            "💡 **Get Insights**: These visualizations will provide insights that even Jack and Rose from the movie would find fascinating. Are you ready for this data-driven adventure? The Titanic's secrets await!"
        )

        st.write("Hit that 'Create Graphs' button below, and let's set sail!")

        bins = list(range(0, 81, 5))  # Creates bins from 0 to 80 with a step of 5

        # Use pd.cut to categorize the data into the specified bins
        titanic['Age Range'] = pd.cut(titanic['Age'], bins=bins, right=True)

        bins = list(range(0, 300, 20))  # Creates bins from 0 to 80 with a step of 5

        # Use pd.cut to categorize the data into the specified bins
        titanic['Fare Range'] = pd.cut(titanic['Fare'], bins=bins, right=True)

        st.write("If you're curious about the real statistics of the Titanic dataset, let's dive in together.")

        user_hue = st.selectbox("What should we use for color encoding?", options=("None", "Survived", "Passenger Class", "Sex", "Age Range", "Siblings & Spouses", "Parents & Children", "Fare Range", "Port of Embarkation", "Deck Letter"))
        user_x = st.selectbox("Choose a value for the x-axis", options=("Survived", "Passenger Class", "Sex", "Siblings & Spouses", "Parents & Children", "Port of Embarkation", "Deck Letter"))

        if user_hue == "None":
            user_hue = None
        titanic.Survived = titanic.Survived.replace([1, 0], ["Survived 😊", "Not Survived 😥"])
        titanic = titanic.rename(columns={"Pclass": "Passenger Class", "SibSp": "Siblings & Spouses", "Parch": "Parents & Children", "Embarked": "Port of Embarkation","Deck_letter":"Deck Letter"})
        fig = plt.figure()
        plot_df = titanic.copy()
        sns.countplot(data=plot_df, x=user_x, hue=user_hue)
        if st.button("Create Graph"):
            st.pyplot(fig)


else:
    # Turkish Content
    st.markdown("# Titanik Macerasına Hoş Geldiniz 🚢")
    st.write(
        "Legandary British yolcu gemisi RMS Titanic'e hoş geldiniz! Bu büyüleyici geminin ilginç hikayesine yolculuk ediyoruz. Bize katılın ve bu muhteşem geminin ilk seferine, Nisan 1912'ye geri dönelim, "
        "Ancak maalesef korkunç bir kaderle karşılaşan bu seyahati yaparken heyecan verici Titanik bilgileriyle hazırlıklı olun:"
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/St%C3%B6wer_Titanic.jpg/800px-St%C3%B6wer_Titanic.jpg", caption="RMS Titanic 📸")

    st.subheader("Titanik Bilgileri İçin Hazır Olun ℹ️:")
    st.markdown(
        "- Ünlü White Star Line tarafından işletilen üç Olympic sınıfı okyanus gemisinden biri olan Titanik'i tanıyın. 🚢"
    )
    st.markdown(
        "- Şöyle düşünün: 14 Nisan 1912, aydınlık bir gece ve birdenbire bir buzdağı! Titanik'in talihsiz karşılaşması, onu 15 Nisan 1912'de Kuzey Atlantik Okyanusu'nun buz gibi sularına gönderdi. ❄️🌊"
    )
    st.markdown(
        "- Koltuklarınıza sıkıca tutun! Bu yürek burkan felakette 1.500'den fazla cesur insan hayatını kaybetti ve bu, tarih boyunca kaydedilmiş en trajik barış zamanı deniz olaylarından biri olarak kabul ediliyor. ☠️"
    )
    st.markdown(
        "- Titanik, döneminin bir harikasıydı ve su geçirmez bölmeler ve cankurtaran botlar gibi gelişmiş güvenlik özelliklerine sahipti. Ama ne yazık ki, herkes için yeterli cankurtaran bot yoktu! 🆘🛶"
    )

    st.write(
        "Titanik'in inanılmaz tarihini keşfetmek için bize katılın, macera ve trajedinin buluştuğu bu unutulmaz yolculukta nasıl bir performans sergilediğinizi öğrenin!"
    )

    # Turkish Content
    st.markdown("# Titanic Hayatta Kalma Tahmini 🧑‍🚀")
    st.write(
        "Titanik Hayatta Kalma Tahminine hoş geldiniz! AI dünyasına bir yolculuk yapalım ve Titanik'te olsaydınız kaderinizi tahmin edelim. Heyecanlı değil mi? 🚢"
    )

    with st.expander("Yapay Zeka modelimiz nasıl çalışıyor? ✨"):
        st.markdown("# Yapay Zeka Modeli Nasıl Çalışıyor? 🤖✨")

        st.write(
            "Titanik Hayatta Kalma Tahminine hoş geldiniz! 🚢 Bu tahminler, bir Yapay Zeka modeli tarafından üretilmektedir. Modelimizin doğruluk oranı yaklaşık %80'dir ve sonuçları tahmin etmek için Random Forest sınıflandırma algoritması kullanıyoruz."
        )

        st.markdown(
            "Random Forest sınıflandırma algoritması, çok sayıda karar ağacının bir araya getirilmesiyle oluşturulan bir ansiklopedik modeldir. 🌲🌲🌲 Bu ağaçlar, rastgele veri örnekleri ve özellikler kullanılarak eğitilir. Model, bu ağaçların tahminlerini bir araya getirerek sonuçları üretir. 🌳🔮"
        )

        st.markdown(
            "Random Forest algoritması, Titanik yolcularının hayatta kalma tahminlerini yapmak için kullanılıyor. Model, yolcuların kişisel bilgileri, bilet sınıfı, cinsiyet, yaş, ve daha fazlasını dikkate alarak tahminlerde bulunur. 🎫👫📆"
        )

        st.markdown(
            "Ancak unutmayın ki bu tahminler sadece bir öngörüdür ve gerçek hayatta çok sayıda faktör etkileyebilir. Modelimizin doğruluk oranı %80 olsa da, sonuçlar kesin değildir ve yalnızca eğlence amaçlıdır. 🎉🤪"
        )


    # Turkish Content
    st.write(
        "Formu doldurun ve tahmininizi görmek için 'Gönder' düğmesine tıklayın! 🚀"
    )

    with st.expander("Macera Dolu Musunuz? Formu Doldurun! 🚀",expanded=True):
        st.write(
            "🌟 Ahoy oraya! Titanik macerasına hoş geldiniz! Zaman yolculuğuna çıkıyoruz ve siz de bu yolculuğun bir parçası olmaya davetlisiniz. "
            "Kendinizi büyük RMS Titanic'in bir yolcusu olarak hayal edin. AI sihirlerimizi kullanarak bu efsanevi yolculukta hayatta kalıp kalmayacağınızı tahmin edeceğiz."
        )

        st.write(
            "🕰️ Ancak bu heyecanlı maceraya başlamadan önce sanal zaman yolcusu şapkalarımızı takalım ve bazı temel bilgileri toplayalım."
        )

        st.write(
            "📝 Endişelenmeyin, bu sıradan bir form değil; bu, Titanik deneyiminiz için bir bilet! İsminiz, yaşınız, cinsiyetiniz ve daha fazlası gibi detayları doldurun, "
            "gerisini biz hallederiz. Can yeleklerine mi ulaşacaksınız, yoksa Kuzey Atlantik'in buzlu sularına cesurca mı meydan okuyacaksınız? Macerayı keşfetmeye hazır mısınız!"
        )

        st.write(
            "🚢 Unutmayın, bu tamamen eğlence ve macera aşkı içindir. AI modelimiz bir tahmin yapacak, ancak gerçek heyecan hayal gücünüzde yatıyor. Hazır mısınız denize açılmaya?"
        )



        user_name_holder = ""
        user_surname_holder = ""
        pclass_holder = 1
        age_holder = 0
        sib_holder = 0
        sp_holder = 0
        par_holder = 0
        ch_holder = 0
        sex_holder = 0
        fare_holder = 0
        embarked_holder = 0
        deck_letter_holder = 0


        success_control = False
        col1, col2 = st.columns(2)
        user_name = col1.text_input("Adınızı Girin ✍️", max_chars=50, placeholder="Adınızı girin",value=user_name_holder)
        user_surname = col2.text_input("Soyadınızı Girin ✍️", max_chars=50, placeholder="Soyadınızı girin",value=user_surname_holder)

        pclass = st.radio("Yolcu Sınıfınızı Seçin 🚢", options=(1, 2, 3), index=pclass_holder-1)

        age = st.slider("Yaşınızı Girin 🎂", min_value=0, max_value=85, value=age_holder)

        sib = st.slider("Gemideki Kardeşler Sayısı 👨‍👩‍👧‍👦", min_value=0, max_value=5, value=sib_holder)
        sp = st.slider("Gemideki Eşler Sayısı 👩‍❤️‍👨", min_value=0, max_value=5, value=sp_holder)

        sib_sp = sib + sp

        par = st.slider("Gemideki Ebeveynler Sayısı 👪", min_value=0, max_value=5, value=par_holder)
        ch = st.slider("Gemideki Çocuklar Sayısı 👶", min_value=0, max_value=5, value=ch_holder)

        parch = par + ch

        num_family = parch + sib_sp + 1

        sex = st.selectbox("Cinsiyetiniz 👩‍🦰👨‍🦱", options=("Kadın", "Erkek"), index=sex_holder)

        min_fare = titanic.loc[titanic["Pclass"] == pclass, "Fare"].min()
        max_fare = titanic.loc[titanic["Pclass"] == pclass, "Fare"].max()

        st.write("💰 Bilet fiyatı aralığı, Yolcu Sınıfınıza göre hesaplanır")

        fare = st.slider(f"💷 İngiliz Sterlini (£) cinsinden Bilet Fiyatı, {min_fare} ile {max_fare} arasında", min_value=min_fare, max_value=max_fare, value=float(fare_holder))

        embarked = st.selectbox("Biniş Limanı 🚢", options=("Cherbourg (C)", "Southampton (S)", "Queenstown (Q)"), index=embarked_holder)

        st.write("🚢 Titanik, A (en üst) ile F (en alt) arasında numaralandırılmış güvertelere sahipti ve 'U'  güverteleri bilinmeyen yolcuları temsil eder. Kullanılabilir güverte seçenekleri, seçtiğiniz yolcu sınıfına göre hesaplanır.")

        deck_options = titanic.loc[titanic["Pclass"] == pclass, "Deck_letter"].unique().tolist()
        deck_letter = st.selectbox("Güverte Harfi 🚢", options=(deck_options), index=deck_letter_holder)

        submit, _, _, _, randomizer = st.columns(5)

        if submit.button("Gönder ✅"):
            if age == 0:
                st.warning("Lütfen gerekli alanları doldurun ⬆️")
            else:
                st.success("Başarıyla Gönderildi! 👍")
                success_control = True

        if success_control:
            # Bir dizi skaler değeri içeren bir sözlük oluşturun ve bir indeks belirtin
            veri = {
                'Pclass': [pclass],
                'Age': [age],
                'SibSp': [sib_sp],
                'Parch': [parch],
                'Fare': [fare],
                'NumFamily': [num_family],
                'Sex_female': [0],
                'Sex_male': [0],
                'Embarked_C': [0],
                'Embarked_Q': [0],
                'Embarked_S': [0],
                'Deck_letter_A': [0],
                'Deck_letter_B': [0],
                'Deck_letter_C': [0],
                'Deck_letter_D': [0],
                'Deck_letter_E': [0],
                'Deck_letter_F': [0],
                'Deck_letter_G': [0],
                'Deck_letter_U': [0],
            }

            # DataFrame için bir indeksi belirtin
            indeks = [0]  # İstenirse indeksi ayarlayabilirsiniz

            df = pd.DataFrame(veri, index=indeks)

            embarked = embarked[0]
            df[f"Embarked_{embarked}"] = 1

            sex=sex.replace("Erkek","Male")
            sex=sex.replace("Kadın","Female")
            
            df[f"Sex_{sex.lower()}"] = 1

            df[f"Deck_letter_{deck_letter}"] = 1

            # Load the model from the pickle file
            with open('model.pkl', 'rb') as file:
                model = pickle.load(file)
            # Yüklenmiş modeli kullanarak tahminler yapın
            tahminler = model.predict(df)

            image_place = st.empty()



            # Specify the directory where your files are located
            alive_directory_path = "alive"
            dead_directory_path = "dead"

            # List all files in the directory
            alive_files = os.listdir(alive_directory_path)

            # Filter files to exclude directories (if any)
            alive_files = [file for file in alive_files if os.path.isfile(os.path.join(alive_directory_path, file))]

            # List all files in the directory
            dead_files = os.listdir(dead_directory_path)

            # Filter files to exclude directories (if any)
            dead_files = [file for file in dead_files if os.path.isfile(os.path.join(dead_directory_path, file))]


            if tahminler[0] == 0:
                st.write("🌊 Maalesef! Görünüşe göre cankurtaran botuna yetişemediniz. Ancak unutmayın, hepsi eğlence amaçlı!")
                chosen_dead_file = os.path.join(dead_directory_path, random.choice(dead_files))
                image_place.image(chosen_dead_file, width=675)
            else:
                st.write("🎉 Tebrikler! Titanik macerasını sağ salim atlattınız! Şimdi, anlatacak heyecan verici hikayeler hayal edin!")                
                chosen_alive_file = os.path.join(alive_directory_path, random.choice(alive_files))
                image_place.image(chosen_alive_file, width=675)


    st.write("Tahmin ediyorum ki Titanic verilerinde gizlenen sırları açığa çıkarmak için sabırsızlanıyorsunuz, öyle değil mi? İşte harika grafiklerle dolu heyecan verici bir veri yolculuğuna hazırlanın!")

    with st.expander("Veri Görselleştirmeye Hazır Mısınız? 📊"):
        st.write(
            "Can yeleklerinizi sıkıca tutun, çünkü Titanic'in verileriyle heyecan dolu bir yolculuğa çıkmak üzereyiz!"
        )

        st.markdown(
            "🎉 **Titanik'in Sırlarını Keşfet**: Titanic'te Sherlock Holmes gibi hissedin! Yolcu sınıfı, cinsiyet ve yaşın kimin hayatta kalacağına nasıl etki ettiğini keşfedeceğiz. Gizemleri açığa çıkarmak için hazır olun!"
        )

        st.markdown(
            "🚀 **Grafiklerle Patlama Yapın**: Gizli silahımız? Güçlü grafikler! Onlar, Titanic'in tarihine sihirli pencereler gibidir. Koltuklarınızı sıkıca bağlayın, çünkü bir roket yolculuğuna çıkıyoruz!"
        )

        st.markdown(
            "💡 **Görüşler Elde Edin**: Bu görselleştirmeler, Titanic'in tarihini bile ilginç bulacak Jack ve Rose gibi insanlara bile ilginç gelecek bilgiler sağlayacak. Bu veri yolculuğuna hazır mısınız? Titanic'in sırları sizi bekliyor!"
        )

        st.write("'Grafik Oluştur' düğmesine tıklayın ve yolculuğa başlayalım!")

        bins = list(range(0, 81, 5))  # 0 ile 80 arasında 5 birimlik aralıklarla bölmeler oluşturur

        # pd.cut kullanarak veriyi belirtilen bölmelere kategorize eder
        titanic['Yaş Aralığı'] = pd.cut(titanic['Age'], bins=bins, right=True)

        bins = list(range(0, 300, 20))  # 0 ile 300 arasında 20 birimlik aralıklarla bölmeler oluşturur

        # pd.cut kullanarak veriyi belirtilen bölmelere kategorize eder
        titanic['Bilet Fiyatı Aralığı'] = pd.cut(titanic['Fare'], bins=bins, right=True)

        st.write("Eğer Titanik veri kümesinin gerçek istatistikleri sizi meraklandırıyorsa, birlikte dalalım.")

        user_hue = st.selectbox("Renk kodlaması için ne kullanmalıyız?", options=("Yok", "Kurtulanlar", "Yolcu Sınıfı", "Cinsiyet", "Yaş Aralığı", "Kardeşler & Eşler", "Anne & Babalar", "Bilet Fiyatı Aralığı", "Biniş Limanı", "Gemi Katı Harfi"))
        user_x = st.selectbox("X ekseni için bir değer seçin", options=("Kurtulanlar", "Yolcu Sınıfı", "Cinsiyet", "Kardeşler & Eşler", "Ebeveynler & Çocuklar", "Biniş Limanı", "Gemi Katı Harfi"))

        if user_hue == "Yok":
            user_hue = None

        titanic.Survived = titanic.Survived.replace([1, 0], ["Kurtulanlar 😊", "Kurtulamayanlar 😥"])
        titanic.Sex = titanic.Sex.replace(["male","female"], ["Erkek", "Kadın"])

        titanic = titanic.rename(columns={"Survived":"Kurtulanlar","Pclass": "Yolcu Sınıfı", "SibSp": "Kardeşler & Eşler", "Parch": "Ebeveynler & Çocuklar", "Embarked": "Biniş Limanı","Deck_letter":"Gemi Katı Harfi","Sex":"Cinsiyet"})
        fig = plt.figure()
        plot_df = titanic.copy()
        sns.countplot(data=plot_df, x=user_x, hue=user_hue)
        if st.button("Grafik Oluştur"):
            st.pyplot(fig)



