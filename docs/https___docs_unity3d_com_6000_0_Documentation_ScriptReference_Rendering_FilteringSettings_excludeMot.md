* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-excludeMotionVectorObjects.html

#  [FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html).excludeMotionVectorObjects
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
excludeMotionVectorObjects; 
### Description
Determines if Unity excludes GameObjects that are in motion from rendering. This refers to GameObjects that have an active Motion Vector pass assigned to their Material or have set the Motion Vector mode to **per object motion** (Menu: **Mesh Renderer > Additional Settings > Motion Vectors > Per Object Motion**). For Unity to exclude a GameObject from rendering, the GameObject must have moved since the last frame. To exclude a GameObject manually, enable a [Motion Vector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) pass.
Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a simple render loop in a custom render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-creating-simple-render-loop.html).
* * *
