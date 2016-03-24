# VPL
Auctioning System using flask and SocketIO

SocketIO is used for buzzer and for  to and fro communication between the buyers and the auctioneer ,

There are two tabs viz, myteam and home ,

The floating fab in the bottom corner of the home or the price below the icon can be used to bid by the buyer.

The auctioneer can choose pools and change the player up for auction .

Auctioneer can start aur pause bidding using the options provided. 

Alerts are displayed showing to whom the player is sold. 

The price of the player and the player is updated using socketIO on bids.

This project also uses Redis as a messaging queue for the SocketIO  requests.

SQLAlchemy 's engine is used to execute MySQL statements.


Url  :

/home  -- > Buyer home

/admin --> Admin home

/myteam --> Team of the buyer
