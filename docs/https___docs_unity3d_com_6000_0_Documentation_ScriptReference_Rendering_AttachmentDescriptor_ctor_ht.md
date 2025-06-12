* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor-ctor.html

# AttachmentDescriptor Constructor
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
public AttachmentDescriptor([RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format); 
## Declaration
public AttachmentDescriptor([Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format); 
## Declaration
public AttachmentDescriptor([RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) target, bool loadExistingContents, bool storeResults, bool resolve); 
### Parameters
Parameter | Description  
---|---  
fmt | The format of this attachment.  
### Description
Create a AttachmentDescriptor to be used with RenderPass.
* * *
