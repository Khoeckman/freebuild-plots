# Freebuild Co-op plots

A Hypixel Housing project. By Khoeckman x Legendary Games.

## Flags

@global - Function is always executed for everyone
@auto <number> - Function runs every <number> ticks
@targeted - Command is in `Targeted` mode

@temp - List of temporary variables in the file which are not documented in this file
@create - Create the function, command, region, ... in Housing
@compile - Import the HTSL file into Housing

{varname} - Player variable
\#{varname} - Global variable
@{varname} - Team variable
Function{functionname} - Function

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
hasMultiple (1 | unset) - Whether it's possible that the player has multiple plots
cookiesTotal (byte) - Total amount of cookies the player has given this house all-time

playtime (int) - Milliseconds of playtime the player has
ptS
ptM
ptH

banSeconds (int) - Amount of seconds a player is soft-banned, -1 means based on {banCount}
banUnix (int | unset) [0] - Unix timestamp marking the end of the ban
banCount (byte) [0] - The amount of times the player got banned

unclaimCd (short | unset) [#{unclaimCd}] - Amount of seconds until a player can unclaim their home. Is set to #{unClaimCd} when claiming a plot
unclaimCdH (short | unset) - formatted hours
unclaimCdM (short | unset) - formatted minutes
unclaimCdS (short | unset) - formatted seconds
unclaimCdActive (&a | unset) [&7] - Color code based on whether the cooldown is active, lime for active, gray for inactive

resetCd (short | unset) [#{resetCd}] - Amount of seconds until a player can reset a plot. Is set to #{resetCd} when resetting a plot
HMS is hardcoded.

reportCd (short | unset) [#{reportCd}] - Amount of seconds until a player can report a player or plot again. Is set to #{reportCd} when reporting a player or plot
HMS is hardcoded.

nvn (1 | unset) [0] - Night vision
nvnStr (string) [&cDISABLED] - Used to display effect status in "Settings" menu
invis (1 | unset) [0] - Invisibility (Staff+ only)
invisStr (string) [&cDISABLED] - Used to display effect status in "Settings" menu

// Temporary plot data to work with or store in {in...} or {home...}
plotAddr (byte) [&cNone] - Plot register address of the current plot
plotId (short) - Owner Id
plotIgn (string) - Owner IGN
plotUnix (int) - Unix timestamp when the plot expires
plotExpr (int) - This needs to be recalculated every time it is used! Delta seconds of {plotUnix}. Negative number means the plot is expired. Positive represents the amount of seconds until it expires (ppcd-live)
plotSettings (byte) - (2 bits: AB) = (A: plotBuild, B: plotProtect) = (00-24) / compressed = (0-15)
plotBuild (byte) - (0, 1, 2) = (Private, Trusted, Public) - Who can build (bitpacked)
plotBuildStr (String) [&cNone] - Name of the build setting (ppcd)
plotProtect (byte) - (0, 1, 2, 3, 4) = (Off, Low, Medium, High, Extreme) - Protection level (bitpacked)
plotProtectStr (String) [&cNone] - Name of the protection setting (ppcd)
plotPermStr (string) [&e[STAFF]] - Required group tag to change the protection setting (ppcd)
plotOnline (byte) - (-1, 0, 1) = (Offline, Unknown, Online) - Is the owner of the plot online. When value is `unknown`: disallow claiming the plot and building (ppcd-async)
plotOnlineStr (string) - ('&7(&c&lOFFLINE&7) ', '&7(&c&lUNKNOWN&7) ', '&7(&a&lONLINE&7) ') - String version, paste ready for Function{Actionbar}
plotTrusted (1 | unset) - Are you trusted on this plot (ppcd-async)
plotPoints (short) [0 / '0.000'] - Total points of the plot
plotRated (short) - Total amount of players that rated the plot (all time)
plotRating (float) - plotPoints / plotRated (ppcd)

// Plot the player is in
inAddr (byte | unset)
oldInAddr (byte) - Set to {inAddr} when Function{Plot entry} downloads the data the plot the player is in
in... - Won't be shown if {inAddr} is not above 0

inSpawn (1 | unset) - Is 1 when the player is exactly on the spawn location.

// Plot the player has claimed as home
homeSyncQ (1 | unset) - Queue checking wether the player still owns {plotAddr}
homeAddr (byte | unset)
homePrefix (string | unset) [&c&oNone] - Text for before the index eg. "&a&oPlot &b&o#" (ppcd)
homeRated (byte) [0]
homeRating (float) [None]

// To /pcopy /ppaste the plot data, cb = clipboard
cbAddr
cb...

plotMenuQ (1 | unset) - Queue refreshing the `Plot menu` menu after updating a setting.
settingStr (string) - (Building, Protection) - Name of the setting that changes
selected (byte) - The value to be assigned to {plotSettings}
selectedStr (string) - The name of the value to be assigned to {plotSettings}
menuBuild0 (&eClick to select | unset) [&eClick to select] - Whether the plot build setting is: Private
menuBuild1 (&eClick to select | unset) [&eClick to select] - Whether the plot build setting is: Trusted
menuBuild2 (&eClick to select | unset) [&eClick to select] - Whether the plot build setting is: Public
menuProtect0 (&eClick to select | unset) [&eClick to select] - Whether the plot protected setting is: Off
menuProtect1 (&eClick to select | unset) [&eClick to select] - Whether the plot protected setting is: Low
menuProtect2 (&eClick to select | unset) [&eClick to select] - Whether the plot protected setting is: Medium
menuProtect3 (&eClick to select | unset) [&eClick to select] - Whether the plot protected setting is: High
menuProtect4 (&eClick to select | unset) [&eClick to select] - Whether the plot protected setting is: Extreme

trustAddr (byte) - Trust register address
trust#Id (short | unset) - Trusted ID (# = register 1 trough 5)
trust#Ign (string | unset) ['&cNone'] - Trusted IGN (# = register 1 trough 5)

points (byte) - Amount of points the player gave. To be added to {plotPoints}. {plotRated} increases with 1
ratingStr (string) - Name of the rating the player gave
ratedAddr (byte) - Register address of the {rated#} register of which it should read the bit at position {pointer}
pointer {byte} - The number of the bit it should read of the {ratedAddr} register
rated1 (long) - Register 1 to binairy bitpack whether the player has rated
rated (1 | unset) - Whether the player has already rated {plotAddr}

### Global

lockdown (byte) - (unset, 1, 2) = (Open, Close, Locked) - Prevent anyone (below staff) from building

reqId (id) - ID of event requestor (dispatch)
resId (id | unset) ['&cNone'] - ID of event responder (callback)
targetId (id) - ID of event target (handler)
targetAddr (byte) - {inAddr} of event target (handler)
targetPlotId (id) - {inId} of event target (handler)
targetHome (1 | unset) - Sync {homeAddr} of event target instead of {inAddr}

reqIgn (string) - IGN of event requestor (dispatch)
resIgn (string | unset) ['&cNone'] - IGN of event responder (callback)
targetIgn (string) - IGN of event target (handler)

reqX (float) - X-coord of the player
reqY (float) - Y-coord of the player
reqZ (float) - Z-coord of the player
minDist (float) - Distance to the nearest player

houseGroup (string) - Group tag (eg. "&4[OWNER]") of the player who joined or quit
houseGroupTag (string) - Group (eg. "Owner") of the player who joined or quit
houseVersion (string) - Minecraft Version of the player who joined or quit

cookieCurrent (short) - Total amount of weekly cookies the house received
cookieRecord (short) - Highest amount of weekly cookies the house received
cookieTotal (short) - Total amount of cookies the house received
cookies (byte) - Total amount of cookies the player just gave
cookiesTotal (byte) - Total amount of cookies the player has given this house all-time

unique (short) [0] - Unique amount of players on the house
auto (byte) - Plot address of the plot /pauto will try to claim

plotXZ (30)
plotGap (7)
plotXZPlusGap (37)

plotY (79)
plotGroundY (4)
plotYPlusGap (86)

plotGridSize (7)
plotLayerSize (49)

plotStartX (-128)
plotStartY (1)
plotStartZ (-113)
plotEndX (124)
plotEndY (254)
plotEndZ (139)

maxPlotAddr (147)
maxHomeAddr (147) (event: 49)
exprBuffer (600) - Amount of seconds being offline until another player can claim their plot.
exprBufferM (10) - Amount of minutes being offline until another player can claim their plot.

unclaimCd (1800) - The number of seconds a player must wait before they can unclaim a plot again
resetCd (600) - The number of seconds a player must wait before they can reset a plot again
reportCd (180) - The number of seconds a player must wait before they can report a player or plot again

plotSyncHyper (1 | unset) - Index of {Plot sync} function that should be used next. Rotate value around 0-1.
online (bool) - Is set to 0 before running Function{Player online} which sets it to 1 if the player with id #{target} is online
trusted (bool) - Whether the requesting player is trusted on plot #{plotAddr}

#### Menu analysis (todo)

mPlra (short) - Amount of clicks on "Menu: Plot rating"
mPlclRebuYes (short) - Amount of clicks on "Plot reset"
mPlclRebuNo (short) - Amount of clicks on "Plot reset"

#### Command analysis (todo)

cPclaim (short) - Use count of "/pclaim"

## Personal Notes

y=1.1x^{1.5}
x = minutes built on plot
y = minutes to keep plot after offline

### Discord invite link to LG

https://discord.gg/jFtGfAnY8P

### Mail

// @debug
chat "&c&lERROR &cYou cannot ... for an unknown reason. &7(Please report this error &e/mail&7)"
sound "Anvil Land" 0.3 1.0 invokers_location

### HMS

&a%var.player/h%h %var.player/m%m %var.player/s%s

### Emojis

⛃ ⚔ ✧ ✦ ❤ ⚡ ❈ 🗡 ✪ ➡ ⎜ ⬛
