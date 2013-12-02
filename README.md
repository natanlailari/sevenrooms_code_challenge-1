SevenRooms Coding Challenge
=========

###Version 1.0

##**A simple game of ping pong**
---

The challenge is to simulate play-by-play games of ping pong between two players in a system of three players, and draw conclusions about the players. This is a stochastic problem in which each player has a set probability of success depending on the pseudo-randomly generated behavior of the other player. 

You do not need to be familiar with the game of ping pong (a.k.a table tennis) to solve this question, but if any of the terminology is confusing, please feel free to reference it on [Wikipedia](http://en.wikipedia.org/wiki/Table_tennis).

We definitely appreciate <i>(and hope you do as well)</i> well-organized elegant and efficient code and a demonstrated ability to follow directions.



###Rules of this game:
 - Play starts when the ball is served by one player and then returned by the other player; play continues in a turn-based fashion until one player fails to return the ball on his turn.
 - If one player fails to return the ball on his turn, the other player will win one point and the play for that point is over.
 - Each player takes turns serving the ball every 5 points, so if player 1 serves for the first five points, player 2 will serve for the next five points regardless of who wins the points.
 - The winner of a game is the player that is the first to score 21 points.


###Assumptions:
  -Each player's ability is based on probability of returning the ball. A 30% chance of returning a ball means there is a 70% chance of not returning and therefore the player's opponent winning the point.

  - There are four different shot types:
    - flat
    - slice
    - topspin
    - unreturnable

  - On return of a serve, after probability determines that the player returned the ball sucessfully, there is an additional 10% chance that they failed to return it.
  - If a shot is unreturnable, the probability of returning that shot is automatically 0.0%


##Data:
###Players:
####Player 1 - <i>Bruce Leeds</i>
  - Probability of shot type:
    - 47% flat
    - 25% slice
    - 25% topspin
    - 3% unreturnable
  - Probability of returning a shot
    - 80% flat
    - 45% slice
    - 75% topspin

####Player 2 - <i>Serena Williamson</i>
  - Probability of shot type:
    - 10% flat
    - 20% slice
    - 66% topspin
    - 4% unreturnable
  - Probability of returning a shot :
    - 65% flat
    - 50% slice
    - 85% topspin

####Player 3 - <i>Jean Claude Van Dime</i>
  - Probability of shot type:
    - 70% flat
    - 10% slice
    - 15% topspin
    - 5% unreturnable
  - Probability of returning a shot:
    - 90% flat
    - 25% slice
    - 85% topspin

##Sample Output
You can come up with your own human-readable representation of the play-by-play which may help with organization in analyzing the results.

    The score is now Bruce Leeds: 0, Serena Williamson: 0
    Bruce Leeds served to Serena Williamson.
    Serena Williamson successfully hit a topspin return.
    Bruce Leeds successfully hit an unreturnable return.
    Serena Williamson was unable to return, Bruce Leeds scores a point!
    The score is now Bruce Leeds: 1, Serena Williamson: 0
    ...


##Questions to answer
<ol>
    <li>In our system of three players, who wins the most? Explain why you made this conclusion.</li>
    <li>After how many samples were you able to confidently make this determination?</li>
</ol>

##Submitting your solution:
Please email us a link to your solution and answers on Github to team@sevenrooms.com with the subject: "A simple game of ping pong" along with your name, and a cover letter if you want to include one, and any other information you'd like us to know about you or your solution.

Thank you for your interest in [Seven Rooms](http://www.sevenrooms.com). We look forward to speaking with you soon!
