# montecarlo
A Monte Carlo Simulator by Tara Haas

## Snynopsis

### Installation

1. Clone the GIT repo:

```
git clone https://github.com/taramh/montecarlo.git
```
2. Install the montecarlo package:

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

### Die Class

Doc String: A die has N sides/faces and W weights, and can be rolled to select a face. You can change the weight of a die, roll a die, or have it show its current faces and weights.

Attributes:
* self.weights: a list of weights for each face of a Die, defaults to 1.0
* self.faces: the list of faces for a Die, each one is either a string, an integer, or a float

Methods:
* change_the_weight(facevalue, newWeight): Takes the face you want to change the weight for and the new weight and updates the Die.
  * facevalue: a face on a Die that is already initialized
  * newWeight: the new weight you'd like assigned to that face (all Die begin with weights of 1.0 for each face)
* roll(times=1): Rolls the die and returns (but does not store) the results.
  * times: defaults to 1, this is how many times you want the Die to be rolled
* show(): Shows the die's faces and weights as a data frame.


### Game Class

Doc String: A game consists of rolling one or more dice of the same kind, one or more times. This class can play a game or show the results of the most recent play.

Methods:
* play(times): Plays the game by rolling your list of dice as many times as you specify. Stores and returns the results as a data frame.
  * times: how many times you want your Die list to be rolled for one game, this is an integer or a float
* show(format="wide"): Shows the game results as a narrow or wide data frame - defaults to wide.
  * format: Shows, in the form of a data frame, the results of the most recent game played. Defaults to "wide" but if a user enters "narrow" then the results will be a narrow data frame.


### Analyzer Game

Doc String: An analyzer takes the results of a single game and computes various descriptive statistical properties about it.

Attributes:
* 

