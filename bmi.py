
def calculate_bmi (height,weight):
    print("Height = " + str(height))
    print ("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("Bmi = "+ str(bmi))
    if (bmi<18.5):
        value= -1

    elif (bmi > 24):
        value =1

    else:
        value = 0
    print ("Returning Value = " + str(value))
    return value
calculate_bmi(weight = 80, height = 1.73)




