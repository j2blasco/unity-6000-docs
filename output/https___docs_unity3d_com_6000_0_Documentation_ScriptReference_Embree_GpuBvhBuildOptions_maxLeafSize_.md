* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions-maxLeafSize.html

#  [GpuBvhBuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions.html).maxLeafSize
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
maxLeafSize; 
### Description
The maximum number of primitives allowed in a leaf node.
If this value is more than 1, the BVH builder can pack multiple triangles into a node, but it only does so when the increase preserves the traversal performance. Default value: 1.
* * *
