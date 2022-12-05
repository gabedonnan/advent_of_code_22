
import numpy as np

def get_nums(line):
    numbers = "0123456789"
    number = False
    final_list = []
    iterator = 0
    for i,char in enumerate(line):
        if line[i] in numbers:
            number = True
            iterator = i
            while number:
                if line[iterator] == " ":
                    number = False
                else:
                    if iterator < len(line)-1:
                        iterator += 1
                    else:
                        number = False
            if line[i:iterator].strip() != "":
                final_list.append(line[i:iterator].strip())
            else:
                final_list.append(line[-1].strip())
    if len(final_list) == 4:
        del final_list[1] 
    return final_list
            
                    
            

def get_boxes(boxes):
    columns = []
    with open(boxes, "r") as b:
        for row,line in enumerate(b):
            columns.append([])
            for i in range(len(line)):
                if (i - 1) % 4 == 0:
                    columns[row].append(line[i])
    return columns[:-1]


def normalise_boxes(box_mat):
    final = np.array(box_mat)
    final = final.transpose()
    final = np.flip(final,1)
    final = final.tolist()
    for i in range(len(final)):
        while " " in final[i]:
            final[i].pop()
    return final

def move_box(box_mat, start, dest):
    if len(box_mat[start]) > 0:
        temp = box_mat[start].pop()
        box_mat[dest].append(temp)
    return box_mat

def move_box_2(box_mat, number, start, dest):
    if len(box_mat[start]) >= number:
        temp = box_mat[start][-number:]
        box_mat[start] = box_mat[start][:len(box_mat[start])-number]
        box_mat[dest].extend(temp)
    elif len(box_mat[number]) > 0:
        temp = box_mat[start][-len(box_mat[number])]
        box_mat[start] = []
        box_mat[dest].extend(temp)
    return box_mat

def main(boxes, instructions):
    numbers = "0123456789"
    box_matrix = get_boxes(boxes)
    final = normalise_boxes(box_matrix)
    instruction_list = []
    with open(instructions, "r") as f:
        for line in f:
            instruction_list = get_nums(line)
            #print(instruction_list)
            for i in range(int(instruction_list[0])):
                final = move_box(final, int(instruction_list[1])-1, int(instruction_list[2])-1)
    for row in final:
        print(row[-1])
    return final
                
def main_2(boxes, instructions):
    numbers = "0123456789"
    box_matrix = get_boxes(boxes)
    final = normalise_boxes(box_matrix)
    instruction_list = []
    with open(instructions, "r") as f:
        for line in f:
            instruction_list = get_nums(line)
            #print(instruction_list)
            final = move_box_2(final,int(instruction_list[0]) ,int(instruction_list[1])-1, int(instruction_list[2])-1)
    for row in final:
        print(row[-1])
    return final
                                    

if __name__ == "__main__":
    main_2("boxes.txt", "instructions.txt")
