import streamlit as st


def get_grade(mark: int) -> str:
    """Return the letter grade for a mark out of 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


if "students" not in st.session_state:
    st.session_state.students = []


st.set_page_config(page_title="Student Grade Manager", page_icon="📚")
st.title("Student Grade Manager")
st.write("Add student marks and review the class performance.")

with st.form("add_student_form", clear_on_submit=True):
    st.subheader("Add a student")
    student_name = st.text_input("Student name")
    marks = st.number_input("Marks", min_value=0, max_value=100, value=0, step=1)
    submitted = st.form_submit_button("Add student")

if submitted:
    name = student_name.strip()
    if not name:
        st.error("Please enter a student name.")
    else:
        mark = int(marks)
        st.session_state.students.append(
            {"Student": name, "Marks": mark, "Grade": get_grade(mark)}
        )
        st.success(f"Added {name}.")

st.subheader("Student list")
if st.session_state.students:
    st.dataframe(st.session_state.students, use_container_width=True, hide_index=True)

    all_marks = [student["Marks"] for student in st.session_state.students]
    st.subheader("Class metrics")
    highest, lowest, average = st.columns(3)
    highest.metric("Highest mark", max(all_marks))
    lowest.metric("Lowest mark", min(all_marks))
    average.metric("Class average", f"{sum(all_marks) / len(all_marks):.2f}")
else:
    st.info("No students have been added yet.")
