# Freebuild Co-op plots

A Hypixel Housing project. By Khoeckman x Legendary Games.

## Flags

@global - Function is global and meant for all players
@target one - Function is global but only meant for one player, determined by #`target`
@target many - Function is global but only meant for certain players

@temp - Temporary variables which are not documented in this file
@create - Create this function, command, region, ... in Housing
@compile - Import this HTSL code into Housing

`varname` - Player variable
\#`varname` - Global variable
@`varname` - Team variable
Func`functionname` - Function

## Params

Input - var (temp) globalvar (#temp) teamvar (@temp)
Output - var (temp) globalvar (#temp) teamvar (@temp)

Event input - Received from `req`
Event output - Sent to `target`

## Variables

**Syntax:**

name (TypeScript style types) [fallback value] - Description
ppcd = Post-processed

### Player

id (number) - Id of the player, mainly used to check if they are new. Might be used in the future
cd (bool) - Check if a function is on cd by setting to 0 and calling a function which should set it to 1. And checking if its 1 after
rated (byte) [0] - The amount of plots a player rated this hour, may not exceed #`maxRated`
banTs (int | unset) [0] - Unix timestamp marking the end of the ban
unclaimCd (short) [1800] - Amount of seconds until a player can unclaim their home. Is set to #`unClaimCd` when claiming a plot

nvn (1 | unset) [0] - Night vision
nvnStr (string) [&cDISABLED] - Used to display effect status in "Profile" menu
invis (1 | unset) [0] - Invisibility (LG+ only)
invisStr (string) [&cDISABLED] - Used to display effect status in "Profile" menu

// Temporary plot data to work with or store in `in...` or `home...`
plotAddr (byte) - Plot register address of the current plot
plotId (short) - Owner Id
plotIgn (string) - Owner IGN
plotUnix (int) - Unix timestamp when the plot expires
plotSettings (byte) - (3 bits: ABC) = (A: plotOnline, B: plotBuild, C: plotProtect) = (000-124) / compressed = (00-30)
plotOnline (byte) - (0, 1) = (Offline, Online) - Wether the owner of the plot is online (bitpacked)
plotBuild (byte) - (0, 1, 2) = (Private, Trusted, Public) - Who can build (bitpacked)
plotBuildStr (String) [&cNone] - Name of the build setting (ppcd)
plotProtect (byte) - (0, 1, 2, 3, 4) = (Off, Low, Medium, High, Extreme) - Protection level (bitpacked)
plotProtectStr (String) [&cNone] - Name of the protection setting (ppcd)
plotTrusted (bool) - (0, 1) = (No, Yes) - Are you trusted on this plot (ppcd-async)
plotPoints (short) [0] - Total points of the plot
plotRated (short) - Total amount of players that rated the plot (all time)
plotRating (float) - plotPoints / plotRated (ppcd)

// Plot the player is in
inAddr (byte | unset)
oldInAddr (byte) - Set to `inAddr` when Func`Plot entry` downloads the data the plot the player is in
in... - Won't be shown if `inAddr` is not above 0

// Plot the player has claimed as home
homeAddr (byte | unset)
homePrefix (string | unset) [&c&oNone] - Text for before the index eg. "&a&oPlot &b&o#" (ppcd)
homeShield (number) [0] - Seconds until home is claimable
homePoints (number)
homeRated (byte) [0]
homeRating (float) ['0.000']

trustAddr (byte) - Trust register address
trust#Ign (string | unset) ['&cNone'] - Trusted IGN (# = register 1 trough 7)

### Global

req (string | id) - IGN or ID of event requestor (dispatch)
res (string | id | unset) ['&cNone'] - IGN or ID of event responder (callback)
target (string | id) - IGN or ID of event target (handler)

houseGroup (string) - Group of the player who joined or quit
houseVersion (string) - Minecraft Version of the player who joined or quit

cookieRecord (short) - highest amount of weekly cookies on the house
unique (short) [0] - Unique amount of players on the house

plotXZ (30)
plotGap (7)
plotXZPlusGap (37)
plotY (?)
plotYPlusGap (?)
plotStartX (-128)
plotStartY (1)
plotStartZ (-113)
plotEndX (124)
plotEndY (254)
plotEndZ (139)

exprBuffer (600) - Amount of seconds until a player can claim another (offline) player's plot.

unclaimCd (short) - The number of seconds a player must wait before they can unclaim a plot again
maxRated (10) - The amount of plots a player can rate per hour

trustX (float) - X-coord of the player
trustY (float) - Y-coord of the player
trustZ (float) - Z-coord of the player
trustNearest (float) - Distance to the nearest player
trusted (bool) - Whether the requesting player is trusted on plot #`plotAddr`

#### Menu analysis (todo)

m_plra (short) - Amount of clicks on "Menu: Plot rating"

#### Command analysis (todo)

c_pclaim (short) - Use count of "/pclaim"

## Personal Notes

y=1.1x^{1.5}
x = minutes built on plot
y = minutes to keep plot after offline

### HMS

&a%var.player/h%h %var.player/m%m %var.player/s%s

### Emojis

⛃ ⚔ ✧ ✦ ❤ ⚡ ❈ 🗡 ✪ ➡ ⎜ ⬛
