* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetPickingIncludeExcludeList.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).GetPickingIncludeExcludeList
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
public static [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) GetPickingIncludeExcludeList([Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
allocator | The allocator to use to create the [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) object.  
### Returns
**PickingIncludeExcludeList** The [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) struct. 
### Description
Gets the picking [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) for the currently executing BatchRendererGroup.OnPerformCulling callback.
**Note** : If you call this method outside of a BatchRendererGroup.OnPerformCulling callback, it returns an empty [PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) object.
* * *
