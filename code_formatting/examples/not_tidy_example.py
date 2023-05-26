from typing import Dict


def my_function(parameter1: str, parameter2: int, parameter3: Dict[str, str]) -> None:
    print(parameter1, parameter2, parameter3)


my_dictionary = {"name": "value", "another name": "another value"}



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
#fmt: off
def my_function2(df, operator_clasificator, phone_number_col_name, temp_country_code_col_name, new_operator_col_name, F) -> None:
    df = (
        df.alias("left")
        .join(operator_clasificator.alias("right"),
            F.expr(f"""substr(left.{phone_number_col_name}, 
                   length(left.{temp_country_code_col_name}) +1) == right.msisdn"""),
            how="left_outer")
        .select("left.*", F.col("right.operator_name").alias(new_operator_col_name))
    )
#fmt: on
if __name__ == "__main__":
    print(
          is_unique(input())
         )



