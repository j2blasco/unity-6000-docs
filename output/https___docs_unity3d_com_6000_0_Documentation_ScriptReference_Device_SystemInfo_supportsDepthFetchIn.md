* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsDepthFetchInRenderPass.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo.html).supportsDepthFetchInRenderPass
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
supportsDepthFetchInRenderPass; 
### Description
Indicates whether RenderPass can use its depth attachment as input. (Read Only)
When RenderPass is emulated (e.g. D3D11 or OpenGL Core) this is always possible since the temporary copy will be used. When native RenderPass is used it depends on the platform support; for example Metal disallows reading from depth attachment.
* * *
