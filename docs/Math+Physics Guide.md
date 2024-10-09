# self.roll[0] += (self.dog_pos[0] - self.exhibit.get_width() / 2 - self.roll[0]) / 30
**Math Explain:** 
newCameraXPosition = currentCameraXPosition+((dogXPosition - (widthOfDisplay/2) - currentCameraXPosition)/30) 

*Why divide the width of the display by 2?*
Because our total window size is (640, 480) and the display size is half that (320, 240). This means we want to work within 320 pixels (The area of the window our player can see at any given time) as opposed to 640. 

*Why divide the new position by 30?*
Dividing by 30 slows down the overall rate of adjustment, giving the feel of a camera rolling across a screen as opposed to an instant change in view. 

For:
# self.roll[1] += (self.dog_pos[1] - self.exhibit.get_height() / 2 - self.roll[1]) / 30
It’s the same logic. Just with the vertical, y, up-down camera change. 
