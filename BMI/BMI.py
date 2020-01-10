class BMICALC:
    def BMI(height,weight):
        bmi = weight/(height*height)

        if bmi <= 18.5:
            return 'Your BMI is', bmi, 'which means you are underweight.'

        elif bmi > 18.5 and bmi < 25:
            return 'Your BMI is', bmi, 'which means you are normal.'

        elif bmi > 25 and bmi < 30:
            return 'Your BMI is',bmi, 'which means you are overweight.'

        elif bmi > 30:
            return 'Your BMI is', bmi, 'which means you are obese.'

    bmi=BMI(1.7,90)
    print(bmi)