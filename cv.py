from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Curriculum Vitae', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

if __name__ == '__main__':
    # Example data
    name = "John Doe"
    email = "john.doe@example.com"
    phone = "+1234567890"
    
    education = [
        {'degree': 'Bachelor of Science', 'major': 'Computer Science', 'university': 'XYZ University', 'year': '2020'},
        # Add more education entries as needed
    ]

    experience = [
        {'position': 'Software Engineer', 'company': 'ABC Corp', 'start_date': '2020', 'end_date': '2022', 'description': 'Worked on various projects'},
        # Add more experience entries as needed
    ]

    skills = ['Python', 'Java', 'Web Development', 'Problem Solving']

    pdf = PDF()
    pdf.add_page()

    # Personal Information
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, name, 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Email: {email}", 0, 1, 'L')
    pdf.cell(0, 10, f"Phone: {phone}", 0, 1, 'L')
    pdf.ln(10)

    # Education
    pdf.chapter_title('Education')
    for edu in education:
        pdf.cell(0, 10, f"{edu['degree']} in {edu['major']}", ln=True)
        pdf.cell(0, 10, f"{edu['university']}, {edu['year']}", ln=True)
    pdf.ln(10)

    # Experience
    pdf.chapter_title('Experience')
    for exp in experience:
        pdf.cell(0, 10, f"{exp['position']}, {exp['company']}", ln=True)
        pdf.cell(0, 10, f"{exp['start_date']} - {exp['end_date']}", ln=True)
        pdf.multi_cell(0, 10, exp['description'])
    pdf.ln(10)

    # Skills
    pdf.chapter_title('Skills')
    pdf.cell(0, 10, ', '.join(skills), ln=True)

    # Save the document
    pdf.output("my_cv.pdf")
