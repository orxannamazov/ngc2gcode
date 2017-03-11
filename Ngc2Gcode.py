inputFile = raw_input('Enter input file name (with format) : ')
with open(inputFile, 'r') as f:
    Gval = ''
    newlines = []
    for line in f:
        if line in ['\n', '\r\n']:
            newlines.append(line)
        elif 'M' in line:
            newlines.append(line)
        elif 'G04' in line:
            newlines.append(line)
        elif 'G' in line and not 'G04' in line:
            Gval = line[line.index('G'):line.index(' ')]

            if Gval == 'G0' or Gval == 'G00':
                Gval = 'G00'
            elif Gval == 'G1' or Gval == 'G01':
                Gval = 'G01'
            elif Gval == 'G2' or Gval == 'G02':
                command = 'G02'
            elif Gval == 'G3' or Gval == 'G03':
                Gval = 'G03'

            if line.startswith('G0 ', 0, 3):
                newlines.append(line.replace('G0', 'G00'))
            elif line.startswith('G1 ', 0, 3):
                newlines.append(line.replace('G1', 'G01'))
            elif line.startswith('G2 ', 0, 3):
                newlines.append(line.replace('G2', 'G02'))
            elif line.startswith('G3 ', 0, 3):
                newlines.append(line.replace('G3', 'G03'))
            elif line.startswith('G4 ', 0, 3):
                newlines.append(line.replace('G4', 'G04'))
            elif line.startswith('G5 ', 0, 3):
                newlines.append(line.replace('G5', 'G05'))
            elif line.startswith('G6 ', 0, 3):
                newlines.append(line.replace('G6', 'G06'))
        else:
            l = Gval + ' ' + line
            newlines.append(l)
    f.close()
    outputFile = inputFile[0:inputFile.index('.')]
    outputFile = outputFile + '.gcode'

    outfile = open(outputFile, 'w')
    for item in newlines:
        outfile.write('%s' % item)
    outfile.close()
    print "\n\tYour File is Converted!!! \n"
    print('Output File: %s' %outputFile)
