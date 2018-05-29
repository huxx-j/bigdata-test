s = """We encourage everyone to contribute to Python. If you still have questions
after reviewing the material
in this guide, then the Python Mentors group is available to help guide new
contributors through the process."""

s_rep1 = s.replace(".", "")
s_rep2 = s_rep1.replace(",", "")
s_lower = s.lower()
s_list = s_lower.split()
s_set = set(s_list)
s_sorted = sorted(s_set)

for i in s_sorted:
    print("{0} : {1}".format(i, s_lower.count(i)))
