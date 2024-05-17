import argparse
import os
from watching import *

msg = "Checks to see which anime in your watchlist are being aired today."
parser = argparse.ArgumentParser(description=msg)

parser.add_argument("-a","--add",nargs="+",help="add series to watching list")
parser.add_argument("-d","--delete",nargs="+",help="remove series from watching list")
parser.add_argument("-ra","--removeAll",action="store_true",help="completly empty watchlist")
parser.add_argument("-ga","--getAiring",action="store_true",help="get list of anime in your watchlist aring today")

    
args = parser.parse_args()

if args.getAiring:
    from webScrape import airingToday
    listAiring(airingToday)
elif args.removeAll:
    removeAllWatchlist()
else:
    if args.add:
        addWatchList(args.add)
    if args.delete:
        deleteWatchlist(args.delete)
           
    displayWatchlist()   


