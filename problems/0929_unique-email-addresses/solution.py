# Question : 929 
# Difficulty : Easy
# Time : O(n)
# Space : O(n)
# Runtime : 48 ms

class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        email_list = set()
        for email in emails:
            name, domain = email.split('@')[0:2]
            name = name.replace(".", "")
            name = name.split('+')[0]
            email_list.add(name + domain)
        return len(email_list)

