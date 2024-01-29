import pandas as pd
from random import randint



class GradiantDecent:

    def algorithm(x, y, iteration, resolution, min_random_value, max_random_value):

        mse_list, m_list, b_list = [], [], []


            
        val1 = (randint(min_random_value, max_random_value)) / 10
        val2 = (randint(min_random_value, max_random_value)) / 10

        for i in range((int(iteration))):


            if val1 > 0:

                val1 = val1 - resolution
                
                if val2 >= 0:
                    
                    val2 = val2 - resolution
                
                
                else:
                    
                    val2 = val2 + resolution
            
            elif val1 < 0:
                
                val1 = val1 + resolution
                
                if val2 >= 0:
                    
                    val2 = val2 - resolution
                
                else:
                    
                    val2 = val2 + resolution
            else:
                pass

            mse, m = GradiantDecent.deploy_values(val1, val2, x, y)
            mse_list.append(mse) #cost metric
            m_list.append(m) #slope
            b_list.append(val2)  #Intercept

        results = pd.DataFrame({'mse': mse_list, 'm': m_list, 'b': b_list})

        global_minimum = results['mse'].min()
        optimal_values = results.loc[results['mse'] == global_minimum]
        slope = optimal_values['m'].iloc[0]
        intercept = optimal_values['b'].iloc[0]

        return global_minimum, slope, intercept, mse_list, b_list , m_list

    def deploy_values(m, b, x, y):
        y_pred = (m * x) + b
        mse = ((y - y_pred) ** 2).mean()
        return mse, m

    def predict(slope, intercept,x):
        return slope*x + intercept

    def create_model(x, y, iteration, resolution = 0.1 , min_random_value = -100, max_random_value = 100):
        for i in range(iteration):
            return GradiantDecent.algorithm(x, y, iteration, resolution , min_random_value, max_random_value)