"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact
import sys
from random import *

DEBUG = 0

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** REPLACE THIS LINE ***"
    res = [dice() for i in range(0, num_rolls)]
    if (1 in res): return 1
    return sum(res)
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    "*** REPLACE THIS LINE ***"
    max_dig = 0
    while (opponent_score):
        max_dig = max(max_dig, opponent_score % 10)
        opponent_score //= 10
    return max_dig + 1
    # END PROBLEM 2


# Write your prime functions here!
def is_prime(x):
    if (x <= 1): return False
    for i in range(2, x):
        if (x % i == 0): return False
    return True

def next_prime(x):
    x += 1
    while (not is_prime(x)):
        x += 1
    return x

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** REPLACE THIS LINE ***"
    score = 0
    if (num_rolls == 0): score = free_bacon(opponent_score)
    else: score = roll_dice(num_rolls, dice)
    if (is_prime(score)):
        score = next_prime(score)
    return score
    # END PROBLEM 2

def dfs(c, d, s, dice):
    if (c == d):
        r = sum(s)
        if 1 in s:
            r = 1
        elif is_prime(r):
            r = next_prime(r)
            
        return r, 1
    x, y = 0, 0
    for i in range(dice):
        tx, ty = dfs(c+1, d, s + [i+1], dice)
        x += tx
        y += ty

    return x, y


def get_exp():
    exp_six, exp_four = [], []
    for i in range(11):
        x, y = dfs(0, i, [], 6)
        exp_six += [x/y]
        x, y = dfs(0, i, [], 4)
        exp_four += [x/y]
        print(i)

    print(exp_six)
    print(exp_four)

def select_dice(dice_swapped):
    """Return a six-sided dice unless four-sided dice have been swapped in due
    to Perfect Piggy. DICE_SWAPPED is True if and only if four-sided dice are in
    play.
    """
    # BEGIN PROBLEM 3
    "*** REPLACE THIS LINE ***"
    return four_sided if dice_swapped else six_sided  # Replace this statement
    # END PROBLEM 3


# Write additional helper functions here!


def is_perfect_piggy(turn_score):
    """Returns whether the Perfect Piggy dice-swapping rule should occur."""
    # BEGIN PROBLEM 4
    "*** REPLACE THIS LINE ***"
    Sqrt = int(pow(turn_score, 1/2))
    Curt = int(pow(turn_score, 1/3))
    return (turn_score != 1 and (Sqrt ** 2 == turn_score or Curt ** 3 == turn_score))    
    # END PROBLEM 4


def is_swap(score0, score1):
    """Returns whether one of the scores is double the other."""
    # BEGIN PROBLEM 5
    "*** REPLACE THIS LINE ***"
    return score0 == score1 * 2 or score1 == score0 * 2
    # END PROBLEM 5


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player

Dice_swapped = False
def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0:     The starting score for Player 0
    score1:     The starting score for Player 1
    """
    global Dice_swapped
    
    # score0, score1 = randint(50, 60), randint(50, 60)
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False # Whether 4-sided dice have been swapped for 6-sided
    
    # BEGIN PROBLEM 6
    "*** REPLACE THIS LINE ***"
    while (max(score0, score1) < goal):
        
        if (player == 1):
            strategy1, strategy0 = strategy0, strategy1
            score0, score1 = score1, score0


        num_rolls = strategy0(score0, score1)
        if DEBUG:
            print("num_rolls = {0}".format(num_rolls))

        turn_score = take_turn(num_rolls, score1, select_dice(dice_swapped))
        dice_swapped ^= is_perfect_piggy(turn_score)

        score0 += turn_score
        Dice_swapped = dice_swapped
        if (is_swap(score0, score1)): score0, score1 = score1, score0
                
        if (player == 1):
            strategy1, strategy0 = strategy0, strategy1
            score0, score1 = score1, score0
            
        if DEBUG:
            print("my score is {0}, opponent_score is {1}".format(score0, score1))
            if (dice_swapped):
                print("Yes", file=sys.stderr)
            else:
                print("No", file=sys.stderr)
                
        player = other(player)

    # END PROBLEM 6

    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the strategy
    returns a valid input. Use `check_strategy_roll` to raise an error with a
    helpful message if the strategy returns an invalid output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 7
    "*** REPLACE THIS LINE ***"
    for x in range(goal):
        for y in range(goal):
            ret = strategy(x, y)
            if (type(ret) != int or ret > 10 or ret < 0):
                return check_strategy_roll(x, y, ret)
    # END PROBLEM 7
    
# Experiments

def make_averaged(fn, num_samples=10000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** REPLACE THIS LINE ***"
    def apply(*args):
        tot = 0
        for i in range(num_samples):
            tmp = fn(*args)
            tot += tmp
            #print(i, file=sys.stderr)
        return tot / num_samples

    return apply
    # END PROBLEM 8

def make_median(fn, num_samples=1000):
    def apply(*args):
        tot = [fn(*args) for i in range(num_samples)]
        tot.sort()
        #print(tot)
        return tot[len(tot) // 2]
    return apply
        
def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** REPLACE THIS LINE ***"
    maxV, maxI = 0.0, 0
    for i in range(1, 11):
        v = make_averaged(roll_dice, num_samples)(i, dice)
        if (v > maxV):
            maxV, maxI = v, i
    return maxI
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if DEBUG:
        print("my score is {0}, opponent_score is {1}\n\n\n".format(score0, score1))
        a = input()
        
    if score0 > score1:
        return 0
    else:
        return 1

    

def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test always_roll(8)
        print('always_roll(4) win rate:', average_win_rate(always_roll(4)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))
        
    if True:  # Change to True to test swap_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    "*** REPLACE THIS LINE ***"
    fb = take_turn(0, opponent_score)
    return num_rolls if fb < margin else 0
    # END PROBLEM 10
    
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    fb = take_turn(0, opponent_score)
    if ((score + fb) * 2 == opponent_score or fb >= margin):
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 11
check_strategy(swap_strategy)


history = []
opponent_history = []

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    # global history, opponent_history
    # history += [score]
    # if (opponent_score != 0): opponent_score = [0]
    # opponent_history += [opponent_score]
    
    #return always_roll(4)(score, opponent_score)
    #return swap_strategy(score, opponent_score)

    global Dice_swapped
    margin, num_rolls = 8, 4
    if (Dice_swapped): margin, num_rolls = 4, 3
    

    if (len(history) > 2 and history[-1] == history[-2] + 1 and history[-3] == history[-2] + 1):
        num_rolls -= 2
        
    if (score - opponent_score > 10):
        margin, num_rolls = 8-2*(score-opponent_score)//10, 3
    if (opponent_score - score > 10):
        num_rolls += (opponent_score - score) // 15
    fb = take_turn(0, opponent_score)

    if DEBUG:
        print("What the fuck of {0}".format(Dice_swapped))

    if (not Dice_swapped and is_perfect_piggy(fb)):
        return 0
    if (Dice_swapped and is_perfect_piggy(fb)):
        margin = 100000
    if ((score + 1) == opponent_score * 2):
        return 0
    if ((score + 1) * 2 == opponent_score):
        return 10
    
    if (opponent_score > GOAL_SCORE - 10 and score + fb< GOAL_SCORE):
        if (Dice_swapped):
            if (margin != 100000):
                return 0
            else:
                return 3
        else:
            return 5
        
    if ((score + fb) == opponent_score * 2):
        return num_rolls
    if ((score + fb) * 2 == opponent_score or fb >= margin):
        return 0

    return num_rolls

    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
  
