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

projects_keys = list(projects)
contributors_keys = list(contributors)

tmp_f = open("C:/Users/zerbi/Desktop/google_hashcode2022/result.txt", "w")
projects_count = 0

for i in range(0,len(projects_keys)):
    roles = projects[projects_keys[i]]["roles"]

    final_contributors = []

    for j in range(0,len(roles)-1,2):
        skill_name = roles[j]
        skill_level = roles[j+1]

        for contributor_name in contributors_keys:
            if skill_name in contributors[contributor_name].keys():
                if contributors[contributor_name][skill_name] >= skill_level:
                    final_contributors.append(contributor_name)

    if len(final_contributors) > 0:
        projects_count += 1
        tmp_f.write(projects_keys[i]+"\n")
        for name in final_contributors:
            tmp_f.write(name+" ")
        tmp_f.write("\n")

tmp_f = open("C:/Users/zerbi/Desktop/google_hashcode2022/result.txt", "r")
tmp_oldfile = tmp_f.read()

tmp_f = open("C:/Users/zerbi/Desktop/google_hashcode2022/result.txt", "w")
tmp_f.write(str(projects_count)+"\n")
tmp_f.write(tmp_oldfile)