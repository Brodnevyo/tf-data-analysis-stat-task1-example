import pandas as pd
import numpy as np


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)
    a = (x_bar - 79) / (2 * s**2)
    return a # Ваш ответ
