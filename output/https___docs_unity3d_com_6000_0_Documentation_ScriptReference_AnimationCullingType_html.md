* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCullingType.html

# AnimationCullingType
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
This enum controlls culling of Animation component.
When culling is enabled, Unity might stop animating if it thinks that the results of the animation won't be visible to the user. This could save you some performance if you have things animating outside of the viewport, whose animation is only important when the user can actually see the thing that is being animated. When Animation component is culled it won't do anything: it won't update animation states, execute events or sample animations.
### Properties
Property | Description  
---|---  
[AlwaysAnimate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCullingType.AlwaysAnimate.html) | Animation culling is disabled - object is animated even when offscreen.  
[BasedOnRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCullingType.BasedOnRenderers.html) | Animation is disabled when renderers are not visible.  
* * *
