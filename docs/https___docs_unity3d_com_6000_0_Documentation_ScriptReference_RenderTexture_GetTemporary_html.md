* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).GetTemporary
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
## Declaration
public static [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) GetTemporary([RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) desc); 
## Declaration
public static [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) GetTemporary(int width, int height, int depthBuffer = 0, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format = RenderTextureFormat.Default, [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) readWrite = RenderTextureReadWrite.Default, int antiAliasing = 1, [RenderTextureMemoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureMemoryless.html) memorylessMode = RenderTextureMemoryless.None, [VRTextureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.html) vrUsage = VRTextureUsage.None, bool useDynamicScale = false); 
### Parameters
Parameter | Description  
---|---  
width | Width in pixels.  
height | Height in pixels.  
depthBuffer | Depth buffer bits (0, 16 or 24). Note that only 24 bit depth has stencil buffer.  
format | Render texture format.  
readWrite | Color space conversion mode.  
antiAliasing | Number of antialiasing samples to store in the texture. Valid values are 1, 2, 4, and 8. Throws an exception if any other value is passed.  
memorylessMode | Render texture memoryless mode.  
vrUsage | How Unity uses the RenderTexture as a VR eye texture. The default is [VRTextureUsage.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.None.html).  
useDynamicScale | Determines whether Unity scales the render texture using [dynamic resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution.html). The default is `false`.  
desc | Use this RenderTextureDesc for the settings when creating the temporary RenderTexture.  
### Description
Allocate a temporary render texture.
This function is optimized for when you need a quick RenderTexture to do some temporary calculations. Release it using [ReleaseTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ReleaseTemporary.html) as soon as you're done with it, so another call can start reusing it if needed.  
  
Internally Unity keeps a pool of temporary render textures, so a call to GetTemporary most often just returns an already created one (if the size and format matches). These temporary render textures are actually destroyed when they aren't used for a couple of frames.  
  
If you are doing a series of post-processing "blits", it's best for performance to get and release a temporary render texture for each blit, instead of getting one or two render textures upfront and reusing them. This is mostly beneficial for mobile (tile-based) and multi-GPU systems: GetTemporary will internally do a [DiscardContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.DiscardContents.html) call which helps to avoid costly restore operations on the previous render texture contents.  
  
You can not depend on any particular contents of the RenderTexture you get from GetTemporary function. It might be garbage, or it might be cleared to some color, depending on the platform.  
  
Additional resources: [ReleaseTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ReleaseTemporary.html).
* * *
