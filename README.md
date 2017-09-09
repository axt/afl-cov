# afl-cov

AFL fuzzing coverage CFG visualization 

The utility is based on [angr](https://github.com/angr/angr), [tracer](https://github.com/angr/tracer), [qemu](https://github.com/qemu/qemu), [bingraphvis](http://github.com/axt/bingraphvis/) and [cfg-explorer](http://github.com/axt/cfg-explorer/).

## Note

This project is in its very early stage!

## Usage
```
$ python -m aflcov /your/binary /path/to/afl/fuzz/queue -l
```
The command above will build the CFG, run the executable for each of the queue files through `qemu` to collect trace info, calculates the node coverage, and display it on the CFG.


## Limitations
*  see limitations of [cfg-explorer](https://github.com/axt/cfg-explorer)

## Screenshots

![scr1][scr1]
![scr2][scr2]


[scr1]: http://i.imgur.com/gqxvXS0.png
[scr2]: http://i.imgur.com/rTiXZgt.png



