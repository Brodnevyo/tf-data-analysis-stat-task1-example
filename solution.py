import pandas as pd
import numpy as np


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    n = len(x)
    x_mean = np.mean(x)
    x_var = np.mean(x**2) - x_mean**2
    a = 2 * x_var / (79**2 * n)# Не меняйте название функции и её аргументы
    return a # Ваш ответ
