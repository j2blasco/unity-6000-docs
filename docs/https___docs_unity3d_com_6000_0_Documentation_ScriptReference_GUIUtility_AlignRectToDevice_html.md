* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.AlignRectToDevice.html

#  [GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html).AlignRectToDevice
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) AlignRectToDevice([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) AlignRectToDevice([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect, out int widthInPixels, out int heightInPixels); 
### Parameters
Parameter | Description  
---|---  
local | The local space rectangle that needs to be processed.  
widthInPixels | Width, in pixel units, of the axis-aligned bounding box that encompasses the aligned points.  
heightInPixels | Height, in pixel units, of the axis-aligned bounding box that encompasses the aligned points.  
### Returns
**Rect** The aligned rectangle in local space. 
### Description
Align a local space rectangle to the pixel grid.
Aligns the top-left and bottom-right corners of the provided local space rectangle to the pixel grid and returns the local space axis-aligned bounding box that encompasses those points.
* * *
