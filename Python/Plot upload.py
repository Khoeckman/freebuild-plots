from math import ceil

output_file = "output.htsl"
plots_per_function = 14
plots = 7*7*3
functions = ceil(plots / plots_per_function)

def nested_loop(funcIdx):
    global plotIdx

    for i in range(1, plots_per_function + 1 + int(funcIdx == functions)):
        plotIdx += 1

        if plotIdx > plots:
            return

        file.write(f'if (var plotAddr == {plotIdx}) {{\n')
        file.write(f'  globalvar p{plotIdx}Id = var plotId 0 true\n')
        file.write(f'  globalvar p{plotIdx}Ign = var plotIgn 0 true\n')
        file.write(f'  globalvar p{plotIdx}Unix = var plotUnix 0 true\n')
        file.write(f'  globalvar p{plotIdx}Settings = var plotSettings 0 true\n')
        file.write(f'  globalvar p{plotIdx}Points = var plotPoints 0 true\n')
        file.write(f'  globalvar p{plotIdx}Rated = var plotRated 0 true\n')
        file.write(f'  exit\n')
        file.write(f'}}\n')


with open(output_file, "w") as file:
    # Step 1: Create all functions
    for funcIdx in range(1, functions + 1):
        if funcIdx == 1:
            file.write(f'goto function "Plot upload"\n')
        else:
            file.write(f'goto function "Plot upload {funcIdx}"\n')

    file.write('\n')

    # Step 2
    plotIdx = 0

    for funcIdx in range(1, functions + 1):
        if funcIdx == 1:
            file.write(f'goto function "Plot upload"\n\n')
            file.write(f'var cd = 1\n\n')
        else:
            file.write(f'goto function "Plot upload {funcIdx}"\n\n')

        if funcIdx < functions:
            file.write(f'if (var plotAddr > {plots_per_function * funcIdx}) {{\n')
            file.write(f'  function "Plot upload {funcIdx + 1}"\n')
            file.write(f'  exit\n')
            file.write(f'}}\n\n')

        nested_loop(funcIdx)

        if funcIdx < functions:
            file.write('\n\n')

print(f'UPLOAD: Generated and written to file.')
