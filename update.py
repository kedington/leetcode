import re
from question import Question

question = Question("Longest Substring Without Repeating Characters", "3", "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "medium", "lengthOfLongest.py")

readme = "README.md"

line_template = "| [{0}.]({1}) | [{2}]({3}/{4}) |\n"

expression_match = "\| \[(.*)\.\]"

# Searches the README for where the question should be in the table of contents and writes it
def update_readme(question):
	with open(readme, "r+") as f:
		lines = f.readlines()
		for idx in range(len(lines)):
			cur_num = re.search(expression_match, lines[idx])
			if cur_num:
				if int(cur_num.group(1)) > int(question.number):
					break
		lines.insert(idx, line_template.format(question.number, question.link, question.name, question.difficulty, question.file_name))
		f.seek(0)
		f.writelines(lines)
	
