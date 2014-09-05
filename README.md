autotweet_classifier.py
=======================

an attempt to detect automated tweets like "facebook photo sharings" within a users list of tweets. 
still very early dev phase. also, this is my first github contribution ;)

evaluating tweets mainly on basis of the frequency of words plus position. so if a word appears many
times at the same position, but rarely on different positions, then that is an indication for an
automated tweet.

use after import:
-"classify(listoftweets)"
-lscore threshold in function compare is adjustable.
