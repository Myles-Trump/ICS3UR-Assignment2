#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the area of a hexagon
#    with face length inputed by the user


def main():
    # this function calculates the area of a hexagon

    # input
    face_length = int(input("Enter the face length of the hexagon (mm): "))

    # process
    area_of_hexagon = (((3 ** 0.5) * 3) / 2) * face_length ** 2

    # output
    print("")
    print("Area is {0}mm²".format(area_of_hexagon))
    print("")
    print("done")


if __name__ == "__main__":
    main()
