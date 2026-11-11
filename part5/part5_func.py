# ==========================
# WARM-UP: SMALL HELPERS
# ==========================

# Calculate the area of a circle
def area_of_circle(r: float) -> float:
    return 3.14 * r * r


# Check whether a number is even
def is_even(n: int) -> bool:
    return n % 2 == 0


# Greet a person in English or Urdu
def greet(name: str, lang: str = "en") -> str:
    if lang == "en":
        return f"Hello, {name}"
    elif lang == "ur":
        return f"Salaam, {name}"
    else:
        return f"Unsupported language: {lang}"


# ==========================
# BUILD: MARKS TOOLKIT
# ==========================

# Calculate average marks
def average(marks: list[int | float]) -> float:
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    return sum(marks) / len(marks)


# Assign grade based on average marks
def grade(avg: float) -> str:

    # Reject marks outside the valid range
    if avg < 0 or avg > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"


# Generate a student's report
def report(name: str, marks: list[int | float]) -> str:
    avg = average(marks)
    student_grade = grade(avg)

    return f"{name}: Average = {avg:.2f}, Grade = {student_grade}"


# ==========================
# TEST THE FUNCTIONS
# ==========================

if __name__ == "__main__":

    print("--- Warm-up Functions ---")
    print("Circle area:", area_of_circle(3))
    print("Is 4 even?", is_even(4))
    print(greet("Ali", "en"))
    print(greet("Sara", "ur"))

    print("\n--- Marks Toolkit ---")
    print(report("Ali", [85, 90, 80]))
    print(report("Sara", [70, 75, 80]))
    print(report("Ahmed", [45, 55, 60]))
