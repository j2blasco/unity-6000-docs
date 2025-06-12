* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetTexture.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).targetTexture
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
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) targetTexture; 
### Description
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) to draw to when [VideoPlayer.renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-renderMode.html) is set to Video.VideoTarget.RenderTexture.
If the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) is of [TextureDimension.Tex2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TextureDimension.Tex2D.html) the video frames will be drawn directly into this target. For optimal performance, [RenderTexture.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-width.html) and [RenderTexture.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-height.html) should match those of the video media exactly.  
  
If the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) is of [TextureDimension.Cube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TextureDimension.Cube.html) the video frames will be interpreted as a cubemap in one of the 4 supported layouts (horizontal or vertical orientation of a cross or strip layout) based on video aspect ratio. The cubemap faces of the video frame are drawn to the 6 faces of the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html). For a one-to-one pixel mapping, [RenderTexture.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-width.html) and [RenderTexture.height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-height.html) should match the size of the individual faces contained within the video media's cubemap (eg. for a 2048x1536 horizontal cross cubemap video, the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) cube size should be set to 512x512).
* * *
