import streamlit as st
import os
import io
import docx

# Set page title and icon
st.set_page_config(page_title="Lesson Plan Creator", page_icon=":books:")

# Create input fields
st.title("HOЁRSKOOL SAUL DAMON")
<<<<<<< HEAD
st.subheader("LESBEPLANNER")
st.write("Vul asseblief die volgende velde in om 'n nuwe lesplan te skep:")
st.write("")
subject = st.text_input("Subject")
lesson_title = st.text_input("Lesson Title")
grade = st.selectbox("Grade", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
lesson_date = st.date_input("Lesson Date")
lesson_objective = st.text_area("Lesson Objective")
lesson_activities = st.text_area("Lesson Activities")
materials_needed = st.text_area("Materials Needed")
homework = st.text_area("Homework")
notes = st.text_area("Notes")
teacher_name = st.text_input("Teacher Name")
teacher_surname = st.text_input("Teacher Surname")
st.write("")
st.write("Created by Mr. A.R Visagie @ Saul Damon High School")

# Create save button
if st.button("Create Lesson Plan"):
    # Create a new Word document
    document = docx.Document()
    # Add input values to the document
    document.add_heading(subject.upper(), level=0)
    document.add_paragraph("")
    document.add_paragraph("Lesson Title: " + lesson_title)
    document.add_paragraph("Grade: " + grade)
    document.add_paragraph("Lesson Date: " + str(lesson_date))
    document.add_paragraph("")
    document.add_heading("Lesson Objective", level=1)
=======
st.header("LESBEPLANNER")
# Define the grade levels
grade_levels = ['GRAAD 9', 'GRAAD 10', 'GRAAD 11', 'GRAAD 12']

# Set up the sidebar
st.sidebar.title("DAAGLIKE BEPLANNER")
selected_grade = st.sidebar.selectbox("KIES N GRAAD", grade_levels)

# Define the lesson plan inputs
subject_name = st.text_input("VAK")
lesson_title = st.text_input("LES TITEL")
lesson_date = st.date_input("LES DATUM")
lesson_objective = st.text_input("LES DOELWIT")
lesson_activities = st.text_area("LEERDER AKTIWITEITE")
lesson_materials = st.text_area("MATERIAAL BENODIG")
lesson_homework = st.text_area("HUISWERK")
lesson_notes = st.text_area("NOTAS")

st.write("Designed by Mr. A.R Visagie @ Saul Damon High School")
# Set up the save button
if st.button("Save"):
    # Check if the file already exists
    file_path = os.path.expanduser(f"~/Desktop/{lesson_title}.docx")
    while os.path.exists(file_path):
        st.warning(f"A file with the name '{lesson_title}.docx' already exists on your desktop. Please choose a different name.")
        lesson_title = st.text_input("Lesson Title")
        file_path = os.path.expanduser(f"~/Desktop/{lesson_title}.docx")
        
    # Add the lesson plan to the document
    p = document.add_paragraph(selected_grade, style='Heading 1')
    p = document.add_paragraph()
    p.add_run(f"Subject: ").bold = True
    p.add_run(f"{subject_name}").bold = True
    p = document.add_paragraph(lesson_title, style='Heading 1')
    
    # Add the lesson date
    date_str = lesson_date.strftime('%A, %B %d, %Y')
    document.add_paragraph(date_str, style='Heading 2')
    
    # Add the lesson objective, activities, materials, and homework
    document.add_heading("Objective", level=2)
>>>>>>> a594bd09b9a9a4275a9a4ef2152a34007de208e9
    document.add_paragraph(lesson_objective)
    document.add_heading("Lesson Activities", level=1)
    document.add_paragraph(lesson_activities)
    document.add_heading("Materials Needed", level=1)
    document.add_paragraph(materials_needed)
    document.add_heading("Homework", level=1)
    document.add_paragraph(homework)
    document.add_heading("Notes", level=1)
    document.add_paragraph(notes)
    document.add_paragraph("")
    document.add_paragraph("Teacher Name: " + teacher_name)
    document.add_paragraph("Teacher Surname: " + teacher_surname)
    document.add_paragraph("Teacher Signature: ")

    # Save document to BytesIO object
    with io.BytesIO() as output:
        document.save(output)
        output.seek(0)
        # Create download button
        st.download_button(
            label="Download Lesson Plan",
            data=output,
            file_name="lesson_plan.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        st.success("Your lesson plan has been created. Click the download button to save the file.")
