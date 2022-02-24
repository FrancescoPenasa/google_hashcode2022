f = open("c:/Users/zerbi/Desktop/a_an_example.in-1.txt")
n_contributors, n_projects = f.readline().split(" ")
n_contributors = int(n_contributors)
n_projects = int(n_projects)

contributors = {}
projects = {}

for i in range(0,n_contributors):
    contributor_name, n_skills = f.readline().strip("\n").split(" ")
    n_skills = int(n_skills)

    while n_skills > 0:
        skill_name, skill_level = f.readline().strip("\n").split(" ")
        contributors.setdefault(contributor_name, {})[skill_name] = skill_level

        n_skills-=1

for i in range(0,n_projects):
    project_name, n_days, score, best_before, n_roles = f.readline().strip("\n").split(" ")
    n_days = int(n_days)
    score = int(score)
    best_before = int(best_before)
    n_roles = int(n_roles)

    projects.setdefault(project_name, {})["n_days"] = n_days
    projects.setdefault(project_name, {})["score"] = score
    projects.setdefault(project_name, {})["best_before"] = best_before
    projects.setdefault(project_name, {})["roles"] = []

    while n_roles > 0:
        skill_name, skill_level = f.readline().strip("\n").split(" ")
        projects[project_name]["roles"] += [skill_name, skill_level]

        n_roles-=1

print(projects)