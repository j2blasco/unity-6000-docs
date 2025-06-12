* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html

# RenderPickingResult
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
This struct contains information to notify Unity the outcome of this render picking callback.
This struct type has to be returned from the [RenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RenderPickingCallback.html) to notify Unity of: 
  * The number of consecutive picking indices used during the callback
  * The [ResolvePickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingCallback.html) delegate to invoke when the user clicks on a pixel, whose value is the `selectionId` encoded from the picking index used during the callback. Refer to [resolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolver.html) for more information.
  * Alternatively, you can use a [ResolvePickingWithWorldPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingWithWorldPositionCallback.html) delegate if you need the world space position or the depth value for the resolve callback to work. Refer to [resolverWithWorldPos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolverWithWorldPos.html).


If nothing has been rendered, return [RenderPickingResult.NoOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.NoOperation.html).
### Static Properties
Property | Description  
---|---  
[NoOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.NoOperation.html) | The constant value to be returned from RenderPickingCallback delegates signifying that nothing has been rendered.  
### Properties
Property | Description  
---|---  
[renderedPickingIndexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-renderedPickingIndexCount.html) | The number of consecutive picking indices used during the current RenderPickingCallback.  
[resolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolver.html) | The callback to invoke to resolve a picking index into a GameObject reference.  
[resolverWithWorldPos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-resolverWithWorldPos.html) | The callback to invoke to resolve a picking index into a GameObject reference.  
### Constructors
Constructor | Description  
---|---  
[RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult-ctor.html) | Constructs a RenderPickingResult value.  
* * *
