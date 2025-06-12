* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildQuality.html

# GpuBvhBuildQuality
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
BVH build quality.
The quality levels represent a trade-off between acceleration structure build performance and ray tracing performance. The slower the acceleration structure build speed, the higher the runtime ray tracing performance is.
### Properties
Property | Description  
---|---  
[Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildQuality.Low.html) | Faster build time, slower ray tracing performance. Can be beneficial for dynamic scenes.  
[Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildQuality.Medium.html) | This level balances the build time and ray tracing performance.  
[High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildQuality.High.html) | Highest possible ray tracing performance, slowest build time. This quality level uses spatial splits when enabled.  
* * *
