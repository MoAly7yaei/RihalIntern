"""# Import statements outside the class
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Modules:
    @staticmethod
    def installation():
        # Check and install pandas
        try:
            import pandas as pd
        except ModuleNotFoundError:
            print("pandas is not installed. Please run 'pip install pandas'.")

        # Check and install numpy
        try:
            import numpy as np
        except ModuleNotFoundError:
            print("numpy is not installed. Please run 'pip install numpy'.")

        # Check and install matplotlib
        try:
            import matplotlib.pyplot as plt
        except ModuleNotFoundError:
            print("matplotlib is not installed. Please run 'pip install matplotlib'.")

        # Check and install seaborn
        try:
            import seaborn as sns
        except ModuleNotFoundError:
            print("seaborn is not installed. Please run 'pip install seaborn'.")
"""