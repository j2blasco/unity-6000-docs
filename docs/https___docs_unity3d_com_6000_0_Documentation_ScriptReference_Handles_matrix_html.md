* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).matrix
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix; 
### Description
Matrix for all handle operations. This is used by functions in [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html) and [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) to transform controls.
To make all Handle routines work in the local coordinate space of a GameObject, set this to [Transform.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localToWorldMatrix.html).  
  
The handles matrix is reset to identity at the end of every frame. It is considered best practice to store and restore the state of this matrix during use. See [DrawingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.html) for a convenient means of preserving handle global state.
* * *
