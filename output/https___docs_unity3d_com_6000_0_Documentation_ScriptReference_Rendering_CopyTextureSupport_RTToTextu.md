* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.RTToTexture.html

#  [CopyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html).RTToTexture
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
### Description
Support for RenderTexture to Texture copies in [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html).
Not all platforms can copy from a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) into a regular [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) directly. For example, Direct3D9 currently can not do this. See [CopyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html) for an overview.
* * *
