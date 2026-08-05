def bmi(weight, height):
    measure = weight/(height*height)
    return ("Underweight" if measure <= 18.5 else "Normal" if measure <= 25 else "Overweight" if measure <= 30 else "Obese" )
