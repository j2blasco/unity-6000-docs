* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions.html

# GpuBvhBuildOptions
struct in UnityEditor.Embree
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
Options for bounding volume hierarchy (BVH) build.
### Properties
Property | Description  
---|---  
[allowPrimitiveSplits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-allowPrimitiveSplits.html) | With this option enabled, Unity performs spatial splits. This increases the memory footprint, but the resulting BVH makes the ray tracing stage faster.  
[isTopLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-isTopLevel.html) | With this option enabled, Unity builds a top level BVH (for instances). When disabled, it builds a bottom level BVH (for a Mesh).  
[maxLeafSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-maxLeafSize.html) | The maximum number of primitives allowed in a leaf node.  
[minLeafSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-minLeafSize.html) | The minimum number of primitives allowed in a leaf node.  
[quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-quality.html) | BVH build quality.  
* * *
