* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderWithShader.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).RenderWithShader
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
public void RenderWithShader([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string replacementTag); 
### Description
Render the camera with shader replacement.
See [Rendering with Replaced Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderReplacement.html) page for details.  
  
This will render the camera. It will use the camera's clear flags, target texture and all other settings.  
  
If the replacementTag argument is not in use, pass an empty string as the value.  
  
The camera will **not** send [OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html), [OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html) or [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPostRender.html) to attached scripts. Image filters will not be rendered either.  
  
This is used for special effects, e.g. rendering screen space normal buffer of the whole Scene, heat vision and so on. To make use of this feature, usually you create a camera and disable it. Then call RenderWithShader on it.  
  
You are not able to call the Render function from a camera that is currently rendering. If you wish to do this create a copy of the camera, and make it match the original one using [CopyFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyFrom.html).  
  
Additional resources: [Rendering with Replaced Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderReplacement.html), [SetReplacementShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetReplacementShader.html), [Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.Render.html).
* * *
