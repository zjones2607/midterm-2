import csv

class Student:
    def __init__(self, sid, name, gpa): self.sid, self.name, self.gpa = sid, name, float(gpa)
    def __str__(self): return f"{self.sid} | {self.name} | GPA: {self.gpa}"

class StudentManager:
    def __init__(self, file): self.file = file; self.students = []
    def load(self):
        try:
            with open(self.file) as f:
                next(f)  # skip header
                self.students = [Student(*line.strip().split(',')) for line in f]
        except Exception as e: print("Error:", e)
    def print_all(self): [print(s) for s in self.students]
    def filter_gpa(self, min_gpa): return [s for s in self.students if s.gpa >= min_gpa]
    def export(self, students, outfile):
        with open(outfile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['student_id','name','gpa'])
            writer.writerows([[s.sid, s.name, s.gpa] for s in students])

if __name__ == "__main__":
    m = StudentManager('students.csv')
    m.load()
    m.print_all()
    filtered = m.filter_gpa(3.5)
    print("\nFiltered:")
    [print(s) for s in filtered]
    m.export(filtered, 'filtered_students.csv')