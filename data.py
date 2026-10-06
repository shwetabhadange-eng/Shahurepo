import  pandas as pd
import requests

data = {
    "id": [1, 2, 3],
    "name": ['A', 'B', 'C'],  # pyright: ignore[reportInvalidTypeForm]
    "age": [20, 30, 60]  # pyright: ignore[reportInvalidTypeForm]
}

print('Students Details')
df =pd.DataFrame(data)
print(df)

print('API data')
response = requests.get('https://jsonplaceholder.typicode.com')
print(response.json())

