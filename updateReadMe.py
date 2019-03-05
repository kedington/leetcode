from question import Question
import re

question = Question("Longest Substring Without Repeating Characters", "3", "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "medium", "lengthOfLongest.py")

read_me = "README.md"

line_template = "| [{0}.]({1}) | [{2}]({3}/{4}) |\n"

expression_match = "\| \[(.*)\.\]"

with open(read_me, "r+") as f:
	lines = f.readlines()
	for idx in range(len(lines)):
		cur_num = re.search(expression_match, lines[idx])
		if cur_num:
			if int(cur_num.group(1)) > int(question.number):
				break
	lines.insert(idx, line_template.format(question.number, question.link, question.name, question.difficulty, question.file_name))
	f.seek(0)
	f.writelines(lines)
	
