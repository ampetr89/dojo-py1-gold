# Ninja-Gold game

In this game you can go to different places to try to earn gold. You are guaranteed to earn something at all of the places except the casino, which may earn you a lot more, but you also may lose gold. Your earnings are tracked in the log panel on the right side of the screen, and a running total of your gold is kept on the top. You can refresh or even close the page and you will not lose your game. You can restart the game by pressing the restart button. 

The game is built using Flask + Ajax, so when you enter a location, the request is routed using Flask, but via an Ajax query which means the page doesn't have to refresh. Since we would expect people to be entering a lot of locations, it would quickly become annoying to have the page refresh each time. After entering a location, the log is appended to using jQuery, and it only adds the most recent activity. If the user refreshes the page, then it recreates the entire list. Note, after each entry is added, the log automatically scrolls to the bottom. 

### Screenshot
![Ninja-Gold game](/doc/screenshot.png "Screenshot")
