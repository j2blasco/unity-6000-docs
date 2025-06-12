* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-blurRadius.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).blurRadius
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html "Go to LightmapParameters Component in the Manual")
blurRadius; 
### Description
The radius (in texels) of the post-processing filter that blurs baked direct lighting.
The filter is aware of geometry and visibility between texels and thus light leaking is reduced. In general, a value in the range from 2 to 8 leads to good results. Note that the processing time depends on the filter size squared and thus larger values should be avoided.
* * *
