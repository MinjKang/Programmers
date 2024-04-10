def solution(brown, yellow):
    answer = []
    total = brown + yellow
    yellow_width = 0
    yellow_height = 0
    height = 0
    
    for width in range(1, total):
        if total % width == 0:
            height = total // width
            if width >= height:
                yellow_width = width-2
                yellow_height = height-2
                if yellow_width * yellow_height == yellow:
                    answer = [width, height]
    return answer
            
    