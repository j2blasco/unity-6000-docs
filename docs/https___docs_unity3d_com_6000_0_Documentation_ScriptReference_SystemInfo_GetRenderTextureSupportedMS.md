* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetRenderTextureSupportedMSAASampleCount.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).GetRenderTextureSupportedMSAASampleCount
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
public static int GetRenderTextureSupportedMSAASampleCount([RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) desc); 
### Parameters
Parameter | Description  
---|---  
desc | The [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) to check.  
### Returns
**int** If the target platform supports the given MSAA samples count of [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html), returns the given MSAA samples count. Otherwise returns a lower fallback MSAA samples count value that the target platform supports. 
### Description
Checks if the target platform supports the MSAA samples count in the [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) argument.
Additional resources: [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html)
* * *
