* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaPosition.html

#  [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html).deltaPosition
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) deltaPosition; 
### Description
The position delta since last change in pixel coordinates.
The absolute position of the touch is recorded periodically and available in the [position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-position.html) property. The deltaPosition value is a Vector2 in pixel coordinates that represents the difference between the touch position recorded on the most recent update and that recorded on the previous update. The [deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaTime.html) value gives the time that elapsed between the previous and current updates; you can calculate the touch's speed of motion by dividing deltaPosition.magnitude by [deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaTime.html).  
  
Additional resources: [deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaTime.html).
* * *
