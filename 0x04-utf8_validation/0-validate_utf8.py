#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
"""

def validUTF8(data):
    """
    Returns True if the given data set represents a valid UTF-8 encoding, and False otherwise.
    """
    num_bytes = 0
    
    # Iterate through each byte in the data set
    for byte in data:
        
        # If this is the start of a new character sequence
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                # This is a single-byte character
                continue
            elif (byte >> 5) == 0b110:
                # This is the start of a two-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # This is the start of a three-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # This is the start of a four-byte character
                num_bytes = 3
            else:
                # This byte is not the start of a valid character sequence
                return False
        
        else:
            # This byte should be a continuation byte
            if (byte >> 6) != 0b10:
                # This byte is not a continuation byte
                return False
            
            num_bytes -= 1
            
    # If we reached the end of the data set and there are still bytes left in the current sequence
    if num_bytes != 0:
        return False
    
    return True
