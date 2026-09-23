student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "James", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "David", "class": "V", "subject": "english, math, science"}
}

print("Student records of id1 - id4")
print(student_data)

print("")
print("ID4 details:")
print(student_data.get("id4", "Not Found"))

print("")
print("ID5 details:")
print(student_data.get("id5", "Not Found"))

student_data["id5"] = {
    "name": "Julian",
    "class": "V",
    "subject" : "english, art, science",
}

print("")
print("After creating ID5:")
print(student_data.get("id5", "Not Found"))

print("")
print("After updating student data:")
print(student_data)

cleaned_data = {}
seen_records = []
 
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
 
student_data = cleaned_data
 
print("")
print("After removing duplicate records:")
print(student_data)
 
removed_student = student_data.pop("id4", "Student not found")
 
print("")
print("Removed student:")
print(removed_student)
 
print("")
print("Total student records left:", len(student_data))
 
print("")
print("===== FINAL STUDENT SUBJECT RECORDS =====")
 
for student_id, details in student_data.items():
    # FIXED: Changed student_data to student_id to print the ID instead of the whole dictionary
    print(student_id, ":", details)
 
print("==========================================")
