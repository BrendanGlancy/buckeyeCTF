# revsere engineer a .sav file 

import sys
import struct

def main():
    # the file is called pocket-monster.sav open it
    with open('pocket-monsters.sav', 'rb') as f:
        # read the entire file into a buffer
        buf = f.read()

    # the first 4 bytes are the number of monsters
    num_monsters = struct.unpack('<I', buf[:4])[0]
    print('num monsters:', num_monsters)

    # the next 4 bytes are the number of items
    num_items = struct.unpack('<I', buf[4:8])[0]
    print('num items:', num_items)

    # the next 4 bytes are the number of moves
    num_moves = struct.unpack('<I', buf[8:12])[0]
    print('num moves:', num_moves)

    # the next 4 bytes are the number of types
    num_types = struct.unpack('<I', buf[12:16])[0]
    print('num types:', num_types)

    # the next 4 bytes are the number of abilities
    num_abilities = struct.unpack('<I', buf[16:20])[0]
    print('num abilities:', num_abilities)




if __name__ == '__main__':
    main()

