* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ReleaseTemporaryRT.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).ReleaseTemporaryRT
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
public void ReleaseTemporaryRT(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | Shader property name for this texture.  
### Description
Add a "release a temporary render texture" command.
Releases a temporary render texture with given name. Presumably you have called ::GetTemporaryRT to create it before.  
  
Any temporary textures that were not explicitly released will be removed after camera is done rendering, or after [Graphics.ExecuteCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.ExecuteCommandBuffer.html) is done.  
  
Additional resources: [GetTemporaryRT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.GetTemporaryRT.html).
* * *
