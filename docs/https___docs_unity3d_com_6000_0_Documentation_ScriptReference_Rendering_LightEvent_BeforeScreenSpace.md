* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.BeforeScreenspaceMask.html

#  [LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html).BeforeScreenspaceMask
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
Before directional light screenspace shadow mask is computed.
Directional lights when using non-mobile shadows "gather" shadowmap into a screenspace buffer and do PCF filtering during this step. Later on actual object rendering just samples this screenspace buffer.  
  
This light event executes command buffers when the screen-space mask render target is set and cleared, and the shadow cascade parameters are set. Note that the shadow mask is not yet computed.
* * *
