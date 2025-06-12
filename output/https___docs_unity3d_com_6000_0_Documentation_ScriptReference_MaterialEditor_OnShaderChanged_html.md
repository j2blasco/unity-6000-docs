* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnShaderChanged.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).OnShaderChanged
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
protected void OnShaderChanged(); 
### Description
A callback that is invoked when a Material's Shader is changed in the Inspector.
This callback is invoked as the result of selecting a new Shader from the pop-up menu in the Inspector, or as the result of undoing or redoing actions that involved changing the Shader. It is called after a new Shader has been assigned to the Material currently in the Inspector, but before all Inspectors have been repainted (updated visually in the Editor).
* * *
