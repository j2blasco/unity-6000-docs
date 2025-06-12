* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-limitLightmapCount.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).limitLightmapCount
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
limitLightmapCount; 
### Description
If enabled, objects sharing the same lightmap parameters will be packed into [LightmapParameters.maxLightmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-maxLightmapCount.html) lightmaps.
This setting can be used to limit the number of generated lightmaps. This is achieved by iteratively scaling down the UV layouts until they fit into the specified number of allowed lightmaps.
* * *
