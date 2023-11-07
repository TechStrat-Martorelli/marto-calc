import numpy as np
import pandas as pd

def mapearIdade(idade):
    if idade <= 30:
        return 'até 30'
    elif idade <= 50:
        return '31 a 50'
    elif idade <= 70:
        return '51 a 70'
    elif idade <= 90:
        return '71 a 90'
    else:
        return '91 ou mais'

def mapearExpectativaVida(faixa):
    if faixa == 'até 30': return 0.05
    if faixa == '31 a 50': return 0.3
    if faixa == '51 a 70': return 0.3
    if faixa == '71 a 90': return 0.5
    return 0.8

def mapearCurva(curva):
    if curva == 'Normal': return 35
    if curva == 'Mais novos': return 55
    if curva == 'Mais velhos': return 75

def criar_df(curva, filiados):
    # Define age groups
    idades = list(range(25, 100))

    # Create a normal distribution with a mean and standard deviation
    mean_age = mapearCurva(curva)  # Mean age
    std_deviation = 15  # Standard deviation

    # Generate 2000 random ages following a normal distribution
    ages = np.random.normal(mean_age, std_deviation, filiados)

    # Clip the generated ages to stay within the defined range
    ages = np.clip(ages, min(idades), max(idades))

    # Round the ages to the nearest integer
    ages = np.round(ages).astype(int)

    # Count the number of people in each age group
    age_counts = {idade: ages.tolist().count(idade) for idade in idades}

    # Create a DataFrame
    data = {
        'idade': idades, 
        'faixa': [mapearIdade(idade) for idade in idades],
        'quantidade': [age_counts[idade] for idade in idades]
    }

    df = pd.DataFrame(data)

    df['expectativa'] = df['faixa'].apply(mapearExpectativaVida)

    df['falecidos'] = df['quantidade'] * df['expectativa']
    df['falecidos'] = df['falecidos'].astype(int)

    df['vivos'] = df['quantidade']-df['falecidos']
    df['vivos'] = df['vivos'].astype(int)

    return df

