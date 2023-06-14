import requests


token = 'c170af50-1a63-46a0-8b5a-5da9156ceb52'
url = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/tickets/'
params = {
    "theme": "string",
    "numberFrom": 0,
    "numberTo": 0,
    "statuses": [
      "NEW"
    ],
    "priorities": [
      "NONE"
    ],
    "specialistIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "contractIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "systemIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "workGroupIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "tagIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "clientIds": [
      "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ],
    "tagName": "string",
    "clientName": "string",
    "specialistName": "string",
    "systemName": "string",
    "dateSolveFrom": "2022-11-03T09:06:28.932Z",
    "dateSolveTo": "2022-11-03T09:06:28.932Z"
}

headers = {'Authorization': 'Bearer ' + token}

response = requests.get(url,headers=headers, params=params)

print(response.json())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
