def _convert_to_ascii(s):
    # chars = {0x0: " ", 0x1: "&", 0xbff: "-", 0x4: "0", 0x8: "1", 0x6ff: "A",
    #          0xA: "J", 0xC: "/",
    #          0x10: "2", : "B", 0x12: "K", 0x14: "S", 0x20: "3", 0x21: "C",
    #          0xbbf: "L",
    #          0x24: "T", 0x40: "4", 0x7df: "D", 0x42: "M", 0x44: "U",
    #          0x80: "5",
    #          0x81: "E",
    #          0x82: "N", 0x84: "V", 0x100: "6", 0x7f7: "F", 0x102: "O",
    #          0x104: "W", 0x200: "7",
    #          0x7fb: "G", 0x202: "P", 0x204: "X", 0x400: "8", 0x401: "H",
    #          0x402: "Q", 0x404: "Y",
    #          0x422: "$", 0x424: ", ",
    #          0x440: "@", 0x441: "<", 0x442: "*", 0x480: ">'", 0x481: "(",
    #          0x482: ")", 0x484: "_",
    #          0x500: "=", 0x501: "+", 0x502: ";", 0x504: ">", 0x600: "\"",
    #          0x604: "?", 0x800: "9", 0x801: "I", 0x802: "R", 0x804: "Z"}

    # print chars
    # return chars[int(s, 2)]
    if s == "011011111111":
        return "A"
    elif s == "011101111111":
        return "B"
    elif s == "011110111111":
        return "C"
    elif s == "011111011111":
        return "D"
    elif s == "011111101111":
        return "E"
    elif s == "011111110111":
        return "F"
    elif s == "011111111011":
        return "G"
    elif s == "011111111101":
        return "H"
    elif s == "011111111110":
        return "I"
    elif s == "101011111111":
        return "J"
    elif s == "101101111111":
        return "K"
    elif s == "101110111111":
        return "L"
    elif s == "101111011111":
        return "M"
    elif s == "101111101111":
        return "N"
    elif s == "101111110111":
        return "O"
    elif s == "101111111011":
        return "P"
    elif s == "101111111101":
        return "Q"
    elif s == "101111111110":
        return "R"
    elif s == "110101111111":
        return "S"
    elif s == "110110111111":
        return "T"
    elif s == "110111011111":
        return "U"
    elif s == "110111101111":
        return "V"
    elif s == "110111110111":
        return "W"
    elif s == "110111111011":
        return "X"
    elif s == "110111111101":
        return "Y"
    elif s == "110111111110":
        return "Z"
    elif s == "101111111111":
        return "-"
    elif s == "110111111111":
        return "0"
    elif s == "111011111111":
        return "1"
    elif s == "111101111111":
        return "2"
    elif s == "111110111111":
        return "3"
    elif s == "111111011111":
        return "4"
    elif s == "111111101111":
        return "5"
    elif s == "111111110111":
        return "6"
    elif s == "111111111011":
        return "7"
    elif s == "111111111101":
        return "8"
    elif s == "111111111110":
        return "9"
    elif s == "110011111111":
        return "/"
    elif s == "011111111111":
        return "&"
    elif s == "111101111101":
        return ":"
    elif s == "110110111101":
        return ","
    elif s == "101111110101":
        return ";"
    elif s == "101111011101":
        return "*"
    elif s == "101101111101":
        return '!'
    elif s == "110110111101":
        return ','
    elif s == "011111011101":
        return '<'
    elif s == "110111110101":
        return '>'
    elif s == "111111111001":
        return '"'
    elif s == "011111101101":
        return '('
    elif s == "101111101101":
        return ')'
    elif s == "111110111101":
        return "#"
    elif s == "110011111111":
        return "/"
    elif s == "011110111101":
        return "."
    else:
        return " "


def _convert_to_bin(s):
    if s == "A":
        return "011011111111"
    elif s == "B":
        return "011101111111"
    elif s == "C":
        return "011110111111"
    elif s == "D":
        return "011111011111"
    elif s == "E":
        return "011111101111"
    elif s == "F":
        return "011111110111"
    elif s == "G":
        return "011111111011"
    elif s == "H":
        return "011111111101"
    elif s == "I":
        return "011111111110"
    elif s == "J":
        return "101011111111"
    elif s == "K":
        return "101101111111"
    elif s == "L":
        return "101110111111"
    elif s == "M":
        return "101111011111"
    elif s == "N":
        return "101111101111"
    elif s == "O":
        return "101111110111"
    elif s == "P":
        return "101111111011"
    elif s == "Q":
        return "101111111101"
    elif s == "R":
        return "101111111110"
    elif s == "S":
        return "110101111111"
    elif s == "T":
        return "110110111111"
    elif s == "U":
        return "110111011111"
    elif s == "V":
        return "110111101111"
    elif s == "W":
        return "110111110111"
    elif s == "X":
        return "110111111011"
    elif s == "Y":
        return "110111111101"
    elif s == "Z":
        return "110111111110"
    elif s == "-":
        return "101111111111"
    elif s == "0":
        return "110111111111"
    elif s == "1":
        return "111011111111"
    elif s == "2":
        return "111101111111"
    elif s == "3":
        return "111110111111"
    elif s == "4":
        return "111111011111"
    elif s == "5":
        return "111111101111"
    elif s == "6":
        return "111111110111"
    elif s == "7":
        return "111111111011"
    elif s == "8":
        return "111111111101"
    elif s == "9":
        return "111111111110"
    elif s == ":":
        return "111101111101"
    elif s == ";":
        return "101111110101"
    elif s == "*":
        return "101111011101"
    elif s == '!':
        return "101101111101"
    elif s == ',':
        return "110110111101"
    elif s == '<':
        return "011111011101"
    elif s == ">":
        return "110111110101"
    elif s == '"':
        return "111111111001"
    elif s == "(":
        return "011111101101"
    elif s == ")":
        return "101111101101"
    elif s == "#":
        return "111110111101"
    elif s == "/":
        return "110011111111"
    elif s == ".":
        return "011110111101"
