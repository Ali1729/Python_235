# def get_area_equal(sides,side1):
#     if sides<3:
#         return "area cannot be calculated"
    
#     if sides==3:
#         return ( 1.73 * side1 * side1) / 4
    
# def get_triangle_area_height(sides,ht, base):
#     if sides<3:
#         return "area cannot be calculated"
    
#     if sides==3:
#         return 0.5 * ht * base

# import math
# def get_triangle_area_diff(sides,side1,side2,side3):
#     if sides<3:
#         return "area cannot be calculated"
    
#     if sides==3:
#         s = side1+side2+side3
#         return math.sqrt(s * (s-side1) *(s-side2 )*(s-side3))
    
    
# print(get_area_equal(3,5))
# print(get_triangle_area_height(3,ht=5,base=10))
# print(get_triangle_area_diff(3,6,7,8))
    
    
# def get_area_triangle(si)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import math
# *args
# *args, **kwargs

def get_area_triangle(sides = 3, *side_sizes,**kwside_sizes)-> float:
    
    if len(side_sizes) ==1:
        return 17 * side_sizes[0]
    
    elif len(side_sizes) ==2:
        # user might have probably given height and base.
        return 0.5 * side_sizes[0] * side_sizes[1]
    elif len(side_sizes) ==3:
        s = sum(side_sizes)/2
        return math.sqrt(s * (s-side_sizes[0]) *(s-side_sizes[1] )*(s-side_sizes[2]))
    
    elif len(side_sizes)==0:
        if 'base' in kwside_sizes and 'height' in kwside_sizes:
            return 0.5 * kwside_sizes['base'] * kwside_sizes['height']
        else:
            return "input details are not correct"
        
    elif len(side_sizes) > 3:
        return "The sides and side_sizes are not matching"

def get_area(sides=3,*side_sizes:int,**kwside_sizes:int)->float:
    """_summary_: calculate area

    Args:
        sides (int, optional): _description_. Defaults to 3.

    Returns:
        float: _description_
    """
    print(" The function started without error")
    if sides <3 or sides> 4:
        return(" The number of sides should be between 3 and 4")
    
    elif sides==3:
        get_area_triangle(sides,*side_sizes,**kwside_sizes) # calling another function
        
    
    elif sides ==4:
        if len(side_sizes)==1:
            return side_sizes[0]*side_sizes[0]
        
    
# print(get_area(3,2))
# print(get_area(3,5,3))
# print(get_area(3,5,3,6))
# print(get_area(3,height=5,base=7))
# print(get_area(4,6))

# print(get_area(6,2))

print(get_area(3,ht=5,base=7))            
        
        