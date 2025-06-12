* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.GetNativeRenderBufferPtr.html

#  [RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html).GetNativeRenderBufferPtr
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
public IntPtr GetNativeRenderBufferPtr(); 
### Description
Returns native RenderBuffer. Be warned this is not native Texture, but rather pointer to unity struct that can be used with native unity API. Currently such API exists only on iOS.
* * *
