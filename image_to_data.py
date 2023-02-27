import cv2
import numpy as np

def line_detector(input_image):
    test_image = cv2.imread(sys.argv[1], 1)
    hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([0, 0, 0], dtype="uint8")
    upper_bound = np.array([250, 250, 110], dtype="uint8")

    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    mask[52:160, 62:86] = 0
    mask[160:183, 54:110] = 0

    detected_line = mask == 255
    output_array = np.nan * np.zeros(mask.shape[1], dtype=int)

    height = mask.shape[0]
    for i in range(mask.shape[1]):
        for j in range(mask.shape[0]):
            if detected_line[j][i]:
                output_array[i] = height - j
                break

    for point in reversed(range(len(output_array))):
        if np.isnan(output_array[point]):
            if point + 1 < len(output_array):
                output_array[point] = output_array[point + 1]
            else:
                output_array[point] = output_array[point - 1]

    output_array = np.array(list(map(int, output_array)))

    output_array.tofile("detected_line.csv", sep=",")

    # cv2.imshow("mask",mask)

    # if cv2.waitKey(0) & 0xFF == ord('q'):
    # cv2.destroyAllWindows()


line_detector(test_image)
