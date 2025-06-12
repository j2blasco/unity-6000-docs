* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.RelativeMouseAt.html

#  [Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html).RelativeMouseAt
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) RelativeMouseAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inputMouseCoordinates); 
### Parameters
Parameter | Description  
---|---  
inputMouseCoordinates | Mouse Input Position as Coordinates.  
### Description
Query relative mouse coordinates.
RelativeMouseAt can be used to query relative mouse input coordinates and the screen in which Mouse Input is recorded. x, y returns the coordinates in relative space and z returns the screen in which Mouse Input is handled, returns [Vector3.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html) when Multiple Displays are not supported. Currently implemented for Windows and macOS Standalone players.
* * *
