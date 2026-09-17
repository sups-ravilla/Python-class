student_data = {
    "id1" : {"name": "John", "Class": "8W", "subject_integrations": "Math, Science, English"},
    "id2" : {"name": "Percy", "Class": "8W", "subject_integrations": "Math, Science, English"},
    "id1" : {"name": "John", "Class": "8W", "subject_integrations": "Math, Science, English"},
    "id4" : {"name": "David", "Class": "8W", "subject_integrations": "Math, Science, English"}
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["Class"],details["subject_integrations"])

if unique_key not in seen_keys:
    seen_keys.append(unique_key)
    result[student_id] = details

for k, v in result.items():
    print(k, ":", v)


    