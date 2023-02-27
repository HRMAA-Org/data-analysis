import cv2
import os
import sys


def pdf_to_concat_image():
    with open(sys.argv[1], "rb") as file:
        pdf = file.read()

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        # print("JPG %d from %d to %d" % (njpg, istart, iend))
        jpg = pdf[istart:iend]
        with open("jpg%d.jpg" % njpg, "wb") as jpgfile:
            jpgfile.write(jpg)

        njpg += 1
        i = iend
    image_list = ["jpg0.jpg", "jpg1.jpg", "jpg2.jpg"]

    opened_image_list = []

    for image in image_list:
        opened_image = cv2.imread(image)
        opened_image_list.append(opened_image)
        os.remove(image)

    output_image = cv2.hconcat(opened_image_list)
    cv2.imwrite("concatenated_ecg.jpg", output_image)


pdf_to_concat_image()
