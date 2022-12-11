"""Signal device protocol marker"""

def has_unique_characters(signal):
    signal_length = len(signal)
    list_conv = []
    list_conv[:0] = signal
    sig_set = set(list_conv)
    if len(sig_set) == signal_length:
        return True
    return False

with open("Day6/input.txt","r") as signal_stream:
    index = 0
    marker_length = 4
    message_marker_length = 14
    signal = signal_stream.readline()
    while index < len(signal) - marker_length:
        if has_unique_characters(signal[index:index+marker_length]):
            print(f"Marker appears at: {index+marker_length}")
            break
        index += 1
    index = 0
    while index < len(signal) - message_marker_length:
        if has_unique_characters(signal[index:index+message_marker_length]):
            print(f"Message marker appears at: {index+message_marker_length}")
            break
        index += 1
