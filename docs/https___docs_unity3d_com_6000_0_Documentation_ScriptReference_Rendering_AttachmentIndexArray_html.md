* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray.html

# AttachmentIndexArray
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
Struct encapsulating a fixed list of attachment indices used when declaring native render passes.
This fixed size struct allows for non-GC declaration of the required indices. Indices point into the attachment list as pass to [CommandBuffer.BeginRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginRenderPass.html)  
  
Additional resources: [CommandBuffer.BeginRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.BeginRenderPass.html).
### Static Properties
Property | Description  
---|---  
[Emtpy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray.Emtpy.html) | Utility to declare an empty index array.  
[MaxAttachments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray.MaxAttachments.html) | Maximum number of indices this struct can hold. This is directly tied to the maximum number of attachments in a native render pass (8).  
### Properties
Property | Description  
---|---  
[Length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray.Length.html) | Number of elements in the AttachmentIndexArrayp.  
### Constructors
Constructor | Description  
---|---  
[AttachmentIndexArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray-ctor.html) | Create and initialize a new AttachmentIndexArray.  
* * *
