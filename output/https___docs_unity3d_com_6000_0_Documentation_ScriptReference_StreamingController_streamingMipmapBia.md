* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StreamingController-streamingMipmapBias.html

#  [StreamingController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StreamingController.html).streamingMipmapBias
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
streamingMipmapBias; 
### Description
Offset applied to the mipmap level chosen by the texture streaming system for any textures visible from this camera. This Offset can take either a positive or negative value.
When texture streaming is active, Unity loads mipmap levels for textures based on their distance from all active cameras. This bias is added to all textures visible from this camera and allows you to force smaller or larger mipmap levels to be loaded for textures visible from this camera.
* * *
