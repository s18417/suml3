import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model2.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model


# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="kiedy wyzdrowieje")
	overview = st.container()
	right = st.columns(1)
	prediction = st.container()

	with overview:
		st.title("czy wyzdrowieje?")
		age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
		sibsp_slider = st.slider( "objawy", min_value=0, max_value=5)
		parch_slider = st.slider( "", min_value=0, max_value=5)
		fare_slider = st.slider( "wzrost", min_value=20, max_value=210)

	data = [[age_slider, sibsp_slider, parch_slider, fare_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje w przeciągu tygodnia? {0}".format("Tak" if survival[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga