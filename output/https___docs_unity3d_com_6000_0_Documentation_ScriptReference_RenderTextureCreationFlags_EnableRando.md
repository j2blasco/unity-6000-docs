* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.EnableRandomWrite.html

#  [RenderTextureCreationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.html).EnableRandomWrite
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
Set this flag to enable random access writes to the RenderTexture from shaders. Normally, pixel shaders only operate on pixels they are given. Compute shaders cannot write to textures without this flag. Random write enables shaders to write to arbitrary locations on a RenderTexture. See [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html) for more details, including supported platforms.
* * *
