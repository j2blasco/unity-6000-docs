* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.DynamicallyScalableExplicit.html

#  [RenderTextureCreationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.html).DynamicallyScalableExplicit
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
Set this flag to mark this RenderTexture for Dynamic Resolution, if the target platform/graphics API supports Dynamic Resolution.
If you set this flag, you need to scale the render texture manually, instead of using `ScalableBufferManager.ResizeBuffers`. This flag is mutually exclusive with [RenderTextureCreationFlags.DynamicallyScalable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.DynamicallyScalable.html). Refer to [RenderTexture.ApplyDynamicScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ApplyDynamicScale.html) and [Dynamic resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution.html) for more details.
* * *
