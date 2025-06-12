* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetTargetBuffers.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).SetTargetBuffers
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public void SetTargetBuffers([RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) colorBuffer, [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) depthBuffer); 
## Declaration
public void SetTargetBuffers(RenderBuffer[] colorBuffer, [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) depthBuffer); 
### Parameters
Parameter | Description  
---|---  
colorBuffer | The RenderBuffer(s) to which color information will be rendered.  
depthBuffer | The RenderBuffer to which depth information will be rendered.  
### Description
Sets the Camera to render to the chosen buffers of one or more RenderTextures.
Additional resources: [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html), [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), [targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html).
* * *
