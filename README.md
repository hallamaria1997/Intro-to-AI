# Taiji

## Installing 
Install the requirements by running the command

``pip install -r requirements.txt``

The most important thing is that the version of the ``pygame`` package has to be ``2.1.2``.

## Running
Start the game by running the command ``python game.py 1`` if you want to play the game against the computer, or ``python game.py 2`` if you want to have two computer agents play against each other. The game is best played on a screen of size of more than 900x900px (unzoomed).

## Rules
The human player always starts, and he has the colour blue, and the computer has white. The players take turns laying down tiles with one white half and one blue half, and try to make as long paths as they can of their colour. The game ends when there are no spaces left to place a tile. The lengths of the players' two longest paths are then added together, and the player with the higher sum wins. In case of a draw, the player who went second - in this case, that is always the computer - wins.

## Gameplay
To place a tile, first click on the desired alignment on the left side. Then place it by clicking on its place on the grid. Click on the grid cell where you want the *upper* half of the tile to be placed if you chose a vertical alignment, and click the cell where the *left* half should be placed if you picked a horizontal alignment. 

The tile isn't drawn on the board until the agent has figured out its move and placed its tile. This can take a few seconds, so it is important to wait even though the tile isn't visible on the board immediately after the click.
