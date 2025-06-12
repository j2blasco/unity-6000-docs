* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-splitExclusionMask.html

#  [BatchCullingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html).splitExclusionMask
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
splitExclusionMask; 
### Description
A bitmask that represents the [BatchCullingContext.cullingSplits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingSplits.html) Unity ignores in a [BatchDrawCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand.html) struct.
The bitmask is 8 bits. A bit value of 1 means Unity ignores the culling split. The least significant bit corresponds to the first culling split in the [BatchCullingContext.cullingSplits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-cullingSplits.html) array, and each successive bit corresponds to the next culling split, up to a maximum of six bits. This means that any of the bits set to 1 in the exclusion mask do not need to be set in the BatchDrawCommand.splitMask either.
* * *
