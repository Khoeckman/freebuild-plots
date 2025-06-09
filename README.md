# Freebuild Co-op plots

A Hypixel Housing project. By Khoeckman x LG.

y=1.1x^{1.5}
x = minutes built on plot
y = minutes to keep plot after offline

## Variables

**Syntax:**

name (type) [fallback value] - Description (ppcd = Post-processed)

### Player

id (number) - Id of the player, mainly used to check if they are new. Might be used in the future.
cd (bool) - Check if a function is on cd by setting to 1 and calling a function which should set it back to 0. And checking if its 0 after

plotAddr (byte) - Plot register address of the downloaded plot
plotPrefix (string) - Text for before the index eg. "&a&oPlot &b&o#" (ppcd)
plotIgn (string) - Owner IGN
plotUnix (number) - Unix timestamp of the last moment the owner was online
plotProtect (byte) - 1, 2, 3, 4, 5
plotProtectStr (String) [&cNone] - Name of the protection setting (ppcd)
plotBuild (byte) - 1, 2, 3
plotBuildStr (String) [&cNone] - Name of the build setting (ppcd)
plotTrusted (bool) - Are you trusted on this plot (async)
plotRatingScore (number) - Total score of the plot
plotRatingCount (byte) - Total amount of players that scored te plot
plotRating (float) - Weighted average of the score (ppcd)

// Plot the player is in
inPlot...
inPlotPrefix (string) [&e&oPublic]

// Home of the player
home...
homePrefix (string) [&c&oNone]

trustAddr (byte) - Trust register address
trust#Ign (string) ['&cNone'] - Trusted IGN (# = register 1 trough 7)

### Public

req (string) - IGN of event requestor (dispatch)
res (string) ['&cNone'] - IGN of event responder (callback)
target (string) - IGN of event target (handler)

houseGroup (string) - Group of the player who joined or quit
houseIgn (string) - IGN of the player who joined or quit
houseVersion (string) - Minecraft Version of the player who joined or quit

trustX (float) - X-coord of the player
trustY (float) - Y-coord of the player
trustZ (float) - Z-coord of the player
trustNearest (float) - Distance to the nearest player
