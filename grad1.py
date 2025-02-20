#Simple program to calculate how many calories the person needs in a day and the amount of water
def calculateBMR(weight, height, age, gender):
    if gender == 'male':
        return 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == 'female':
        return 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    else:
        return None

def calculateAMR(BMR, activity_level):
    if activity_level == 'very low':
        return BMR * 1.4
    elif activity_level == 'low':
        return BMR * 1.5
    elif activity_level == 'middle':
        return BMR * 1.6
    elif activity_level == 'active':
        return BMR * 1.725
    elif activity_level == 'very active':
        return BMR * 1.9
    else:
        return None

def calculateWATER(weight):
    return weight * 0.033

def main():
    gender = input(" Enter your gender (male/female): ").lower()
    weight = float(input(" Enter your weight in kg  "))
    height = float(input(" Enter your height in cm  "))
    age = int(input(" Enter your age "))
    activity_level = input("Enter your activity level \" very low ,low , middle , active , very active\" ")
    BMR = calculateBMR(weight, height, age, gender)
    
    if BMR is not None:
        AMR=calculateAMR(BMR, activity_level)
        WATER=calculateWATER(weight)
        
        if AMR is not None:
         print(f" BMR rate is {BMR:.2f} calorie per day ")
         print(f"AMR rate is  {AMR:.2f} calorie per day ")
         print(f" Water intake  {WATER:.2f} liter per day ")
        else:
         print("Invalid activity level")
    else:
      print("Incorrect gender")
if __name__ =="__main__":
    main()
