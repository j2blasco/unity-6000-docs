* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ReleaseTemporary.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).ReleaseTemporary
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
## Declaration
public static void ReleaseTemporary([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) temp); 
### Description
Release a temporary texture allocated with [GetTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html).
Later calls to [GetTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html) will reuse the RenderTexture created earlier if possible. When no one has requested the temporary RenderTexture for a few frames it will be destroyed.  
  
Additional resources: [GetTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html) function.
* * *
