#ask the user for the number of fat grams
#and carbs
#calculate calories from fat = fat * 9
#and calories from carbs = carb * 4
#then calculate total calories


def UserInput():
  fat_grams = float(input('Enter the number of fat grams: '))
  carb_grams = float(input('Enter the number of carb grams: '))
  return fat_grams,carb_grams



def cals_fat(n1,n2):
    #cals_fat = fat_grams * 9
    #print(cals_fat)
    return n1*n2

def cals_carb(n1,n2):
   # cals_carb = carb_grams * 4
   # print(cals_carb)
    return n1*n2


def cals_total(n1,n2):
    #cals_total = cals_carb * cals_fat
    #print(cals_total)
    return n1*n2

def main():
    fat_cal = 9
    carb_cal = 4
    fgrams,cgrams = UserInput()
    cals_fats = cals_fat(fat_grams,fat_cal)

main()
