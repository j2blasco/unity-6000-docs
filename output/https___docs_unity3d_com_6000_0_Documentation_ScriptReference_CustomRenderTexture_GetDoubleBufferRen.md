* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.GetDoubleBufferRenderTexture.html

#  [CustomRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.html).GetDoubleBufferRenderTexture
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html "Go to CustomRenderTexture Component in the Manual")
## Declaration
public [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) GetDoubleBufferRenderTexture(); 
### Returns
**RenderTexture** If CustomRenderTexture. doubleBuffered is true, this returns the Render Texture that this Custom Render Texture uses for double buffering. If CustomRenderTexture. doubleBuffered is false, this returns null. 
### Description
Gets the Render Texture that this Custom Render Texture uses for double buffering.
Use this if you are implementing your own Custom Render Texture update loop for a Custom Render Texture that is double buffered. Additional resources: Rendering.GraphicsSettings.disableBuiltinCustomRenderTextures, [CustomRenderTexture.doubleBuffered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-doubleBuffered.html).
* * *
