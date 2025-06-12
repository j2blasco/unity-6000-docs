* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-colorFormat.html

#  [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html).colorFormat
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
[RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) colorFormat; 
### Description
The format of the RenderTarget is expressed as a [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html). Internally, this format is stored as a [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) compatible with the current system (see [SystemInfo.GetCompatibleFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetCompatibleFormat.html)). Therefore, if you set a format and immediately get it again, it may return a different result from the one just set.
* * *
