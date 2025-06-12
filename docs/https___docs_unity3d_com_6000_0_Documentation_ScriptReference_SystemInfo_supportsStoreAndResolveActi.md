* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsStoreAndResolveAction.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).supportsStoreAndResolveAction
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
supportsStoreAndResolveAction; 
### Description
This property is true if the graphics API of the target build platform takes [RenderBufferStoreAction.StoreAndResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) into account, false if otherwise.
Use this property to check if [RenderBufferStoreAction.StoreAndResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) results in GPU storing the multisampled render target content.  
  
If false, the [RenderBufferStoreAction.StoreAndResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) store actions fall back to [RenderBufferStoreAction.Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.Resolve.html).  
  
Use this property to ensure that any multisampled render target content is stored and can be loaded correctly by any following [RenderBufferLoadAction.Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.Load.html) load action.
* * *
