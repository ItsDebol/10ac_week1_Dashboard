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
    st.title("TEL CO user analytics")
    selection_type = st.sidebar.selectbox("Select analysis",("-","Customer overview", "User engagement"))
    st.write('')
    st.write(selection_type)
    if(selection_type == "Customer overview" ):
        int_selection_type = st.selectbox("Select what to overview" , ("-","Top 10 handsets used by the customers", 
        "Top 3 handsets manufacturers", "Top 5 handsets per top 3 handsets manufacturer",  
        "distribution functions of applications used "))
        if(int_selection_type == "Top 10 handsets used by the customers"):
            st.image('overview/top handset types.PNG')
        elif(int_selection_type == "Top 3 handsets manufacturers"):
            st.image('overview/top.PNG')
        elif(int_selection_type == "Top 5 handsets per top 3 handsets manufacturer"):
            st.image('overview/top apple.PNG')
            st.image('overview/top samsung.PNG')
            st.image('overview/top huawei.PNG')
        elif(int_selection_type == "distribution functions of applications used "):
            st.write("Apps used by users via TEL CO")
            st.image('overview/social_media.png')
            st.image('overview/email.png')
            st.image('overview/gaming.png')
            st.image('overview/youtube.png')
            st.image('overview/google.png')
            st.image('overview/netflix.png')
            st.image('overview/durms.png')                           
    elif(selection_type == "User engagement"):
        int_selection_type_user = st.selectbox("Select User engagement",("-","top 10 customers with the hight usage of data",
        "session durations ","kmean and decile","Most used applications",))
        if(int_selection_type_user == "top 10 customers with the hight usage of data"):
            st.image('user engagement/top bytes.PNG')
        elif(int_selection_type_user == "session durations "):
            st.image('user engagement/xdr.PNG')
            st.image('user engagement/total duration.PNG')
        elif(int_selection_type_user ==  "kmean and decile"):
            st.image('user engagement/kmmean.PNG')
            st.image('user engagement/decile.PNG')      
        elif(int_selection_type_user == "Most used applications"):
            st.image('user engagement/top 5 apps.PNG')
        

    
# initialization()
main()


    