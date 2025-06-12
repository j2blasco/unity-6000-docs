* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-memorylessMode.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).memorylessMode
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
[RenderTextureMemoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureMemoryless.html) memorylessMode; 
### Description
The render texture memoryless mode property.
Use this property to set or return the render texture memoryless modes.  
  
Memoryless render textures are temporarily stored in the on-tile memory when it is rendered. It does not get stored in CPU or GPU memory. This reduces memory usage of your app but note that you cannot read or write to these render textures.  
  
On-tile memory is a high speed dedicated memory used by mobile GPUs when rendering.  
  
Note that memoryless render textures are only supported when using the Metal or Vulkan graphics APIs on iOS 10+, tvOS 10+, and visionOS. Render textures are read/write protected and stored in CPU or GPU memory on other platforms.  
  
Additional resources: [RenderTextureMemoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureMemoryless.html).
* * *
