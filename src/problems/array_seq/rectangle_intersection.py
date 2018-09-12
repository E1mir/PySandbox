"""
Problem
Given two rectangles, determine if they overlap. The rectangles are defined as a Dictionary:

r1 = {
    # x and y coordinates of the bottom-left corner of the rectangle
    'x': 2, 'y': 4,
    # Width and Height of rectangle
    'w': 5, 'h': 12
}
If the rectangles do overlap, return the dictionary which describes the overlapping section
"""


def calc_overlap(coord_1, dim_1, coord_2, dim_2):
    greater = max(coord_1, coord_2)
    lower = min(coord_1 + dim_1, coord_2 + dim_2)

    if greater >= lower:
        return None, None

    overlap = lower - greater

    return greater, overlap


def calc_rect_overlap(r1, r2):
    x_overlap, w_overlap = calc_overlap(
        r1['x'], r1['w'],
        r2['x'], r2['w']
    )

    y_overlap, h_overlap = calc_overlap(
        r1['y'], r1['h'],
        r2['y'], r2['h']
    )

    if not w_overlap or not h_overlap:
        print('No overlap')
        return None

    return {
        'x': x_overlap,
        'y': y_overlap,
        'w': w_overlap,
        'h': h_overlap
    }


if __name__ == '__main__':
    r1 = {'x': 2, 'y': 4, 'w': 5, 'h': 12}
    r2 = {'x': 1, 'y': 5, 'w': 7, 'h': 14}
    o = calc_rect_overlap(r1, r2)
    print(o)
