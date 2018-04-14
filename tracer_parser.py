def parser(trace_file):
    read_trace = open(trace_file,"r")
    trace_str = ""
    for rows in read_trace.readlines():
        rows = rows.replace(";#ref","") if ";#ref" in rows else rows
        rows = rows.replace("$ns_","") if "$ns_" in rows else rows
        rows = rows.replace("$node_(","node=") if "$node_" in rows else rows
        trace_str += rows.replace("\"","")
    tempfile = open("{0}_copy".format(trace_file),"w")
    tempfile.write(trace_str)
    tempfile.close()
    return tempfile.name

# fp = parser("highway25")
