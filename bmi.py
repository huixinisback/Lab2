
def calculate_bmi (height,weight):
    print("Height = " + str(height))
    print ("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("Bmi = "+ str(bmi))
    if (bmi<19):
        value= -1
    elif (bmi > 24):
        value =1
    else:
        value = 0
    print ("Returning Value = " + str(value))

calculate_bmi(weight = 57, height = 1.73)




