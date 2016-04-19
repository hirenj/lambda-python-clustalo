from clustalo import clustalo, DNA, PROTEIN

def my_handler(event, context):
    return_val = clustalo( { "A" : event['seqa'], "B" : event['seqb'], "C": event['seqc'] }, seqtype=PROTEIN)
    return { 
        'message' : return_val
    }