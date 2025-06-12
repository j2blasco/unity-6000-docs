* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ClearRenderTarget.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).ClearRenderTarget
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
public void ClearRenderTarget(bool clearDepth, bool clearColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor); 
## Declaration
public void ClearRenderTarget(bool clearDepth, bool clearColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor, float depth); 
## Declaration
public void ClearRenderTarget(bool clearDepth, bool clearColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor, float depth, uint stencil); 
## Declaration
public void ClearRenderTarget([Rendering.RTClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html) clearFlags, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor, float depth, uint stencil); 
## Declaration
public void ClearRenderTarget([Rendering.RTClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html) clearFlags, Color[] backgroundColors, float depth, uint stencil); 
### Parameters
Parameter | Description  
---|---  
clearDepth | Whether to clear both the depth buffer and the stencil buffer.  
clearColor | Whether to clear the color buffer.  
clearFlags | Which render targets to clear, defined using a bitwise OR combination of [RTClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html) values.  
backgroundColor | Color to clear with.  
backgroundColors | Colors to clear with.  
depth | Depth to clear with (default is 1.0).  
stencil | Stencil to clear with (default is 0).  
### Description
Adds a "clear render target" command.
* * *
