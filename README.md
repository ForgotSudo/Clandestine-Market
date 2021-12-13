How to run the python file: 
First set up the bitmessage daemon by following the instructions here:
Build bitmessage from source "http://bitmsgdyvsmwgsimkxplisxbzpewvkhfm3fmomzd63apaymaxiznz6ad.onion/index.php/Compiling_instructions" or "https://wiki.bitmessage.org/index.php/Compiling_instructions". Set up the daemon by following these instructions "http://bitmsgdyvsmwgsimkxplisxbzpewvkhfm3fmomzd63apaymaxiznz6ad.onion/index.php/Daemon" or "https://wiki.bitmessage.org/index.php/Daemon". Set up the API in the keys.dat file
"http://bitmsgdyvsmwgsimkxplisxbzpewvkhfm3fmomzd63apaymaxiznz6ad.onion/index.php/API_Reference" or "https://wiki.bitmessage.org/index.php/API_Reference"

Next, change the username and password in the test file to the username and password that is used in the daemon. This will allow the api to connect to the daemon. Now you can run the test file. 

The test.py file is the basic lay out of the app so far. I would recommend familiarizing yourself with Bitmessage. Bitmessage is based on bitcoin but is meant for messaging rather than transfering currency. The idea of our project is to build on top of Bitmessage and use it as a communications layer. Specifically, we will use bitmessage's "chan" feature as our basis for each market. For example, when I add a new market, I will enter the bitmessage chan address. In the market there will be product listings and our app will scan the market to find said product listings. Product listings are simply the messages that merchants sent via bitmessage. In order for the app to scan the market for product listings, there has to be a specific format in which each listing will be made. An example would be like the following:

"

Product: "X"

Price: "5", "XMR"

Description: "Product X is the best..."

signing key: "..."

"

In the menu bar there will be a button for a user to create a product listing. When clicked, there will be a prompt that will ask for the products name, price, description, etc. After that is completed, the product can be sent to that market and be seen by other users.

Another feature that will be needed is the verification of pgp keys. With this feature, we could implement a system where customers can review the merchants. And to prevent review spamming, there could be a requirement that each customer has had to buy a product from that merchant. One way to go about this is every time a customer buys an item there is a confirmation message sent to the customer which contains a key that will be used to review that merchant.




The following are just general bullet points and potential features in the app
The first tab will automatically load the default market. This market will be used as a "trojan horse" to get the normal everyday user to use a private marketplace instead of what is currently being offered by privacy invasive comanies like google, amazon, and facebook.

In the second tab that is where one can search for a new "market" and get products that may not be sold on a different market. A usecase for this is if someone were to live in "Country A" but "Market B" isnt local to Country A. That person would just search for a market that is local to their country and use that market instead.

The menu bar on the left side is a work in progress but it will serve as a "bookmark" bar to store your saved markets (chans)





