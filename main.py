import streamlit as st
# import turtle

# def initialization():
#     skk = turtle.Turtle()
    # turtle.bgcolor('black')
    # turtle.color('cyan')
    # turtle.speed(11)
    # turtle.right(45)
    # for i in range(150):
    #     turtle.circle(30)
    #     if 7 < i < 62:
    #         turtle.left(5)
    #     if 80 < i < 133:
    #         turtle.right(5)
    #     if i < 80:
    #         turtle.forward(10)
    #     else:
    #         turtle.forward(5)

def main():
    st.title("Users analytics in the Telecommunication Industry")
    selection_type = st.sidebar.selectbox("Select analysis",("-","Customer overview", "User engagement","Experiance analysis","Satisfaction analysis"))
    st.write('')
    st.write(selection_type)
    if(selection_type == "Customer overview" ):
        int_selection_type = st.selectbox("Select what to overview" , ("-","Top 10 handsets used by the customers", "Top 3 handsets manufacturers", "Top 5 handsets per top 3 handsets manufacturer", "Univariant analysis", "Bivariant analysis against the total data"))
        if(int_selection_type == "Top 10 handsets used by the customers"):
            st.image('images/1.PNG')
        elif(int_selection_type == "Top 3 handsets manufacturers"):
            st.image('images/2.PNG')
        elif(int_selection_type == "Top 5 handsets per top 3 handsets manufacturer"):
            st.image('images/3.PNG')
        elif(int_selection_type == "Univariant analysis"):
            st.write("Histogram plot of Duration")
            st.image('images/Duration ms.png')
            st.write("Histogram plot of Email")
            st.image('images/email.png')
            st.write("Histogram plot of Game")
            st.image('images/game.png')
            st.write("Histogram plot of Youtube")
            st.image('images/youtube.png')      
        elif(int_selection_type == "Bivariant analysis against the total data"):
            st.write('Between the application and the total data')
            st.image('images/bivariant.PNG')
            st.write('Between each applications')
            st.image("images/among each other.png")

    elif(selection_type == "User engagement"):
        int_selection_type_user = st.selectbox("Select User engagement",("-","Variables and datatypes","Comparision of customers by session frequency","Comparision of customers by total duration","Comparision of customers by total data","Most used applications",))
        if(int_selection_type_user == "Variables and datatypes"):
            st.image('images/data_type1.PNG')
            st.image('images/data_type2.PNG')
        elif(int_selection_type_user == "Comparision of customers by session frequency"):
            st.image('images/customersSession.PNG')
        elif(int_selection_type_user ==  "Comparision of customers by total duration"):
            st.image('images/customersTotalduration.PNG')
        elif(int_selection_type_user == "Comparision of customers by total data"):
            st.image('images/customersData.PNG')
        elif(int_selection_type_user == "Most used applications"):
            st.image('images/top users.PNG')

    elif(selection_type == "Experiance analysis"):
        st.image('images/totaltcprtn.PNG')

    elif(selection_type == "Satisfaction analysis"):
        st.write("""
        # Sorry Nothing to display
        Under analysis... 
        """)
# initialization()
main()


    