# Task Tracker Program

# COM 103 Midterm Exam

# Task types: parallel lists
task_names = ["Program Logic / Coding", "UI / Output Formatting", "Testing & Debugging", "Documentation / README", "Presentation Slides"]
task_hours = [6, 3, 2, 2, 2]

# Get project information
project_title = input("Project title: ")
group_name = input("Group name: ")

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
    try:
        task_number = int(input("Task number (0 to skip): "))
    except ValueError:
        # invalid input treated as skip
        print("Invalid input - slot skipped.")
        print()
        continue

    if task_number == 0:
        print()
        continue

    # Validate task number (1-5)
    if 1 <= task_number <= 5:
        member_name = input("Member name: ")
        status = input("Status (done/pending): ").strip().lower()
        if status not in ("done", "pending"):
            # default to pending if unexpected
            status = "pending"
        print()

        # Store assignment
        assigned_tasks.append(task_number)
        assigned_members.append(member_name)
        assigned_statuses.append(status)

        # Calculate points based on status
        if status == "done":
            points = 2
        else:
            points = 1

        assigned_points.append(points)
    else:
        print("Invalid task number - slot skipped.")
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
    task_name = task_names[task_idx]
    hours = task_hours[task_idx]
    member = assigned_members[i]
    status = assigned_statuses[i]
    points = assigned_points[i]

    print(f"[{i + 1}] {task_name:<22} [{hours}h]")
    print(f"    Assigned to : {member}")
    print(f"    Status      : {status}")
    print(f"    Points      : {points} / 2")
    print()

print("-" * 48)
print(f"Points Earned   : {total_earned} / {total_max}")
print(f"Progress        : {progress_percent}%")
print(f"Project Status  : {project_status}")
print("=" * 48)
# COM 103 Midterm Exam

# Task types: parallel lists
task_names = ["Program Logic / Coding", "UI / Output Formatting", "Testing & Debugging", "Documentation / README", "Presentation Slides"]
task_hours = [6, 3, 2, 2, 2]

# Get project information
project_title = input("Project title: ")
group_name = input("Group name: ")

print()
print("=" * 42)
print("   COM 103 PROJECT -- TASK TYPES")
print("=" * 42)

# Display task types using a loop
for i in range(5):
    print(f" {i + 1}. {task_names[i]:<25} [{task_hours[i]}h]")

print("=" * 42)
print()

# Storage for assignments
assigned_tasks = []
assigned_members = []
assigned_statuses = []
assigned_points = []
assigned_max_points = []

# Task entry loop - runs exactly 4 times
for task_slot in range(4):
    print(f"--- TASK {task_slot + 1} ---")
    task_number = int(input("Task number (0 to skip): "))
    
    if task_number == 0:
        print()
        continue
    
    # Validate task number (1-5)
    if task_number >= 1 and task_number <= 5:
        member_name = input("Member name: ")
        status = input("Status (done/pending): ")
        print()
        
        # Store assignment
        assigned_tasks.append(task_number)
        assigned_members.append(member_name)
        assigned_statuses.append(status)
        
        # Calculate points based on status
        if status == "done":
            points = 2
        else:
            points = 1
        
        assigned_points.append(points)
        assigned_max_points.append(2)

# Calculate totals
total_earned = sum(assigned_points)
total_max = sum(assigned_max_points)
progress_percent = (total_earned // total_max) * 100 if total_max > 0 else 0

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
    task_name = task_names[task_idx]
    hours = task_hours[task_idx]
    member = assigned_members[i]
    status = assigned_statuses[i]
    points = assigned_points[i]
    
    print(f"[{i + 1}] {task_name:<22} [{hours}h]")
    print(f"    Assigned to : {member}")
    print(f"    Status      : {status}")
    print(f"    Points      : {points} / 2")
    print()

print("-" * 48)
print(f"Points Earned   : {total_earned} / {total_max}")
print(f"Progress        : {progress_percent}%")
print(f"Project Status  : {project_status}")
print("=" * 48)