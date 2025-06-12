* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).GetHandleSize
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
public static float GetHandleSize([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The position of the handle in 3d space.  
### Returns
**float** A constant screen-size for the handle, based on the distance between from the supplied handle's position to the camera. 
### Description
Get world space size of a manipulator handle at given position.
Uses the current camera to calculate suitable size.
* * *
