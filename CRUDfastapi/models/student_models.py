def student_model(student: dict) -> dict:
    return {
        "prn": int(student["prn"]),
        "name": student["name"],
        "age": student["age"],
        "contact": int(student["contact"])
    }
