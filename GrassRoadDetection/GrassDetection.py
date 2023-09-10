import cv2
import numpy as np

def grey(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def gauss(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def canny(image):
    return cv2.Canny(image, 50, 150)

def region(image):
    height, width = image.shape
    triangle = np.array([
        [(100, height), (475, 325), (width, height)]
    ])
    mask = np.zeros_like(image)
    mask = cv2.fillPoly(mask, triangle, 255)
    mask = cv2.bitwise_and(image, mask)
    return mask

def display_lines(image, lines):
    lines_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return lines_image

def average(image, lines):
    left = []
    right = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            y_int = parameters[1]
            if slope < 0:
                left.append((slope, y_int))
            else:
                right.append((slope, y_int))

    if left and right:
        right_avg = np.average(right, axis=0)
        left_avg = np.average(left, axis=0)
        left_line = make_points(image, left_avg)
        right_line = make_points(image, right_avg)
        return np.array([left_line, right_line])
    else:
        return None

def make_points(image, average):
    slope, y_int = average
    y1 = image.shape[0]
    y2 = int(y1 * 0.6)  # Adjust the y2 value for lane length
    x1 = int((y1 - y_int) / slope)
    x2 = int((y2 - y_int) / slope)
    return np.array([x1, y1, x2, y2])

def detect_green_grass(image):
    lower_green = np.array([35, 100, 40])
    upper_green = np.array([90, 255, 255])
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    return green_mask

def calculate_road_boundary(left_line, right_line, height):
    if left_line is not None and right_line is not None:
        left_slope, left_y_int = left_line[0], left_line[1]
        right_slope, right_y_int = right_line[0], right_line[1]
        y1 = height
        y2 = int(height * 0.6)
        x1 = int((y1 - left_y_int) / left_slope)
        x2 = int((y1 - right_y_int) / right_slope)
        return (x1, y1, x2, y2)
    else:
        return None

def process_image(image_path):
    image = cv2.imread(image_path)

    green_mask = detect_green_grass(image)

    kernel = np.ones((5, 5), np.uint8)
    dilated_mask = cv2.dilate(green_mask, kernel, iterations=2)
    eroded_mask = cv2.erode(dilated_mask, kernel, iterations=1)
    grey_image = grey(image)
    blurred_image = gauss(grey_image)
    edges_image = canny(blurred_image)
    isolated_region = cv2.bitwise_and(edges_image, eroded_mask)

    cv2.imshow("Edges", edges_image)
    cv2.imshow("Green Grass Region", isolated_region)

    # Crop the original image using the green mask
    cropped_image = cv2.bitwise_and(image, image, mask=eroded_mask)

    lines = cv2.HoughLinesP(isolated_region, 1, np.pi/180, 100, np.array([]), minLineLength=80, maxLineGap=20)

    connected_lines = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            connected_lines.append((x1, y1, x2, y2))

    averaged_lines = average(isolated_region, connected_lines)
    line_image = display_lines(cropped_image, averaged_lines)  # Draw lane lines on the cropped image

    road_boundary = calculate_road_boundary(averaged_lines[0] if averaged_lines is not None else None,
                                            averaged_lines[1] if averaged_lines is not None else None,
                                            image.shape[0])

    if road_boundary is not None:
        x1, y1, x2, y2 = road_boundary
        cv2.line(cropped_image, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("Lane Detection with Road Boundary", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Process multiple images
image_paths = ["HighGrass1.jpeg", "HighGrass.jpeg","HighGrass2.jpeg","campimg4.jpeg"]  

for path in image_paths:
    process_image(path)