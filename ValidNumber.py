"""
This answer is a joke, but it technically works :)
"""

def main():
   print(isNumber("0.0.1"))

def isNumber(s: str) -> bool:
   try:
      float(s)
   except ValueError:
      return False
   return True

if __name__ == '__main__':
	main()