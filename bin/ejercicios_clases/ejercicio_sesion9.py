import sys

def ATContent(sequence):
    '''
    Calculate percentage of AT content in the sequence
    :param sequence: The genomic sequence
    :return: float, percentage
    '''
    sequence = sequence.upper()
    a_content = sequence.count('A')
    t_content = sequence.count('T')
    frequency = ((a_content + t_content)*100) / len(sequence)
    return frequency

arguments = sys.argv
# arguments -> ("nombre del script", "ruta del archivo")
file_path = arguments[1]
completeLine = ''
with open(file_path, 'r') as file_handler:
    for line in file_handler:
        if(line.startswith(">")):
            continue
        completeLine = completeLine + line.strip()

print (ATContent(completeLine.upper()))