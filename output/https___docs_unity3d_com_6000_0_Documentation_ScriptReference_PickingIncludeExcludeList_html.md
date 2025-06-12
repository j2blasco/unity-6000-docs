* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html

# PickingIncludeExcludeList
struct in UnityEditor
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
Represents a list of Unity Object and [DOTS Entity](https://docs.unity3d.com/Packages/com.unity.entities@latest/index.html?subfolder=/manual/ecs_entities.html) IDs that picking algorithms can either consider or discard.
### Properties
Property | Description  
---|---  
[ExcludeEntities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.ExcludeEntities.html) | An array of DOTS Entity IDs that the picking algorithm doesn't consider when it selects the nearest object.  
[ExcludeRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.ExcludeRenderers.html) | An array of GameObjects that the picking algorithm doesn't consider when it selects the nearest object.  
[IncludeEntities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.IncludeEntities.html) | An array of DOTS Entity IDs that the picking algorithm exclusively considers when it selects the nearest object. If this is null, Unity considers all DOTS Entities in open scenes for selection.  
[IncludeRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.IncludeRenderers.html) | An array of GameObjects that the picking algorithm exclusively considers when it selects the nearest object. If this is null, Unity considers all GameObjects in open scenes for selection.  
### Constructors
Constructor | Description  
---|---  
[PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList-ctor.html) | Construct a PickingIncludeExcludeList.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.Dispose.html) | Dispose all the Unity.Collections.NativeArray inside the struct.  
* * *
