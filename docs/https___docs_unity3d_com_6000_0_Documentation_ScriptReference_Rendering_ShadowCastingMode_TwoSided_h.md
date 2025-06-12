* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.TwoSided.html

#  [ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html).TwoSided
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
Shadows are cast from this object, treating it as two-sided.
Shadow rendering will turn off backface culling, even if object's shader has backface culling on. This means that single-sided objects (like a Plane or a Quad) will cast shadows, even if the light is behind them.  
  
Additional resources: [Renderer.shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-shadowCastingMode.html).
* * *
