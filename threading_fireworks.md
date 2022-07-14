# Learning Threading with Fireworks

Make a simple flask server that takes in the name of the firework as long as the time it takes to go bang.

```python
from time import sleep
from flask import Flask

app = Flask(__name__)


@app.route("/<fw>/<bang_time>")
def launch(fw, bang_time):
    sleep(int(bang_time))
    return f"""

        .
      .' |
    .'   |
    /`-._'
   /   /
  /   /
 /   /
(`-./
 )

{fw} launched!
"""


if __name__ == "__main__":
    app.run(port=1776)
```


Next, create our old, slow way to get these fireworks.

```python
import time
import requests


fireworks = [
    ("Roman Candle", 1),
    ("Report", 3),
    ("Peony", 4),
    ("Palm Tree", 3),
    ("Pistil", 5),
]


def launch_firework(firework):
    print(f"launching a {firework[0]}!")
    return requests.get(f"http://0.0.0.0:1776/{firework[0]}/{firework[1]}")


start = time.time()

processes = []

print("Starting the fireworks show!")
for fw in fireworks:
    print(launch_firework(fw).text)


# display the total run time
print(f'Time taken: {time.time() - start}')
```

In one tmux tab, start the flask server.

In another tmux tab, run your slow fireworks script. Should take about 15-16 seconds.


Now let's make a faster way!

```python
#!/usr/bin/python3
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests


fireworks = [
    ("Roman Candle", 1),
    ("Report", 3),
    ("Peony", 4),
    ("Palm Tree", 3),
    ("Pistil", 5),
]


def launch_firework(firework):
    print(f"launching a {firework[0]}!")
    return requests.get(f"http://0.0.0.0:1776/{firework[0]}/{firework[1]}")


start = time.time()

processes = []

# we want to be careful with the number of workers
# if you are making thousands of requests, does your target have limiting engaged?
# beware you don't overload internal or external services; 5 to 10 is fine for most scripts
print("Starting the fireworks show!")
with ThreadPoolExecutor(max_workers=5) as executor:
    for fw in fireworks:
        processes.append(executor.submit(launch_firework, fw))   # add a new task to the threadpool and store in processes list


    for task in as_completed(processes):    # yields the items in processes as they complete (it finished or was canceled)
        print(task.result().text)

# display the total run time
print(f'Time taken: {time.time() - start}')
```

Run the faster code! It should only take about 5 seconds this time!

