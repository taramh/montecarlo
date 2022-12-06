# montecarlo
A Monte Carlo Simulator by Tara Haas

## Snynopsis

You can install this code by doing:

```
pip install montecarlo
```

There are three classes: `Die`, `Game`, and `Analyzer`.

You create a `Die` by passing in a list of unique faces. Faces can be integers, floats, or strings.

For example:

```
firstDie = Die(faces=[1,2,3.5,"heads","tails"])
```

A Game is initiated with a die List, a list of Die to play with. You can use a die more than once if you want to play with multiples.

```
firstGame = Game(dieList=[firstDie,firstDie,firstDie])
```

After you play a game, `firstGame.play(times=n)`, you can then use an Analyzer to provdie insights on the game results. An Analyzer takes one Game as an input upon initializing.

```
firstAnalyzer = Analyzer(firstGame)
```

## API Description


