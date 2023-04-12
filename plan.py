import streamlit as st
import docx
import os
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.set_page_config(page_title= "LESBEPLANNING")
lottie_sd = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ljx86sv6.json")
st.title("HOЁRSKOOL SAUL DAMON")

def create_document(lesson_title, subject, grade, day, lesson_objective, lesson_plan, conclusion, signature):
    document = docx.Document()

    # Set the document styles
    style = document.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = docx.shared.Pt(12)

    # Add the lesson plan header
    document.add_heading('Lesson Plan', level=1)
    document.add_paragraph('Subject: ' + subject)
    document.add_paragraph('Grade: ' + grade)
    document.add_paragraph('Day: ' + day)

    # Add the lesson objectives
    document.add_heading('Lesson Objectives', level=2)
    document.add_paragraph(lesson_objective)

    # Add the lesson plan
    document.add_heading('Lesson Plan', level=2)
    document.add_paragraph(lesson_plan)

    # Add the conclusion and signature
    document.add_heading('Conclusion', level=2)
    document.add_paragraph(conclusion)
    document.add_paragraph('Teacher Signature: ' + signature)

    return document

def main():
    st.title("LESBEPLANNING")

    # Get the input from the user
    lesson_title = st.text_input("Lesson Title")
    subject = st.text_input("Subject Name")
    grade = st.selectbox("Grade", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
    day = st.text_input("Day")
    date = st.text_input("Date")
    lesson_objective = st.text_area("Lesson Objective")
    lesson_plan = st.text_area("Lesson Plan")
    conclusion = st.text_area("Conclusion")
    signature = st.text_input("Teacher Signature")

    # Create the Word document
    if st.button("Save Lesson Plan"):
        filename = lesson_title + ".docx"
        i = 1
        while os.path.exists(filename):
            filename = lesson_title + " (" + str(i) + ")" + ".docx"
            i += 1
        document = create_document(lesson_title, subject, grade, day, lesson_objective, lesson_plan, conclusion, signature)
        document.save(filename)
        st.success(f"Lesson Plan saved as {filename}.")

st_lottie(lottie_sd, height = 350 , key="coding")

if __name__ == "__main__":
    main()
