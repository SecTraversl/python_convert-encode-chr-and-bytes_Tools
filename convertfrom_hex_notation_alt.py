# %%
#######################################
def convertfrom_hex_notation_alt(bytes_string: bytes):
    import codecs
    return codecs.encode(bytes_string, 'hex')