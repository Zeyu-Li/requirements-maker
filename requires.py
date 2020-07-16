# imports requests for get and json for json returns
import requests, json


def main():
    # gets user input and formates it
    requires = input('What modules are required (comma separated list): ')
    requires = requires.strip().split(',')

    output = ''
    # for all he items
    for require in requires:
        # format to the right requests
        require = require.strip()
        request = f'https://pypi.org/pypi/{require}/json'
        
        # get request
        response = requests.get(request)

        # check to see if the request returns a good json file
        if response.status_code != 200:
            print(f'The {require} module is not found :(')
            return

        # responce -> json data
        data = json.loads(response.text)

        version_number = data['info']['version']
        output += f'{require}=={version_number}\n'

    # write to requirements.txt
    with open('requirements.txt', 'w') as fp:
        fp.write(output)

    # output to console
    print('requirements.txt:\n' + output)

if __name__ == "__main__":
    main()
