# Private Variables

verify - (0 = new; 1 = read the rules & signed the Terms of Service, 2 = gave cookies to unlock plot)
naughty - determines how heavy this players next auto-punishment will be
banReason - Index of reason
banDuration - Time to add to banTs
banTs - end of ban timestamp
Playtime - playtime in seconds
lock - 1 = Stop plot enter and home verify from using the plotData functions

err - boolean to tell if function exited with an error
x, y, z - used for /plot_home
homeVerifyCd - used to execute 'Home Verify' every x ticks (set to 0 to trigger instantly)

plot - number of the plot you are targeting
plotData - data of the plot you are targeting
plotTitle - 0 = show title of plot you are in; 1 = already shown
plot...

home - number of the plot you own
homeData - data of the plot you own
home...

inPlot - number of the plot you are in
inPlotData - data of the plot you are in
inPlot...
inPlotRow - used to check what plot you are in
inPlotCol - used to check what plot you are in
inPlotX - used to check if you are on the street
inPlotZ - used to check if you are on the street

## Minimap

region - selected region on the minimap (0-8)
oldRegion - Skip loading minimap if region remained the same (todo: add regionTs to check if it has been cached for 5+ minutes, then reset)
minimapLoad - Minimap is loading (progressbar ⬛)

menuPlot# - number of plot on item
menuPlot#...
menuPlot#h - hours until expire

## Private Command Variables

auto - what plotId /pauto will try to claim
nvn - if night vision is on
invis - if invisibility is on (staff only)

## Temporary Private Variables

packed - used to pack bitpacked stats like `plotData` without modifying its original value
unpacked - used to unpack bitpacked stats like `plotData` without modifying its original value
mask - used to help unpack bitpacked stats like `plotData`
unix - store %date.unix% for math ops

difference - used in @function modulo
delta - used to determine menuPlot1 from region x

cond# - used for more complex conditionals

# Public Variables

id - Player ID
UniquePlayers - #
CookieRecord - Highest ever amount of cookies on this housing

Claimed - total amount of plots currently claimed
Expired - total amount of plots that are expired
OwnerOnline - amount of plots who's owner is online

buffer - max offline hours
plotSize - 18 = (18x18)
plotGridSize - 9 = (9x9 plots each 22x22)
plotGapSize - 5
regionSize - 3 = (3x3)

!!! IMPORTANT !!! manually update when subvalues update OR update it when someone joins
plotPlusGapSize - 23 (18 + 5) Cache this value to improve performance and reduce script size

bcType - Broadcast Type
plot - Used in broadcast and `inPlotData verify`
banDuration - Used in staff broadcast

auto - The next plot /auto will try to claim

**NEW**
plot# - bitpacking: FEDCBBBBBBBBAAAAAA (1F 1E 1D 1C 8B 6A = 18/19 bits)
#: Plot number
A: plotId - Owner ID (max: 999.999)
B: plotUnix - Owner last online minute [%date.unix% / 60], inclusive (max: 99.999.999)

C: plotProtect - Wether the plot is protected from expiring (0 = No; 1 = Yes)
0: plotOn - Wether the owner is online (0 & 4 = No; 2 = Yes) (NOT STORED IN THE DATA, derived from plotUnix)
D: plotPublic - Wether visitors can build on this plot. (4 = No; 2 = Yes)
E: plotGm - Gamemode of visitors in the plot. (0 = Creative; 1 = Survival; 2 = Adventure)
F: plotPvP - Wether visitors can PvP. (4 = No; 0 & 2 = Yes)
