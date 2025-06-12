* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.TextureStreaming.html

#  [DrawCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.html).TextureStreaming
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
The camera is set to run in texture streaming debug mode.
In debug mode, a green tint on the texture indicates mipmaps were dropped/discarded but the mipmap level is still sufficient for rendering on screen (the color will be brighter when more mipmaps are dropped, indicating a saving in GPU memory use). A Red tinted texture indicates texture memory restrictions have resulted in the desired mipmap being dropped (the brighter the tint, the further from desired value) and the mipmap level is no longer sufficient to maintain visual quality. No tint indicates that the mipmap level has not changed from its original value.
* * *
