from math import ceil

output_file = "output.htsl"
plots_per_function = 24
plots = 7*7*3
functions = ceil(plots / plots_per_function)


def nested_loop(funcIdx):
    global plotIdx

    for i in range(1, plots_per_function + 1 + int(funcIdx == functions)):
        plotIdx += 1

        if plotIdx > plots:
            return

        file.write(f'if (var plotAddr == {plotIdx}) {{\n')
        file.write(f'  var plotId = globalvar p{plotIdx}Id\n')
        file.write(f'  var plotIgn = globalvar p{plotIdx}Ign\n')
        file.write(f'  var plotUnix = globalvar p{plotIdx}Unix\n')
        file.write(f'  var plotSettings = globalvar p{plotIdx}Settings\n')
        file.write(f'  var plotPoints = globalvar p{plotIdx}Points\n')
        file.write(f'  var plotRated = globalvar p{plotIdx}Rated\n')
        file.write(f'  exit\n')
        file.write(f'}}\n')


with open(output_file, "w") as file:
    # Step 1: Create all functions
    for funcIdx in range(1, functions + 1):
        if funcIdx == 1:
            file.write(f'goto function "Plot download"\n')
        else:
            file.write(f'goto function "Plot download {funcIdx}"\n')

    file.write('\n')

    # Step 2
    plotIdx = 0

    for funcIdx in range(1, functions + 1):
        if funcIdx == 1:
            file.write(f'goto function "Plot download"\n\n')
            file.write(f'var cd = 1\n')
            file.write(f'var plotId unset\n\n')
        else:
            file.write(f'goto function "Plot download {funcIdx}"\n\n')

        if funcIdx < functions:
            file.write(f'if (var plotAddr > {plots_per_function * funcIdx}) {{\n')
            file.write(f'  function "Plot download {funcIdx + 1}"\n')
            file.write(f'  exit\n')
            file.write(f'}}\n\n')

        nested_loop(funcIdx)

        if funcIdx < functions:
            file.write('\n\n')

print(f'DOWNLOAD: Generated and written to file.')
