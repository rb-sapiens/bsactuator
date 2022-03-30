# bsactuator

# install
```
pip install git+https://github.com/rb-sapiens/bsactuator.git
```

# initialization
```
import bsactuator
ba = bsactuator.BsActuator("/dev/tty.ACM0",115200)
```

# function list
## set_length(length, speed)
Stretch the aluminum tape to the specified length.

params
- length: Length of aluminum tape[mm] int, 0-150
- speed: Expansion and contraction speed, int, 1-10

example
```
ba.set_length(200, 5)   # Extend and retract at a rate of 5 to a position of 200 mm
```

## get_length()
Get the current length as an integer. Unit is mm.

example
```
ba.get_length()  # will return 200 for example
```

## hold()
The stepping motor is energized to fix the aluminum tape.

example
```
ba.hold()
```

## release()
Shut off the power to the stepping motor so that the aluminum tape can be moved.

example
```
ba.release()
```

## reset()
Return to the initial position (length 0mm) and return to the initial state.

example
```
ba.reset()
```
