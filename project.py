import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class ReportCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Report Card System")
        self.root.geometry("600x850")
        self.root.config(bg="#e8f4fc")

        # ----------------------------------------------------------
        # COMPLETE COURSE → SUBJECTS MAPPING (20+ COURSES)
        # ----------------------------------------------------------
        self.course_subjects = {

            # FULL STACK COURSES
            "python full stack": [
                "Python", "HTML", "CSS", "JavaScript", "SQL", "React", "Django"
            ],
            "java full stack": [
                "Core Java", "Advanced Java", "HTML", "CSS",
                "JavaScript", "Spring Boot", "Hibernate"
            ],

            # DATA COURSES
            "data science": [
                "Python", "Statistics", "Machine Learning", "SQL",
                "Deep Learning", "Data Visualization", "NLP"
            ],
            "machine learning": [
                "Python", "Statistics", "Supervised ML", "Unsupervised ML",
                "Deep Learning", "Model Deployment"
            ],
            "artificial intelligence": [
                "Python", "Neural Networks", "Deep Learning",
                "NLP", "Computer Vision", "Robotics"
            ],

            # CYBER SECURITY
            "cyber security": [
                "Networking", "Linux", "Cryptography", "Ethical Hacking",
                "Cloud Security", "Digital Forensics"
            ],

            # CLOUD & DEVOPS
            "cloud computing": [
                "AWS", "Azure", "GCP", "Linux", "Terraform", "DevOps Basics"
            ],
            "devops": [
                "Git", "Linux", "Docker", "Kubernetes",
                "CI/CD", "Terraform", "Jenkins"
            ],

            # WEB DEVELOPMENT
            "web development": [
                "HTML", "CSS", "JavaScript", "Bootstrap",
                "React", "Node.js", "MongoDB"
            ],

            # TESTING
            "software testing": [
                "Manual Testing", "Automation Testing", "Selenium",
                "API Testing", "JUnit", "Mobile Testing"
            ],

            # MOBILE APP DEVELOPMENT
            "android development": [
                "Java/Kotlin", "XML", "SQLite", "Firebase", "Android Studio"
            ],
            "ios development": [
                "Swift", "XCode", "UIKit", "CoreData", "SwiftUI"
            ],

            # UI UX
            "ui ux": [
                "Figma", "Prototyping", "Wireframing",
                "Visual Design", "User Research"
            ],

            # EMERGING TECHNOLOGIES
            "blockchain": [
                "Ethereum", "Solidity", "Smart Contracts",
                "Web3.js", "Cryptocurrency", "DApps"
            ],
            "big data": [
                "Hadoop", "Spark", "Hive", "Kafka",
                "Data Lakes", "HDFS"
            ],

            # NETWORKING
            "networking": [
                "CCNA Basics", "Routing & Switching", "Network Security",
                "Wireless Networks", "WAN Technologies"
            ],

            # ENGINEERING (CSE/IT)
            "cse": [
                "Data Structures", "Algorithms", "DBMS",
                "Operating System", "Computer Networks", "OOP"
            ],
            "it": [
                "Programming", "DBMS", "Web Development",
                "Networking", "Cloud Basics", "Cybersecurity"
            ],

            # IOT & EMBEDDED
            "iot": [
                "Sensors", "Embedded C", "Python", "MQTT",
                "Cloud IoT", "Arduino/Raspberry Pi"
            ],
            "embedded systems": [
                "C Programming", "Microcontrollers", "IoT Basics",
                "Sensors", "RTOS"
            ],

            # ROBOTICS
            "robotics": [
                "Python", "Sensors", "Actuators", "Control Systems", "ROS"
            ],

            # E-COMMERCE
            "ecommerce": [
                "Web Design", "SEO", "Digital Marketing",
                "Payment Gateways", "Analytics"
            ]
        }

        # ----------------------------------------------------------
        # GUI ELEMENTS
        # ----------------------------------------------------------
        tk.Label(root, text="Student Report Card", font=("Arial", 20, "bold"),
                 bg="#e8f4fc").pack(pady=10)

        frame = tk.Frame(root, bg="#e8f4fc")
        frame.pack()

        tk.Label(frame, text="Student Name:", bg="#e8f4fc").grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(frame, width=30)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Roll Number:", bg="#e8f4fc").grid(row=1, column=0, pady=5)
        self.roll_entry = tk.Entry(frame, width=30)
        self.roll_entry.grid(row=1, column=1)

        tk.Label(frame, text="Enter Course:", bg="#e8f4fc").grid(row=2, column=0, pady=5)
        self.course_entry = tk.Entry(frame, width=30)
        self.course_entry.grid(row=2, column=1)

        tk.Button(frame, text="Load Subjects", bg="#9C27B0", fg="white",
                  command=self.load_subjects).grid(row=3, column=0, columnspan=2, pady=10)

        self.subject_frame = tk.Frame(root, bg="#e8f4fc")
        self.subject_frame.pack()

        tk.Button(root, text="Generate Report", bg="#4CAF50", fg="white",
                  command=self.generate_report, width=20).pack(pady=10)

        tk.Button(root, text="Show Pie Chart", bg="#2196F3", fg="white",
                  command=self.show_pie_chart, width=20).pack(pady=5)

        tk.Button(root, text="Clear", bg="#f44336", fg="white",
                  command=self.clear_fields, width=20).pack(pady=5)

        self.output = tk.Text(root, height=18, width=70, bg="white")
        self.output.pack(pady=10)

        self.subject_entries = []

    # ----------------------------------------------------------
    # LOAD SUBJECTS
    # ----------------------------------------------------------
    def load_subjects(self):
        for widget in self.subject_frame.winfo_children():
            widget.destroy()
        self.subject_entries.clear()

        course = self.course_entry.get().strip().lower()

        if course in self.course_subjects:
            subjects = self.course_subjects[course]
        else:
            # Create custom 4 subjects for unknown course
            subjects = [
                f"{self.course_entry.get().title()} Topic 1",
                f"{self.course_entry.get().title()} Topic 2",
                f"{self.course_entry.get().title()} Topic 3",
                f"{self.course_entry.get().title()} Topic 4"
            ]
            messagebox.showinfo("Notice", 
                f"No predefined subjects for '{self.course_entry.get()}'.\nCreating custom subjects.")

        for i, subject in enumerate(subjects):
            tk.Label(self.subject_frame, text=f"{subject} Marks:", bg="#e8f4fc").grid(row=i, column=0, pady=5)
            entry = tk.Entry(self.subject_frame, width=25)
            entry.grid(row=i, column=1)
            self.subject_entries.append((subject, entry))

    # ----------------------------------------------------------
    # GRADE CALCULATION
    # ----------------------------------------------------------
    def get_grade(self, avg):
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else: return "D"

    # ----------------------------------------------------------
    # GENERATE REPORT
    # ----------------------------------------------------------
    def generate_report(self):
        try:
            self.name = self.name_entry.get()
            self.roll = self.roll_entry.get()
            self.course = self.course_entry.get()

            if not self.subject_entries:
                messagebox.showerror("Error", "Load subjects first!")
                return

            self.marks = {}
            total = 0

            for subject, entry in self.subject_entries:
                m = int(entry.get())
                self.marks[subject] = m
                total += m

            avg = total / len(self.subject_entries)
            grade = self.get_grade(avg)

            report = f"""
===================================================
                    STUDENT REPORT CARD
===================================================
Name        : {self.name}
Roll Number : {self.roll}
Course      : {self.course}
---------------------------------------------------
"""

            for sub, mk in self.marks.items():
                report += f"{sub:<30}: {mk}\n"

            report += f"""
---------------------------------------------------
Total Marks : {total}
Average     : {avg:.2f}
Grade       : {grade}
===================================================
"""

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, report)

        except ValueError:
            messagebox.showerror("Error", "Marks must be numbers only!")

    # ----------------------------------------------------------
    # PIE CHART
    # ----------------------------------------------------------
    def show_pie_chart(self):
        if not hasattr(self, "marks"):
            messagebox.showerror("Error", "Generate report first!")
            return

        plt.figure(figsize=(7, 7))
        plt.pie(self.marks.values(), labels=self.marks.keys(),
                autopct="%1.1f%%", startangle=90)
        plt.title(f"Marks Distribution - {self.name}")
        plt.show()

    # ----------------------------------------------------------
    # CLEAR FORM
    # ----------------------------------------------------------
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.output.delete("1.0", tk.END)

        for widget in self.subject_frame.winfo_children():
            widget.destroy()
        self.subject_entries.clear()


# ---------------- MAIN PROGRAM ----------------
root = tk.Tk()
app = ReportCard(root)
root.mainloop()





