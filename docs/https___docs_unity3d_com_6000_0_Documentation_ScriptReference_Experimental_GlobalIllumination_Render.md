* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.RenderSettings-useRadianceAmbientProbe.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.RenderSettings.html).useRadianceAmbientProbe
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
useRadianceAmbientProbe; 
### Description
If enabled, ambient trilight will be sampled using the old radiance sampling method.
This feature is here to maintain backwards compatibility for real-time ambient light when using the trilight mode. The new default behavior now uses the correct sampling behavior. Please note that the new sampling method is slower.
* * *
