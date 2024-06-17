def is_triangle(sides: list[int]) -> bool:
   return all(sides) and sum(sides) >= max(sides) * 2
    

def equilateral(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) == 3
