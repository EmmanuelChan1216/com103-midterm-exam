# Task Tracker Program

# COM 103 Midterm Exam

# Task types: parallel lists
task_names = ["Program Logic / Coding", "UI / Output Formatting", "Testing & Debugging", "Documentation / README", "Presentation Slides"]
task_hours = [6, 3, 2, 2, 2]

# Get project information
project_title = ""
while not project_title:
    project_title = input("Project title: ").strip()

group_name = ""
while not group_name:
    group_name = input("Group name: ").strip()

print()
print("=" * 42)
print("   COM 103 PROJECT -- TASK TYPES")
print("=" * 42)

# Display task types using a loop
for i in range(len(task_names)):
    print(f" {i + 1}. {task_names[i]:<25} [{task_hours[i]}h]")

print("=" * 42)
print()

# Storage for assignments
assigned_tasks = []
assigned_members = []
assigned_statuses = []
assigned_points = []

# Task entry loop - runs exactly 4 times
for task_slot in range(4):
    print(f"--- TASK {task_slot + 1} ---")
    task_number = int(input("Task number (1-5, 0 to skip): ").strip() or "0")
    
    if task_number == 0:
        print()
        continue
    
    if 1 <= task_number <= 5:
        member_name = input("Member name: ").strip()
        status = input("Status (done/pending): ").strip().lower()
        
        if status in ("done", "pending"):
            assigned_tasks.append(task_number)
            assigned_members.append(member_name)
            assigned_statuses.append(status)
            assigned_points.append(2 if status == "done" else 1)
            print()
        else:
            print("Invalid status.")
            print()
    else:
        print("Invalid task number.")
        print()

# Calculate totals
total_earned = sum(assigned_points)
total_assigned = len(assigned_tasks)
total_max = total_assigned * 2
progress_percent = int((total_earned / total_max) * 100) if total_max > 0 else 0

# Determine project status
if progress_percent >= 75:
    project_status = "PROJECT READY!"
elif progress_percent >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

# Display task board
print("=" * 48)
print(f"     {project_title} -- TASK BOARD")
print("=" * 48)
print(f"Project : {project_title}")
print(f"Group   : {group_name}")
print("-" * 48)

# Display each assigned task
for i in range(len(assigned_tasks)):
    task_idx = assigned_tasks[i] - 1
    print(f"[{i + 1}] {task_names[task_idx]} [{task_hours[task_idx]}h]")
    print(f"    Assigned to : {assigned_members[i]}")
    print(f"    Status      : {assigned_statuses[i]}")
    print(f"    Points      : {assigned_points[i]} / 2")
    print()

print("-" * 48)
print(f"Points Earned   : {total_earned} / {total_max}")
print(f"Progress        : {progress_percent}%")
print(f"Project Status  : {project_status}")
print("=" * 48)
