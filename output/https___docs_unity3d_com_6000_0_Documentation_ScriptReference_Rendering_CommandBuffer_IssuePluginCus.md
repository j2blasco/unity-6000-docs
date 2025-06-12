* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginCustomBlit.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).IssuePluginCustomBlit
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
public void IssuePluginCustomBlit(IntPtr callback, uint command, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) source, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dest, uint commandParam, uint commandFlags); 
### Parameters
Parameter | Description  
---|---  
callback | Native code callback to queue for Unity's renderer to invoke.  
command | User defined command id to send to the callback.  
source | Source render target.  
dest | Destination render target.  
commandParam | User data command parameters.  
commandFlags | User data command flags.  
### Description
Send a user-defined blit event to a native code plugin.
* * *
