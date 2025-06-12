* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadIdentity.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).LoadIdentity
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
public static void LoadIdentity(); 
### Description
Load an identity into the current model and view matrices.
Changing the model, view or projection matrices overrides the current rendering matrices. It is good practice to save and restore these matrices using [GL.PushMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html) and [GL.PopMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html).  
  
Additional resources: [GL.MultMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultMatrix.html).
* * *
