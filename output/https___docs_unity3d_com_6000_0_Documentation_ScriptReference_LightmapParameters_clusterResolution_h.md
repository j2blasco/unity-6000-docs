* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-clusterResolution.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).clusterResolution
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
clusterResolution; 
### Description
Controls the resolution at which Enlighten Realtime Global Illumination stores and can transfer input light.
Typically this resolution can be slightly lower than the resolution of the real-time lightmap without significantly reducing the final quality, although this depends on the kinds of lighting environments you wish to use. Small, bright light sources will require a higher clusterResolution for Enlighten Realtime Global Illumination to capture them accurately.  
  
  
  
Cluster resolution is multiplied by the real-time lightmap resolution. A high value means a higher cluster resolution. A value of 1 matches each texel in the real-time lightmap with one input cluster.  
  
  
  
Using a very small cluster resolution results in light being smeared across the output texels. Larger values do not significantly increase quality (as they have to be averaged for the final output texel), but can cause unnecessary increases in time and memory footprint.
* * *
