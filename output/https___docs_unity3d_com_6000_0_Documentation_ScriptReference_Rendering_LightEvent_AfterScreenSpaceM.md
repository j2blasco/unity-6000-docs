* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.AfterScreenspaceMask.html

#  [LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html).AfterScreenspaceMask
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
After directional light screenspace shadow mask is computed.
Directional lights when using non-mobile shadows "gather" shadowmap into a screenspace buffer and do PCF filtering during this step. Later on actual object rendering just samples this screenspace buffer.  
  
This light event will execute command buffers when the screenspace mask is computed, and the active render target is still the screenspace mask.
* * *
