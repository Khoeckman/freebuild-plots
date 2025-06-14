# Freebuild Co-op plots

A Hypixel Housing project. By Khoeckman x Legendary Games.

## Todo

Plot sync was deleted, make sure every use is recompiled

## Flags

@global - Function is always executed for everyone

@temp - List of temporary variables in the file which are not documented in this file
@create - Create the function, command, region, ... in Housing
@compile - Import the HTSL file into Housing

{varname} - Player variable
\#{varname} - Global variable
@{varname} - Team variable
Func{functionname} - Function

## Params

Input - var (temp) globalvar (#temp) teamvar (@temp)
Output - var (temp) globalvar (#temp) teamvar (@temp)

Event input - Received from {req}
Event output - Sent to {target}

## Variables

**Syntax:**

name (TypeScript style types) [fallback value] - Description
ppcd = Post-processed

### Player

id (number) - Id of the player, mainly used to check if they are new. Might be used in the future
cd (bool) - Check if a function is on cd by setting to 0 and calling a function which should set it to 1. And checking if its 1 after
permission (byte) - Permission level of the player used to compare against the protection level of a plot
rated (byte) [0] - The amount of plots a player rated this hour, may not exceed #{maxRated}
banTs (int | unset) [0] - Unix timestamp marking the end of the ban
unclaimCd (short) [1800] - Amount of seconds until a player can unclaim their home. Is set to #{unClaimCd} when claiming a plot
groupStr (string) - Stored group tag for chat feedback

nvn (1 | unset) [0] - Night vision
nvnStr (string) [&cDISABLED] - Used to display effect status in "Profile" menu
invis (1 | unset) [0] - Invisibility (LG+ only)
invisStr (string) [&cDISABLED] - Used to display effect status in "Profile" menu

// Temporary plot data to work with or store in {in...} or {home...}
plotAddr (byte) - Plot register address of the current plot
plotId (short) - Owner Id
plotIgn (string) - Owner IGN
plotUnix (int) - Unix timestamp when the plot expires
plotSettings (byte) - (2 bits: AB) = (A: plotBuild, B: plotProtect) = (00-24) / compressed = (0-15)
plotBuild (byte) - (0, 1, 2) = (Private, Trusted, Public) - Who can build (bitpacked)
plotBuildStr (String) [&cNone] - Name of the build setting (ppcd)
plotProtect (byte) - (0, 1, 2, 3, 4) = (Off, Low, Medium, High, Extreme) - Protection level (bitpacked)
plotProtectStr (String) [&cNone] - Name of the protection setting (ppcd)
plotPermStr (string) [&e[STAFF]] - Required group tag to change the protection setting (ppcd)
plotOnline (bool) - (0, 1) = (Offline, Online) - Wether the owner of the plot is online (ppcd-async)
plotTrusted (bool) - (0, 1) = (No, Yes) - Are you trusted on this plot (ppcd-async)
plotPoints (short) [0] - Total points of the plot
plotRated (short) - Total amount of players that rated the plot (all time)
plotRating (float) - plotPoints / plotRated (ppcd)

// Plot the player is in
inAddr (byte | unset)
oldInAddr (byte) - Set to {inAddr} when Func{Plot entry} downloads the data the plot the player is in
in... - Won't be shown if {inAddr} is not above 0

// Plot the player has claimed as home
homeAddr (byte | unset)
homePrefix (string | unset) [&c&oNone] - Text for before the index eg. "&a&oPlot &b&o#" (ppcd)
homeShield (number) [0] - Seconds until home is claimable
homePoints (number)
homeRated (byte) [0]
homeRating (float) ['0.000']

settingStr (string) - (Building, Protection) - Name of the setting that changes
selected (byte) - The value to be assigned to {setting}
selectedStr (string) - The name of the value to be assigned to {setting}

trustAddr (byte) - Trust register address
trust#Id (short | unset) - Trusted ID (# = register 1 trough 5)
trust#Ign (string | unset) ['&cNone'] - Trusted IGN (# = register 1 trough 5)

### Global

reqId (id) - ID of event requestor (dispatch)
resId (id | unset) ['&cNone'] - ID of event responder (callback)
targetId (id) - ID of event target (handler)

reqIgn (string) - IGN of event requestor (dispatch)
resIgn (string | unset) ['&cNone'] - IGN of event responder (callback)
targetIgn (string) - IGN of event target (handler)

reqX (float) - X-coord of the player
reqY (float) - Y-coord of the player
reqZ (float) - Z-coord of the player
minDist (float) - Distance to the nearest player

houseGroup (string) - Group of the player who joined or quit
houseVersion (string) - Minecraft Version of the player who joined or quit

cookieRecord (short) - highest amount of weekly cookies on the house
unique (short) [0] - Unique amount of players on the house
auto (byte) - Plot address of the plot /pauto will try to claim

plotXZ (30)
plotGap (7)
plotXZPlusGap (37)
plotY (78)
plotYPlusGap (86)
plotStartX (-128)
plotStartY (1)
plotStartZ (-113)
plotEndX (124)
plotEndY (254)
plotEndZ (139)

maxPlotAddr (98)
exprBuffer (600) - Amount of seconds until a player can claim another (offline) player's plot.
maxRated (10) - The amount of plots players can rate per hour

plotSyncHyper (1 | unset) - Index of {Plot sync} function that should be used next. Rotate value around 0-1.
unclaimCd (short) - The number of seconds a player must wait before they can unclaim a plot again
online (bool) - Is set to 0 before running Func{Player online} which sets it to 1 if the player with id #{target} is online
trusted (bool) - Whether the requesting player is trusted on plot #{plotAddr}

#### Menu analysis (todo)

m_plra (short) - Amount of clicks on "Menu: Plot rating"

#### Command analysis (todo)

c_pclaim (short) - Use count of "/pclaim"

## Personal Notes

y=1.1x^{1.5}
x = minutes built on plot
y = minutes to keep plot after offline

### Mail

// @debug
chat "&c&lERROR &cYou cannot ... for an unknown reason. &7(Please report this error &e/mail&7)"
sound "Anvil Land" 0.3 1.0 invokers_location

### HMS

&a%var.player/h%h %var.player/m%m %var.player/s%s

### Emojis

⛃ ⚔ ✧ ✦ ❤ ⚡ ❈ 🗡 ✪ ➡ ⎜ ⬛
