"""
Name : George Malak
Date : 26 / 4 /2025
"""


# Create Linear Model y = ax + b
class Private_Linear_Model:
    def __int__(self):
        self.cof_ = None  # slope = a
        self.inter_ = None  # intercept = b
    def fit(self, x_List, y_List):
        size = len(x_List)
        sum_x = sum(x_List)
        sum_y = sum(y_List)
        sum_xy = sum([x_List[i] * y_List[i] for i in range(size)])
        sum_xx = sum([x_List[i] * x_List[i] for i in range(size)])

        #Calc Slope a by this formula
        nemrtr = (size * sum_xy) - (sum_y * sum_x)
        denmntr = (size * sum_xx) - (sum_x ** 2)

        if denmntr == 0:
            print("Cannot Fit a line !!")
            return
        self.cof_ = nemrtr / denmntr

        # Calc intercept b
        self.inter_ = (sum_y - self.cof_ * sum_x) / size

    def predict(self,x_list):
        result = [self.cof_ * i + self.inter_ for i in x_list]
        return result
# Example
x = [1, 2, 3, 4, 5, 6]
y = [50, 55, 60, 65, 70, 75]
model = Private_Linear_Model()
model.fit(x,y)

print("Slope of Model :", model.cof_)
print("Intercept of Model :", model.inter_)

# Predict
test = [8, 9, 10, 11, 15]
prdct = model.predict(test)
print("Predictions : ", prdct)