* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html

# RenderQueue
enumeration
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
Determine in which order objects are renderered.
This way for example transparent objects are rendered after opaque objects, and so on.  
  
Additional resources: [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html), [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html), [subshader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
### Properties
Property | Description  
---|---  
[Background](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Background.html) | This render queue is rendered before any others.  
[Geometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Geometry.html) | Opaque geometry uses this queue.  
[AlphaTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.AlphaTest.html) | Alpha tested geometry uses this queue.  
[GeometryLast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.GeometryLast.html) | Last render queue that is considered "opaque".  
[Transparent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Transparent.html) | This render queue is rendered after Geometry and AlphaTest, in back-to-front order.  
[Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.Overlay.html) | This render queue is meant for overlay effects.  
* * *
