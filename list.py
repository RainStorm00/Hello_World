Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 19 2015, 20:38:51) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
players = [11,22,33,44,55,66,77]
>>> players[2]
33
>>> players[2] = 66
>>> players
[11, 22, 66, 44, 55, 66, 77]
>>> players.append(120)
>>> players + [10,22,33,029,394]
SyntaxError: invalid token
>>> players + [32,432,3123]
[11, 22, 66, 44, 55, 66, 77, 120, 32, 432, 3123]
>>> players.append(120)
>>> players
[11, 22, 66, 44, 55, 66, 77, 120, 120]
>>> players[:2]
[11, 22]
>>> players[:2] = [33,123]
>>> players
[33, 123, 66, 44, 55, 66, 77, 120, 120]
>>> players[:2] = []
>>> players
[66, 44, 55, 66, 77, 120, 120]
>>> players[:] = []
>>> players
[]
>>> 
