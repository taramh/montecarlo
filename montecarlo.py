import random
import pandas as pd

class Die:
    """
    A die has N sides/faces and W weights, and can be rolled to select a face. You can change the weight of a die, roll a die, or have it show its current faces and weights.
    """

    def __init__(self, faces):
        assert isinstance(faces, list), "Faces has to be a list"
        for fa in faces:
            accepted = ["<class 'int'>", "<class 'str'>", "<class 'float'>"]
            what = str(type(fa))
            if what in accepted:
                continue
            else:
                print("Objects in the faces list must be integers, floats, or strings. Please try again.")
        self.faces=list(set(faces))
        n = len(self.faces)
        self.weights = [1] * n
        self.die = pd.DataFrame({
            'face': self.faces,
            'weight': self.weights
        })

    def change_the_weight(self, facevalue, newWeight):
        '''Takes the face you want to change the weight for and the new weight and updates the Die.'''
        if facevalue in self.faces:
            try:
                newWeight = float(newWeight)
                indexofface = self.die[self.die['face'] == facevalue].index.values
                self.die.loc[indexofface,"weight"] = newWeight
                faceindex = self.faces.index(facevalue)
                self.weights[faceindex] = newWeight
            except ValueError as e:
                print("The new weight you wish to add to the die must be entered as an integer or float.")
        else:
            print("The face value you entered does not appear in your Die's faces.")

    def roll(self, times=1):
        '''Rolls the die and returns (but does not store) the results.'''
        return(random.choices(population=self.faces, weights=self.weights, k=times))

    def show(self):
        '''Shows the die's faces and weights as a data frame'''
        return(self.die)
        

class Game:
    """
    A game consists of rolling one or more dice of the same kind, one or more times. This class can play a game or show the results of the most recent play.
    """

    def __init__(self, dieList):
        self.dieObjects = dieList
    
    def play(self, times):
        '''Plays the game by rolling your list of dice as many times as you specify. Stores and returns the results.'''
        self.gameresults = pd.DataFrame()
        dicenumber = 1
        for m in self.dieObjects:
            mResults = m.roll(times=times)
            name = f"Die Number {dicenumber}"
            mSeries = pd.Series(mResults, name=name)
            mDF = pd.DataFrame(mSeries)
            if dicenumber == 1:
                self.gameresults = mDF
            else:
                self.gameresults = self.gameresults.join(mDF)
            dicenumber += 1
        self.gameresults.index = self.gameresults.index + 1
        self.gameresults.index.name = "Roll Number"
        return(self.gameresults)

    def show(self, format="wide"):
        '''Shows the game results as a narrow or wide data frame - defaults to wide.'''
        try:
            if format == "wide":
                return(self.gameresults)
            elif format == "narrow":
                return(self.gameresults.stack())
        except ValueError as e:
            print("The variable 'format' must be either 'wide' or 'narrow.'.")
    

class Analyzer:
    """
    An analyzer takes the results of a single game and computes various descriptive statistical properties about it. Attributes are: face_counts_per_roll, jackpots, rollcombinations.
    """

    def __init__(self, game):
        self.game = pd.DataFrame(game.show())

    def face_counts_per_roll(self):
        '''Returns and saves a frequence table for the roll results of your game, per roll.'''
        self.facefreq = (self.game.apply(pd.Series.value_counts, axis=1).fillna(0))
        return(self.facefreq)

    def jackpot(self):
        '''Stores a data frame of all jackpots (where every die rolled the same face) and which roll number they were. Returns only the number of jackpots.'''
        colnum = self.game.shape[1]
        self.face_counts_per_roll()
        hits = self.facefreq[self.facefreq.isin([colnum]).any(axis=1)]
        jacknum = hits.shape[0]
        self.jackpots = hits
        return(jacknum)
    
    def combinations(self):
        '''Computes all combinations of faces taht were rolled in a game, saves and returns a frequency table for these combinations.'''
        colnum = self.game.shape[1]
        self.rollcombinations = self.game.apply(lambda x : sorted(list(x.iloc[0:colnum])), axis=1).value_counts().to_frame('Frequency of Combination')
        return(self.rollcombinations)



