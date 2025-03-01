import streamlit as st


st.title('BMI Calculator')
st.markdown('This app calculate body mass index')
try:
   weight=st.number_input('enter weight in kg',step=0.1,)
   height=st.number_input('enter height in cms',step=0.1)
   height=float(height)
   
   if st.button("calculate bmi"):
        bmi=weight/((height/100)**2)
        st.write("your bmi ",bmi)

        if bmi<18.5:
            st.write("you are under  weight")
        elif bmi>=18.5 and bmi<25:
            st.write("you have normal weight")
        elif bmi>=25 and bmi<30:
            st.write("you are over weight")
        elif bmi>=30:
            st.write("You are obese")

except ZeroDivisionError:
   st.write("something went wrong")

except Exception as e:
   st.write(e)
       

