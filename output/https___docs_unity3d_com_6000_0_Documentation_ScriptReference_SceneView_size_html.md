* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-size.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).size
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
size; 
### Description
The size of the Scene view measured diagonally.
Use with [pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-pivot.html), [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-rotation.html), and [ CameraSettings.fieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-fieldOfView.html) to calculate camera transformation.   
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SceneViewSizeDiagram.png)   
The image above shows the math used to calculate the actual field of view. Here BC = size, and you need to find AB. ACB is a right angle, and BAC is half the field of view. That creates the expression: sin(BAC) = BC/AB, and so AB = BC/sin(BAC).
* * *
