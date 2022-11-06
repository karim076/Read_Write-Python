# how many lines
lineCount = 1
# total words
wordCountTotal = 0
# opening report.txt in write modes and opening record in read modes
reportFile = open("report.txt", "w")
recordFile = open("record.txt", "r")
# counting line and words
for line in recordFile:
        wordCountLine =  len(line.split())
        wordCountTotal += wordCountLine
        lineCount += 1

# putting data into record file 
reportFile.write(f"Aantal woorden: {wordCountTotal}\nAantal regels: {lineCount}")
# Debug in terminal (testing purposes)
print(f"Aantal regels: {lineCount}")
print(f"Aantal woorden: {wordCountTotal}")
# closing the files
reportFile.close()
recordFile.close()