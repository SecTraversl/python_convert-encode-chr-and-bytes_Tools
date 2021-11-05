# %%
#######################################
def convertfrom_hex_notation(bytes_string: bytes):
    """Takes a given bytes object containing hex notation (e.g. b'\\x00\\x01\\x02\\x03') and returns a bytes object with the hexadecimal notation '\\x' glyphs removed from the output (or, transforming the output to the "Hexadecimal representation of binary data", as the binascii module terms it).

    Examples:
        >>> eth_dst = b"\\x00\r\\xb9'\\x07\\x80"\n
        >>> eth_src = b'\\x00\\x0c)%l\\x15'\n
        
        >>> convertfrom_hex_notation(eth_dst)\n
        b'000db9270780'
        >>> eth_dst\n
        b"\\x00\r\\xb9'\\x07\\x80"

        >>> convertfrom_hex_notation(eth_src)\n
        b'000c29256c15'
        >>> eth_src\n
        b'\\x00\\x0c)%l\\x15'

    References:
        https://stackoverflow.com/questions/20556139/how-do-i-parse-a-captured-packet-in-python

    Args:
        bytes_string (bytes): Reference a bytes object with hexadecimal notation.

    Returns:
        bytes: Returns a bytes object.
    """
    import binascii
    # This ".b2a_hex()" is the same as ".hexlify()", so this also works:
    # - slash_x_removed = binascii.b2a_hex(bytes_string)
    slash_x_removed = binascii.hexlify(bytes_string)
    return slash_x_removed

