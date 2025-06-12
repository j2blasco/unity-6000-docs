* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList-ctor.html

# PickingIncludeExcludeList Constructor
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
public PickingIncludeExcludeList(List<int> includeRendererInstanceIDs, List<int> excludeRendererInstanceIDs, List<int> includeEntityIndices, List<int> excludeEntityIndices, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
includeRendererInstanceIDs | UnityEngine.Renderer instanceIDs to be included.  
excludeRendererInstanceIDs | UnityEngine.Renderer instanceIDs to be excluded.  
includeEntityIndices | DOTS Entity indices to be included.  
excludeEntityIndices | DOTS Entity indices to be excluded.  
allocator | Allocator to use to construct the four Unity.Collections.NativeArray of the [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html).  
### Description
Construct a [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html).
* * *
