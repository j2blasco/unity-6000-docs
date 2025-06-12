* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-useViewFrustumForShadowCasterCull.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).useViewFrustumForShadowCasterCull
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
useViewFrustumForShadowCasterCull; 
### Description
Whether to cull shadows for this Light when the Light is outside of the view frustum.
Set this to true to calculate shadows for the Light only when it is within the view frustum, and cull shadows for this Light when it is outside the view frustum. This is the default behavior.  
  
Set this to false to calculate shadows for this Light, regardless of whether it is within the view frustum or not. This is useful if you are caching shadow maps; you can calculate shadows for a number of Lights that are not visible within the same view frustum, and continue to use the shadow map as the view changes.  
  
When you set this to false, Unity performs the same culling calculations as before but with an effectively infinite view frustum.
* * *
