* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipMapBias.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).mipMapBias
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
mipMapBias; 
### Description
The mipmap bias of the Texture.
A positive bias makes a Texture appear extra blurry, while a negative bias sharpens the Texture.  
  
Note that using large negative bias can reduce performance, so it's not recommended to use more than -0.5 negative bias. In most cases you can achieve better sharpening of the Texture by using anisotropic filtering.  
  
Mipmap bias doesn't work with the following: 
  * MaterialPropertyBlocks.
  * Some graphics APIs. For example Metal, or OpenGL ES unless you use custom shaders.


Additional resources: [Texture.anisoLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-anisoLevel.html), [Texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html).
* * *
