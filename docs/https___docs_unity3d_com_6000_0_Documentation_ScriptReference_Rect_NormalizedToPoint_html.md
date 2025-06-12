* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.NormalizedToPoint.html

#  [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).NormalizedToPoint
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) NormalizedToPoint([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rectangle, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) normalizedRectCoordinates); 
### Parameters
Parameter | Description  
---|---  
rectangle | Rectangle to get a point inside.  
normalizedRectCoordinates | Normalized coordinates to get a point for.  
### Description
Returns a point inside a rectangle, given normalized coordinates.
The rectangle has coordinates between zero and one for the x and y axes. This function will compute the real screen coordinates and return as a `Vector2`.
* * *
