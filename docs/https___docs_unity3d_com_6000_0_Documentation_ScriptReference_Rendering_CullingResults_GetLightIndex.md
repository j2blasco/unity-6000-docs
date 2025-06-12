* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.GetLightIndexMap.html

#  [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).GetLightIndexMap
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
## Declaration
public NativeArray<int> GetLightIndexMap([Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
allocator | The allocator to use.  
### Returns
**NativeArray <int>** Array of indices that map from [VisibleLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight.html) indices to internal per-object light list indices. 
### Description
If a [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) sorts or otherwise modifies the [VisibleLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight.html) list, an index remap will be necessary to properly make use of per-object light lists.
Additional resources:: [CullingResults.SetLightIndexMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.SetLightIndexMap.html), [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).
* * *
