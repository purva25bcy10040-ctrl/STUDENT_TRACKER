import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(columns=["ID", "Name", "Branch", "Year", "Email"])

def add_student():
    sid = np.random.randint(1000, 9999)
    name = input("Name: ")
    branch = input("Branch: ")
    year = input("Year: ")
    email = input("Email: ")
    global data
    data = pd.concat([data, pd.DataFrame([[sid, name, branch, year, email]], columns=data.columns)], ignore_index=True)
    print(f"Added with ID {sid}")

def view_students():
    if data.empty: print("No students")
    else: print(data)

def search_student():
    try: sid = int(input("ID: "))
    except: print("Invalid"); return
    res = data[data["ID"] == sid]
    print(res if not res.empty else "Not found")

def update_student():
    global data
    try: sid = int(input("ID to update: "))
    except: print("Invalid"); return
    if sid not in data["ID"].values: print("Not found"); return
    idx = data.index[data["ID"] == sid][0]
    for col in ["Name","Branch","Year","Email"]:
        new = input(f"New {col} (blank to skip): ")
        if new.strip(): data.at[idx, col] = new
    print("Updated")

def delete_student():
    global data
    try: sid = int(input("ID to delete: "))
    except: print("Invalid"); return
    if sid in data["ID"].values:
        data = data[data["ID"] != sid]
        print("Deleted")
    else: print("Not found")

def plot_branch():
    if data.empty: print("No data"); return
    counts = data["Branch"].value_counts()
    counts.plot(kind='bar', color='skyblue')
    plt.title("Branch Distribution")
    plt.xlabel("Branch")
    plt.ylabel("Students")
    plt.show()

def main():
    options = {"1": add_student, "2": view_students, "3": search_student,
               "4": update_student, "5": delete_student, "6": plot_branch}
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Plot 7.Exit")
        ch = input("Choice: ")
        if ch == "7": break
        func = options.get(ch)
        if func: func()
        else: print("Invalid")

if __name__ == "__main__":
    main()
