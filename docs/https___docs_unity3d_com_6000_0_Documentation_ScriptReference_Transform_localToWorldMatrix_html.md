* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localToWorldMatrix.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).localToWorldMatrix
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) localToWorldMatrix; 
### Description
Matrix that transforms a point from local space into world space (Read Only).
You can also use [Transform.TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html) to transform coordinates instead of this matrix.  
  
Do not use this matrix to set shader parameters or to perform calculations related to rendering. Use [Renderer.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localToWorldMatrix.html) instead.
* * *
