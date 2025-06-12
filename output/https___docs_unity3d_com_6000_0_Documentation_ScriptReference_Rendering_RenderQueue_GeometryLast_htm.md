* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.GeometryLast.html

#  [RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html).GeometryLast
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
Last render queue that is considered "opaque".
Render queues in [0, GeometryLast] range are treated as opaque objects (sorted to reduce render state changes), whereas queues in [GeometryLast+1, 5000] range are treated as semitransparent objects (sorted back-to-front).  
  
Additional resources: [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html), [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html), [subshader tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
* * *
