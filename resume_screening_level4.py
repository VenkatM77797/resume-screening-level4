import os
import PyPDF2

# -----------------------------
# CONFIG
# -----------------------------
MUST_HAVE = ["python", "sql", "excel"]
NICE_TO_HAVE = ["machine learning", "pandas", "numpy", "power bi", "communication"]

CURRENT_YEAR = 2026

# -----------------------------
# READ PDF
# -----------------------------
def read_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for p in reader.pages:
            text += (p.extract_text() or "")
    return text.lower()

# -----------------------------
# SIMPLE SKILL EXTRACTION
# -----------------------------
def extract_skills(text, skills):
    found = []
    for s in skills:
        if s in text:
            found.append(s)
    return found

# -----------------------------
# EXPERIENCE (VERY SIMPLE)
# -----------------------------
def extract_experience(text):
    years = []
    for y in range(1990, CURRENT_YEAR + 1):
        if str(y) in text:
            years.append(y)

    if len(years) >= 2:
        return min(CURRENT_YEAR - min(years), 5)  # cap at 5 years
    return 0

# -----------------------------
# DECISION LOGIC
# -----------------------------
def decision_logic(found):
    missing = [s for s in MUST_HAVE if s not in found]

    if len(missing) == 0:
        return "ELIGIBLE", missing
    elif len(missing) == 1:
        return "REVIEW", missing
    else:
        return "REJECT", missing

# -----------------------------
# SCORE
# -----------------------------
def score(found, exp):
    skill_score = (len(found) / (len(MUST_HAVE) + len(NICE_TO_HAVE))) * 100
    exp_score = (exp / 5) * 100
    return round(0.7 * skill_score + 0.3 * exp_score, 2)

# -----------------------------
# MAIN
# -----------------------------
def main():
    folder = "resumes"

    if not os.path.exists(folder):
        print(f"Folder '{folder}' not found. Please create it and add PDF resumes.")
        return

    print("\n=== SIMPLE LEVEL 4 ATS RESULTS (RANKED) ===\n")

    results = []

    for file in os.listdir(folder):
        if not file.endswith(".pdf"):
            continue

        text = read_pdf(os.path.join(folder, file))

        all_skills = MUST_HAVE + NICE_TO_HAVE
        found = extract_skills(text, all_skills)

        decision, missing = decision_logic(found)
        exp = extract_experience(text)
        final_score = score(found, exp)

        results.append({
            "file": file,
            "decision": decision,
            "score": final_score,
            "experience": exp,
            "skills": found,
            "missing": missing
        })

    # Sort by score (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)

    rank = 1
    for r in results:
        print(f"Rank #{rank}")
        print(f"Resume: {r['file']}")
        print(f"Decision: {r['decision']}")
        print(f"Final Score: {r['score']}")
        print(f"Experience (approx): {r['experience']} years")
        print(f"Found Skills: {r['skills']}")
        if r["missing"]:
            print(f"Missing MUST-HAVE: {r['missing']}")
        print("-" * 60)
        rank += 1

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    main()
