* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Clear.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).Clear
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
public static void Clear(bool clearDepth, bool clearColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) backgroundColor, float depth = 1.0f); 
### Parameters
Parameter | Description  
---|---  
clearDepth | Should the depth buffer be cleared?  
clearColor | Should the color buffer be cleared?  
backgroundColor | The color to clear with, used only if `clearColor` is `true`.  
depth | The depth to clear the z-buffer with, used only if `clearDepth` is `true`. The valid range is from 0 (near plane) to 1 (far plane). The value is graphics API agnostic: the abstraction layer will convert the value to match the convention of the current graphics API.  
### Description
Clear the current render buffer.
This clears the screen or the active [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) you are drawing into. The cleared area is limited by the active viewport. This operation might alter the model/view/projection matrices.  
  
In most cases, a Camera will already be configured to clear the screen or [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) and you will not need to perform this operation manually.  
  
Additional resources: [GL.ClearWithSkybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.ClearWithSkybox.html).
* * *
