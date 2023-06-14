data3 = {'session_code': 'cBzhS4_YewBZmusi1pCtEy9b8vz7Ru2crjRi_EByFQE',
'execution': '2d1c4e91-4f13-4589-a025-9a9e4dd5e97e',
'client_id': "frontapp",
'tab_id': 'ka2B7NKQtKo'}

url3 = 'http://keycloak.t1support-portal.dev.ts:8080/auth/realms/T1-Support-Portal/login-actions/authenticate?session_code=J_8Y5-3CPLhDmTCSv7KOHas66HFDUFJysLPgmhcKnoA&execution=2d1c4e91-4f13-4589-a025-9a9e4dd5e97e&client_id=frontapp&tab_id=D6suZWoL_jU'

headers2 = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Sec-Ch-Ua": ""Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": ""Windows"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6489ac62-1d21311b2bcd3b811ddbd22d"
  }

response = requests.get(url3, headers=headers2, data=data3)
print(response)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
