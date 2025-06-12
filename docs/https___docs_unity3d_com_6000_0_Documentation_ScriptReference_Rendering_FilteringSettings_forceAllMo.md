* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-forceAllMotionVectorObjects.html

#  [FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html).forceAllMotionVectorObjects
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
forceAllMotionVectorObjects; 
### Description
Determines if Unity renders not moving GameObjects in motion vector pass. This refers to GameObjects that have an active Motion Vector pass assigned to their Material and did not move since the last frame. This flag can be used to render both moving objects and not moving objects in the motion vector pass to populate object motion data and scene depth data together.
Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a simple render loop in a custom render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-creating-simple-render-loop.html).
* * *
