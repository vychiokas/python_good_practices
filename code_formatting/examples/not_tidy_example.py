from typing import Dict
def my_function(parameter1: str, parameter2: int, parameter3: Dict[str, str]) -> None:
    print(parameter1, parameter2, parameter3)


my_dictionary = {"name":"value","another name":"another value"}



def is_unique(
               s
               ):
    s = list(s
                )
    s.sort()
 
 
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1
 
 
if __name__ == "__main__":
    print(
          is_unique(input())
         )