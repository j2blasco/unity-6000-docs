* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html

# AttachmentDescriptor
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
A declaration of a single color or depth rendering surface to be attached into a RenderPass.
A AttachmentDescriptor object identifies a single color or depth rendering surface that can be used with a RenderPass. Note that the AttachmentDescriptor object derives from UnityEngine.Object so they do not get garbage collected like normal C# objects. Instead, they are only GC'd when unloading a Scene or when Resources.UnloadUnusedAssets() is called. Therefore do not create these objects each frame: Instead, create these objects in the constructor of your rendering class, and reuse those objects each frame.
### Properties
Property | Description  
---|---  
[clearColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-clearColor.html) | The currently assigned clear color for this attachment. Default is black.  
[clearDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-clearDepth.html) | Currently assigned depth clear value for this attachment. Default value is 1.0.  
[clearStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-clearStencil.html) | Currently assigned stencil clear value for this attachment. Default is 0.  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-format.html) | The format of this attachment.  
[graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-graphicsFormat.html) | The GraphicsFormat of this attachment. To use in place of format.  
[loadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-loadAction.html) | The load action to be used on this attachment when the RenderPass starts.  
[loadStoreTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-loadStoreTarget.html) | The surface to use as the backing storage for this AttachmentDescriptor.  
[resolveTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-resolveTarget.html) | When the renderpass that uses this attachment ends, resolve the MSAA surface into the given target.  
[storeAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-storeAction.html) | The store action to use with this attachment when the RenderPass ends. Only used when either ConfigureTarget or ConfigureResolveTarget has been called.  
### Constructors
Constructor | Description  
---|---  
[AttachmentDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-ctor.html) | Create a AttachmentDescriptor to be used with RenderPass.  
### Public Methods
Method | Description  
---|---  
[ConfigureClear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.ConfigureClear.html) | When the RenderPass starts, clear this attachment into the color or depth/stencil values given (depending on the format of this attachment). Changes loadAction to RenderBufferLoadAction.Clear.  
[ConfigureResolveTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.ConfigureResolveTarget.html) | When the renderpass that uses this attachment ends, resolve the MSAA surface into the given target.  
[ConfigureTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.ConfigureTarget.html) | Binds this AttachmentDescriptor to the given target surface.  
* * *
