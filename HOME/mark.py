from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ----------- INPUT SECTION -----------
name = input("Enter Student Name: ")

subjects = ["English", "Hindi", "Math", "Science", "Sst", "Computer"]
marks = {}

for sub in subjects:
    marks[sub] = float(input(f"Enter marks for {sub}: "))

# ----------- PROCESSING -----------
# Sort subjects by marks (descending)
sorted_marks = sorted(marks.items(), key=lambda x: x[1], reverse=True)

# Take top 5 subjects
top5 = sorted_marks[:5]

# Calculate total and percentage
total = sum([m[1] for m in top5])
percentage = total / 5

# ----------- DISPLAY RESULT -----------
print("\n----- RESULT -----")
print(f"Student Name: {name}")
print("\nTop 5 Subjects:")

for sub, mark in top5:
    print(f"{sub}: {mark}")

print(f"\nTotal (Top 5): {total}")
print(f"Percentage: {percentage:.2f}%")

# ----------- PDF GENERATION -----------
doc = SimpleDocTemplate("Marksheet.pdf")
styles = getSampleStyleSheet()

content = []

# Title
content.append(Paragraph("CBSE Class 10 Marksheet (2026)", styles['Title']))
content.append(Spacer(1, 10))

# Student Name
content.append(Paragraph(f"Student Name: {name}", styles['Normal']))
content.append(Spacer(1, 10))

# Table Data
table_data = [["Subject", "Marks"]]

for sub, mark in marks.items():
    table_data.append([sub, mark])

# Add top 5 total and percentage
table_data.append(["Top 5 Total", total])
table_data.append(["Percentage", f"{percentage:.2f}%"])

# Table Style
table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

content.append(table)

# Build PDF
doc.build(content)

print("\n✅ Marksheet PDF generated successfully as 'Marksheet.pdf'")