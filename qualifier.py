"""             ┌----------------┐
                |TABLE COMPONENTS|
                |GLOBAL VARIABLES|
                └----------------┘
"""
STRAIGHT_EDGE_VERTICAL = "│"
STRAIGHT_EDGE_HORIZONTAL = "─"
TOP_LEFT_CORNER = "┌"
TOP_RIGHT_CORNER = "┐"
BOTTOM_LEFT_CORNER = "└"
BOTTOM_RIGHT_CORNER = "┘"
TOP_MIDDLE_INTERSECTION = "┬"
BOTTOM_MIDDLE_INTERSECTION = "┴"
VERTICAL_RIGHT_INTERSECTION = "├"
VERTICAL_MIDDLE_INTERSECTION = "┼"
VERTICAL_LEFT_INTERSECTION = "┤"
SPACE = " "

"""
MAIN FUNCTION- 
def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:

    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.

"""
def make_table(rows, labels = None, centered = False):
    table = ""
    num_rows = len(rows)
    num_items = len(rows[0])
    num_labels = 1
    if(labels != None):
        num_labels = len(labels)

    max_length_list = get_max_length(num_rows, num_items, rows, labels)
    table += draw_top_table(max_length_list, num_items)

    if(labels != None):
        table = draw_label_table(num_labels, labels, max_length_list, table, centered)

    table = draw_table(num_rows, num_items, rows, max_length_list, table, centered)
    return table

"""
CREATES A LIST WITH THE LENGTHS OF THE LONGEST ITEMS FOR EACH LABEL
"""
def get_max_length(num_rows, num_labels, rows, labels):

    length_list = []
    for n in range(0, num_labels):
        if(labels != None):
            max_length = len(str(labels[n]))
        else:
            max_length = 0
        for i in range(0, num_rows):
            if len(str(rows[i][n])) > max_length:
                max_length = len(str(rows[i][n]))
        length_list.append(max_length)
    return length_list

"""
DRAWS THE TABLE FOR THE LABELS
"""
def draw_label_table(num_labels, labels, max_length_list, table, centered):
    for i in range(0, num_labels):
        item_len = len(str(labels[i]))
        border = SPACE * (max_length_list[i] - item_len + 1)
        border2 = SPACE * (abs(max_length_list[i] - item_len)//2 + 1)
        if(centered == False):
            table += STRAIGHT_EDGE_VERTICAL + SPACE + str(labels[i]) + border
        else:
            table += STRAIGHT_EDGE_VERTICAL + border2 + str(labels[i]) + border2
            if ((max_length_list[i] - item_len) % 2 != 0):
                table += SPACE
    table += STRAIGHT_EDGE_VERTICAL + "\n" + draw_middle_table(max_length_list, num_labels)
    return table

"""
DRAWS THE TABLE FOR ALL THE ITEMS
"""
def draw_table(num_rows, num_labels, rows, max_length_list, table, centered):

    for n in range(0,num_rows):
        for i in range(0, num_labels):
            item_len = len(str(rows[n][i]))
            border = SPACE * (max_length_list[i] - item_len + 1)
            border2 = SPACE * (abs(max_length_list[i] - item_len) // 2 + 1)
            if (centered == False):
                table += STRAIGHT_EDGE_VERTICAL + SPACE + str(rows[n][i]) + border
            else:
                table += STRAIGHT_EDGE_VERTICAL + border2 + str(rows[n][i]) + border2
                if((max_length_list[i] - item_len) %2 != 0):
                    table += SPACE
        table += STRAIGHT_EDGE_VERTICAL + "\n"
    table += draw_bottom_table(max_length_list, num_labels)

    return table

"""
DRAWS THE TOP LINE OF THE TABLE
"""
def draw_top_table(length,num_labels):

    line = TOP_LEFT_CORNER
    for i in range(0, num_labels):
        aux = length[i]
        while(aux != 0):
            line += STRAIGHT_EDGE_HORIZONTAL
            aux -= 1
        if(num_labels != 1 and i != num_labels -1):
            line += STRAIGHT_EDGE_HORIZONTAL*2 + TOP_MIDDLE_INTERSECTION
    line += STRAIGHT_EDGE_HORIZONTAL*2 + TOP_RIGHT_CORNER + "\n"
    return line

"""
DRAWS THE BOTTOM LINE OF THE LABELS TABLE
"""
def draw_middle_table(length,num_labels):

    line = VERTICAL_RIGHT_INTERSECTION
    for i in range(0, num_labels):
        aux = length[i]
        while(aux != 0):
            line += STRAIGHT_EDGE_HORIZONTAL
            aux -= 1
        if(num_labels != 1 and i != num_labels -1):
            line += STRAIGHT_EDGE_HORIZONTAL*2 + VERTICAL_MIDDLE_INTERSECTION
    line += STRAIGHT_EDGE_HORIZONTAL*2 + VERTICAL_LEFT_INTERSECTION + "\n"
    return line

"""
DRAWS THE BOTTOM LINE OF THE TABLE
"""
def draw_bottom_table(length,num_labels):

    line = BOTTOM_LEFT_CORNER
    for i in range(0, num_labels):
        aux = length[i]
        while(aux != 0):
            line += STRAIGHT_EDGE_HORIZONTAL
            aux -= 1
        if(num_labels != 1 and i != num_labels -1):
            line += STRAIGHT_EDGE_HORIZONTAL*2 + BOTTOM_MIDDLE_INTERSECTION
    line += STRAIGHT_EDGE_HORIZONTAL*2 + BOTTOM_RIGHT_CORNER
    return line

table = make_table(
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"],
    centered = True
)
print(table)