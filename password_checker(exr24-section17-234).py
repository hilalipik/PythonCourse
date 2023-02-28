import requests
import hashlib
import sys

def request_api_data(password):
    '''
    Function sends a request to the pwned passwords api website.
    Input: The first 5 characters of a hashed password.
    Output: the response from the website.
    '''
    url = 'https://api.pwnedpasswords.com/range/' + password
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status}, check api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    '''
    Function finds the number of leaks for a wanted hashed password.
    Input: the hashes and their counts fished from website, the hashed password's tail (without the first 5 characters).
    Output: the number of leaks for the hashed password.
    '''
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def hash_password(password):
    '''
    Function returns the hashed password using sha1 hashing to fit the website syntax.
    '''
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


def pwned_api_check(password):
    '''
    Function checks if password was pwned using an api.
    Input: password to check.
    Output: the number of leaks for the hashed password.
    '''
    hashed = hash_password(password)
    first5, tail = hashed[:5], hashed[5:]
    response = request_api_data(first5)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. You should probably change your password.")
        else:
            print(f"{password} wasn't found, Congrats!")


if __name__ == "__main__":
    main(sys.argv[1:])