# ProgressBar
A Python Progress Bar Implementation


## Implementation
* ProgressBar() takes the number of iterations that will occur as well as the size of the progress bar
* ```bar = ProgressBar(iterations, bar_size)```
* After each bit of processing call ```bar.progress()```

```
from progress_bar import ProgressBar


def main():
  bar = ProgressBar(50, None)
  for i in range(0,50):
    # do some processing here
    bar.progress()
    

if __name__ == '__main__':
  main()
```
