* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetMaterialProperty.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).targetMaterialProperty
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
targetMaterialProperty; 
### Description
[Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) texture property which is targeted when [VideoPlayer.renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-renderMode.html) is set to Video.VideoTarget.MaterialOverride.
The video is sent to every [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) in the [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) that has the targeted texture property. When this property is empty, the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) uses the name of the material's first [main texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html). If no main texture is found, the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) uses the name of the material's first texture property.
* * *
