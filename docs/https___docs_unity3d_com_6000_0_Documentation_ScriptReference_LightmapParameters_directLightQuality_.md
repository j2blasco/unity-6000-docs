* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-directLightQuality.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).directLightQuality
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
directLightQuality; 
### Description
The number of rays used for lights with an area. Allows for accurate soft shadowing.
This is the maximum number of rays to trace to any light with an area. Larger lights will require more rays to produce a noise-free output. The default value works with the majority of Scene setups, but you should increase this value if you observe noise. It can have a significant impact on performance, and for Scenes with lots of area lights, halving this value halves the baking time.
* * *
