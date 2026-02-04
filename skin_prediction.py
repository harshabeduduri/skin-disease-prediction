def predict_disease(symptom):
    if symptom == "itching":
        return "Possible Allergy. Remedy: Use soothing lotion."
    elif symptom == "rash":
        return "Possible Skin Rash. Remedy: Keep the area clean."
    else:
        return "Condition unclear. Please consult a dermatologist."

user_input = input("Enter symptom: ").lower()
print(predict_disease(user_input))
