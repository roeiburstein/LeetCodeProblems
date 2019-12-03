"""
Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z,
and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time.
Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

def main():
   print(isMatch("hellofriends", "hef*.*oa*fr*iena*ds*"))

def isMatch(s: str, p: str) -> bool:
   str1_index = 0 # Counter for index of s
   str2_index = 0 # Counter for index of p
   if p is "" and s is not "":
      return False
   while True:
      if str1_index == len(s): # If we've reached end of the first string
         return checkForEndOfWord(p, str2_index)
      if str2_index == len(p) and p[str2_index - 1] is not '*':
         return False
      if str2_index > 0: # Checks for out of bounds for next if statement
         if p[str2_index] is '*' and not compareChars(s[str1_index], p[str2_index - 1]): # Check if str1 is a new character that '*' doesn't represent
            str2_index += 1 # Increment string2 index
            continue

      if compareChars(s[str1_index], p[str2_index]): # If current character in string1 equals current character in string2
         str1_index += 1 # Increment string1 index
         str2_index += 1 # Increment string2 index
         continue

      else:
         if p[str2_index] is '*': # If characters are not the same, but current character in string2 is '*'
            if compareChars(s[str1_index], p[str2_index - 1]): # If character before '*' in string 2 is the same as current character in string1
               str1_index += 1 # Increment string1 index
               if str2_index > 0 and str1_index < len(p):
                  if p[str2_index - 1] is '.' and not compareChars(s[str1_index - 1], s[str1_index]):
                     str2_index += 1
               continue
            else: # If character before * in string2 is NOT the same as current character in string1
               return False
         elif not compareChars(s[str1_index], p[str2_index]) and p[str2_index + 1] is '*':
            str2_index += 2
            continue
         else: # Characters are not the same and current character in string2 is NOT '*'
            return False

"""
Compares two characters with '.' character allowed to equal anything. Returns
True if characters are equal, False if they are not equal.
"""
def compareChars(char1: str, char2: str) -> bool:
   if len(char1) != 1 or len(char2) != 1:
      return False
   if char1 is char2 or char1 is "." or char2 is ".": # If both characters are equal or at least 1 character is '.'
      return True
   else: # Characters are not equal
      return False

"""
Once end of string1 has been reached, checks if remaining characters in string2
are valid for matching string1. This is only true if we've reached the end of
string2 or if string2 alternates in '*' characters (allowing zero of the
preceding character when matching).
"""
def checkForEndOfWord(string: str, curr_ind: int) -> bool:
   if curr_ind == len(string): # If we've reached end of string1 at the same index as string2
      return True
   if string[curr_ind] is not '*': # If we've ended on a '*'
      curr_ind -= 1
   iter = 2 + curr_ind
   while iter < len(string):
      if string[iter] is not '*':
         return False
      iter += 2
   return string[-1] is '*'

if __name__ == '__main__':
	main()