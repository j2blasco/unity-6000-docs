* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.html

# BatchCullingViewType
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
The type of an object that is requesting culling.
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.Unknown.html) | The type of the object that is requesting culling is unknown.  
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.Camera.html) | A Camera is requesting culling.  
[Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.Light.html) | A shadow-casting Light is requesting culling.  
[Picking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.Picking.html) | The Scene view is requesting culling so that it can render object picking data. Unity calls the OnPerformCulling() with this enum value when a user clicks in the Scene view.  
[SelectionOutline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.SelectionOutline.html) | The Scene view is requesting culling so that it can render the selection outline of the objects currently picked. Unity calls the OnPerformCulling() with this enum value when rendering the selection outline.  
[Filtering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.Filtering.html) | The Scene view is requesting culling so that it can render filtered objects. Unity calls the OnPerformCulling() with this enum value when a user writes a search query in the Hierarchy window.  
* * *
