"""
Algorithm

    1- Define 2 random values (m,b)
    2- Check if it is valid values refering to the cost function
    3- If it's not valid then Modefy the value to decrease the cost till we can reach to the sutable values.
    4- return (m,b)
"""

import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




class Regression:
    def __init__(self):
        self.learning_rate = 0.1
        self.m = randint(-1000 , 1000)  
        self.b = randint(-1000, 1000)  
        self.cost = []
        self.epochs = 1000

    def cost_function(self, X, y):
        y_pred = [(self.m * x  + self.b) for x in X]
        mse_value = np.mean([((y_pred[i] - y[i]) ** 2) for i in range(len(y))])
        return mse_value

    def fit(self, X, y):
        m_values = []
        b_values = []

        X = [value for value in X]
        y = [value for value in y]

        
        for i in range(self.epochs):
            try:
                y_pred = (self.m * X[i]) + self.b
                dm = -2 * np.mean(X[i] * (y[i] - y_pred))
                db = -2 * np.mean(y[i] - y_pred)
                
                # Store current values of m and b
                m_values.append(self.m)
                b_values.append(self.b)
                
                # Store current cost
                self.cost.append(self.cost_function(X, y))
                try:

                    if self.cost[i] <= self.cost[i-1]:
                        self.m -= self.learning_rate * dm
                        self.b -= self.learning_rate * db
                    else:
                        pass
                except IndexError:
                    pass

            except IndexError:
                if i == len(X):
                    j = 0
                    y_pred = (self.m * X[j]) + self.b
                    dm = -2 * np.mean(X[j] * (y[j] - y_pred))  # Gradient w.r.t. m
                    db = -2 * np.mean(y[j] - y_pred)  # Gradient w.r.t. b

                    # Store current values of m and b
                    m_values.append(self.m)
                    b_values.append(self.b)
                    
                    # Store current cost
                    self.cost.append(self.cost_function(X, y))

                    try:

                        if self.cost[i] <= self.cost[i-1]:
                            self.m -= self.learning_rate * dm
                            self.b -= self.learning_rate * db
                        else:
                            pass
                    except IndexError:
                        pass


                    j += 1
                    if j == len(X):
                        j = 0


        # 3D Visualization of Gradient Descent
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a 3D scatter plot
        ax.scatter(m_values, b_values, self.cost, c='b', marker='o')
        
        # Create a line plot for the trajectory
        ax.plot(m_values, b_values, self.cost, color='r')
        
        ax.set_xlabel('m values')
        ax.set_ylabel('b values')
        ax.set_zlabel('Cost')
        plt.title('Gradient Descent Trajectory')
        plt.show()

    def predict(self, X):
        return (self.m * X) + self.b
    
        





"""
class Classification:
    def __init__(self, random_minimum_value, random_maximum_value):
        self.m = randint(a=int(random_minimum_value), b = int(random_maximum_value))
        self.b = randint(a=int(random_minimum_value), b = int(random_maximum_value))
        self.cost = []
        self.learning_rate = 0.01
        self.epochs = 100
        return self

    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
       
    def cost_function(self, X, y):
        for i in range(int((self.epochs)**0.5)):
            z = (self.m * X) + self.b
            y_pred = Classification.sigmoid(z)
            log_loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
            self.cost.append(log_loss)
        return self.cost

"""
            


