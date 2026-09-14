from fpdf import FPDF

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add Title Page
pdf.add_page()
pdf.set_font("Arial", size=16, style='B')
pdf.cell(200, 10, "Amazing Inventions That Changed the World", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, "Year 5 Science Project", ln=True, align='C')
pdf.cell(200, 10, "Student Name", ln=True, align='C')
pdf.cell(200, 10, "School Name", ln=True, align='C')
pdf.cell(200, 10, "Date", ln=True, align='C')

# Add Page 2 with Inventions and Impact
pdf.add_page()
pdf.set_font("Arial", size=14, style='B')
pdf.cell(200, 10, "Inventions That Changed the World", ln=True, align='C')

pdf.set_font("Arial", size=12)

inventions = [
    ("The Wheel", "The wheel revolutionized transportation, making it easier to move goods and people."),
    ("The Light Bulb", "Thomas Edison's light bulb transformed the world by making it possible to work and live after dark."),
    ("The Telephone", "Alexander Graham Bell's invention of the telephone allowed people to communicate over long distances."),
    ("The Airplane", "The Wright Brothers’ airplane made global travel faster and more accessible."),
    ("The Internet", "The Internet connected the world, revolutionizing communication, business, and education.")
]

for title, description in inventions:
    pdf.ln(10)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, title, ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, description)

# Add Page 3 with Conclusion
pdf.add_page()
pdf.set_font("Arial", size=14, style='B')
pdf.cell(200, 10, "The Impact of Inventions", ln=True, align='C')

pdf.set_font("Arial", size=12)
conclusion = """
Inventions have had a profound impact on the world. They have made our lives easier, faster, and more connected.
From transportation to communication, these inventions have improved the way we live. And the best part is, new
inventions continue to shape the world in exciting ways!
"""

pdf.multi_cell(0, 10, conclusion)

# Save the PDF
pdf_output_path = "/mnt/data/amazing_inventions_project.pdf"
pdf.output(pdf_output_path)

pdf_output_path