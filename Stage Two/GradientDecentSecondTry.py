import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt

class Regression:

    def __init__(self):
        self.val1 = (randint(-10000, 10000)) / 1000
        self.val2 = (randint(-10000, 10000)) / 1000
        self.iteration = 100000
        self.learning_rate = 0.1

    def algorithm(self, x, y):
        mse_list, m_list, b_list = [], [], []

        for i in range(self.iteration):
            if self.val1 > 0:
                self.val1 -= self.learning_rate
                self.val2 = self.val2 - self.learning_rate if self.val2 >= 0 else self.val2 + self.learning_rate
            elif self.val1 < 0:
                self.val1 += self.learning_rate
                self.val2 = self.val2 - self.learning_rate if self.val2 >= 0 else self.val2 + self.learning_rate

            mse, m = self.deploy_values(self.val1, self.val2, x, y)
            mse_list.append(mse)
            m_list.append(m)
            b_list.append(self.val2)

        results = pd.DataFrame({'mse': mse_list, 'm': m_list, 'b': b_list})
        global_minimum = results['mse'].min()
        optimal_values = results.loc[results['mse'] == global_minimum]
        slope = optimal_values['m'].iloc[0]
        intercept = optimal_values['b'].iloc[0]

        return global_minimum, slope, intercept, mse_list, b_list, m_list

    @staticmethod
    def deploy_values(m, b, x, y):
        y_pred = (m * x) + b
        mse = ((y - y_pred) ** 2).mean()
        return mse, m

    @staticmethod
    def predict(slope, intercept, x):
        return slope * x + intercept

    def fit(self, x, y):
        return self.algorithm(x, y)

    @staticmethod
    def try_the_algorithm():
        test_data = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7], 'y': [2, 4, 6, 8, 10, 12, 14]})
        """
        In this test data the sutabe parametar is y = 2x so slope = 2 and intercept = 0
        """
        x = test_data['x']
        y = test_data['y']
        model = Regression()
        global_minimum, slope, intercept, mse_list, b_list, m_list = model.fit(x=x, y=y)
        print(slope, intercept)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

        ax.scatter(m_list, b_list, mse_list, c='red', label='MSE')
        
        ax.set_xlabel('Slope (m)')
        ax.set_ylabel('Intercept (b)')
        ax.set_zlabel('MSE')

        plt.legend()
        plt.show()


