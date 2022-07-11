# RESTFUL APIs with Requests Example

Chuck Norris Jokes - They are still as fresh as the man himself

## Basic Rest API

```python
import requests

url = "https://api.chucknorris.io/jokes/random"

headers = {
	"accept": "application/json",
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

> Explore the output - find `value` - We will get that next

## Try to Get Cleaner Output

THIS ONE FAILS - SEE WHY!

```diff
  import requests

  url = "https://api.chucknorris.io/jokes/random"

  headers = {
    "accept": "application/json",
  }

  response = requests.request("GET", url, headers=headers)

  print(response.text)
+ print(response.text.get('value'))
```

#### FAILURE

```
Traceback (most recent call last):
  File "chucky.py", line 12, in <module>
    print(response.text.get('value'))
AttributeError: 'str' object has no attribute 'get'
```

## Silly Coder, We need JSON data, not Str

```diff
  import requests

  url = "https://api.chucknorris.io/jokes/random"

  headers = {
    "accept": "application/json",
  }

  response = requests.request("GET", url, headers=headers)

- print(response.text)
- print(response.text.get('value'))
+ print(response.json())
+ print(response.json().get('value'))
```

Huzzah!


## Even Better
```diff
  import requests

  url = "https://api.chucknorris.io/jokes/random"

  headers = {
    "accept": "application/json",
  }

- response = requests.request("GET", url, headers=headers)
+ response = requests.request("GET", url, headers=headers).json()

- print(response.json())
- print(response.json().get('values'))
+ print(response)
+ print(response.get('values'))
```
