import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns=['score']).assign(group = 'Group A')
    
    sns.histplot(data=df_normal_a, x='score', bins=50, kde=True)
    
    plt.show()
