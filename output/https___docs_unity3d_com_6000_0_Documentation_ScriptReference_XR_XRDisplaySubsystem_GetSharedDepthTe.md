* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetSharedDepthTextureForRenderPass.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).GetSharedDepthTextureForRenderPass
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
public [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) GetSharedDepthTextureForRenderPass(int renderPass); 
### Parameters
Parameter | Description  
---|---  
renderPass | The render pass index to get the shared depth buffer render texture for.  
### Returns
**RenderTexture** The shared depth buffer render texture associated with that render pass, or null if not found. 
### Description
Given a render pass, return the shared depth buffer RenderTexture instance backing that render pass. If the render pass is invalid, or if the render texture does not exist, return null.
* * *
