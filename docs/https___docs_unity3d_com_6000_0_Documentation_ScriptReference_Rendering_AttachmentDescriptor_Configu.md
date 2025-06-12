* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.ConfigureTarget.html

#  [AttachmentDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html).ConfigureTarget
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
public void ConfigureTarget([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) target, bool loadExistingContents, bool storeResults); 
### Parameters
Parameter | Description  
---|---  
tgt | The surface to use as the backing storage for this AttachmentDescriptor.  
loadExistingContents | Whether to read in the existing contents of the surface when the RenderPass starts.  
storeResults | Whether to store the rendering results of the attachment when the RenderPass ends.  
### Description
Binds this AttachmentDescriptor to the given target surface.
This method sets the backing storage of this AttachmentDescriptor to the given target surface.  
  
If loadExistingContents is true, changes [loadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-loadAction.html) to RenderBufferStoreAction.Load unless the load action is already set to RenderBufferStoreAction.Clear, in which case this parameter is ignored.  
  
If `storeResults` is true, changes [storeAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-storeAction.html) to either [RenderBufferStoreAction.Store](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.Store.html) or [RenderBufferStoreAction.StoreAndResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) depending on whether the `resolveAttachment` was configured or not.  
  
Note: If you call both [ConfigureResolveTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.ConfigureResolveTarget.html) with `storeResults` set to `true` and `ConfigureTarget`, Unity stores both the resolved and unresolved MSAA surfaces respectively in `resolveTarget` and `loadStoreTarget`. This means Unity writes more data to memory.
* * *
