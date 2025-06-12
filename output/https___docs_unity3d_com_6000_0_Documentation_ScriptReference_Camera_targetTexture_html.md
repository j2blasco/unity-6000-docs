* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).targetTexture
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) targetTexture; 
### Description
Destination render texture.
Usually cameras render directly to screen, but for some effects it is useful to make a camera render into a texture. This is done by creating a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) object and setting it as [targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html) on the camera. The camera will then render into that texture.  
  
When targetTexture is `null`, camera renders to screen.  
  
When rendering into a texture, the camera always renders into the whole texture; effectively [rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-rect.html) and [pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelRect.html) are ignored.  
  
It is also possible to make camera render into separate [RenderBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html), or into multiple textures at once, using [SetTargetBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetTargetBuffers.html) function.  
  
Additional resources: [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), [SetTargetBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetTargetBuffers.html).
* * *
