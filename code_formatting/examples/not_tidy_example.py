from typing import Dict
from random import randbytes, randint,random, randrange, Random, SystemRandom, sample,shuffle
def my_function(parameter1:str,parameter2:int,parameter3:Dict[str, str], 
                parameter4:str, parameter5:str) -> None:
    print(parameter1, parameter2, parameter3, parameter4, parameter5)


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
# fmt: off
def my_function2(df, operator_clasificator, phone_number_col_name, temp_country_code_col_name, 
                 new_operator_col_name,
                 F) -> None:
    df = (
        df.alias("left")
        .join(operator_clasificator.alias("right"),
            F.expr(f"""substr(left.{phone_number_col_name}, 
                   length(left.{temp_country_code_col_name}) +1) == right.msisdn"""),
            how="left_outer")
        .select("left.*", F.col("right.operator_name").alias(new_operator_col_name))
    )
# fmt: on


def my_function3  (paramater1:str,
        parameter2: str) -> str:
    return (((paramater1 + parameter2)))


def my_function4():
    number=5*5
    some_calculation= number*number/25*15


my_list = [1,2,3,4,
           5,6,7]







my_dict = {"affecting_moves":
    {"decrease":
        
        
        [{"change":-1,"move":{"name":"mist-ball",
                                      "url":"https://pokeapi.co/api/v2/move/296/"}}
                 ,{"change":-2,"move":{"name":"overheat",
                                       "url":"https://pokeapi.co/api/v2/move/315/"}},
                 {"change":-2,"move":{"name":"psycho-boost",
                                      "url":"https://pokeapi.co/api/v2/move/354/"}}]}}








if __name__ == "__main__":
        print(
          is_unique(input())
         )

