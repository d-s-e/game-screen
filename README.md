# GameScreen

`GameScreen` is a simple Flask based application to shine some coordinated
light onto a game board.

It was made primarily for the boardgame "Nemesis Lockdown".
Depending on the power situation during the game, some corridors and rooms
are lit and some are dark. With `GameScreen` it is possible to visualize
this dynamically, to hopefully not forget the light situation again.

To use it, you have to place a projector over your boardgame table facing
down, which should display a fullscreen web browser showing
`http://127.0.0.1:5000/projector/`. 

The lights can be controlled with another browser pointing at
`http://127.0.0.1:5000/control/`.

The most difficult part is the exact placement of the projector over the
game board.
