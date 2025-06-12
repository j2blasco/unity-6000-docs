* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetReplacementShader.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).SetReplacementShader
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
public void SetReplacementShader([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string replacementTag); 
### Description
Make the camera render with shader replacement.
See [Rendering with Replaced Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderReplacement.html) page for details.  
  
If the replacementTag argument is not in use, pass an empty string as the value.  
  
After calling this function, camera will render its view with shader replacement. Call [ResetReplacementShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetReplacementShader.html) to reset it back to normal rendering.  
  
Additional resources: [Rendering with Replaced Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderReplacement.html), [ResetReplacementShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetReplacementShader.html), [RenderWithShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderWithShader.html).
* * *
