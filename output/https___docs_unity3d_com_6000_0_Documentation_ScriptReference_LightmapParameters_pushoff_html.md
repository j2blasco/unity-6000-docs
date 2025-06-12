* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-pushoff.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).pushoff
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
pushoff; 
### Description
The distance to offset the ray origin from the geometry when performing ray tracing, in modelling units. Unity applies the offset to all baked lighting: direct lighting, indirect lighting, environment lighting and ambient occlusion.
Changing the value of the offset can fix unwanted artifacts on faraway geometry that are the result of limited floating point precision. These artifacts resemble incorrect ambient occlusion or shadowing.  
  
The range of valid values is 0.0 - 1.0, inclusive. 
* * *
