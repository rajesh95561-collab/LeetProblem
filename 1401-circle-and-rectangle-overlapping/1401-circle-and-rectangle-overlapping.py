class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xi,yi = 0,0
        #find the nearest xi point of rectangle from circle
        if x2 < xCenter:xi = x2
        elif xCenter < x1:xi = x1
        else: xi = xCenter
        #find the nearest yi point of rectangle from circle
        if y2 < yCenter:yi = y2
        elif yCenter < y1:yi = y1
        else: yi = yCenter
        #find the distance between nearest point and circle center
        d = ((xi-xCenter)**2 + (yi-yCenter)**2)**0.5
        if d <= radius:return True
        return False
