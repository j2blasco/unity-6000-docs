* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-ctor.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).RenderTexture Constructor
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
public RenderTexture([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) textureToCopy); 
## Declaration
public RenderTexture([RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) desc); 
## Declaration
public RenderTexture(int width, int height, int depth, [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format = RenderTextureFormat.Default, [RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) readWrite = RenderTextureReadWrite.Default); 
### Parameters
Parameter | Description  
---|---  
width | Texture width in pixels.  
height | Texture height in pixels.  
depth | Number of bits in depth buffer (0, 16, 24 or 32). Note that only 24 and 32 bit depth have stencil buffer support.  
format | Texture color format.  
colorFormat | The color format for the RenderTexture.  
depthStencilFormat | The depth stencil format for the RenderTexture.  
mipCount | Amount of mips to allocate for the RenderTexture.  
readWrite | How color space conversions are applied on texture read/write.  
desc | Create the RenderTexture with the settings in the RenderTextureDescriptor.  
textureToCopy | Copy the settings from another RenderTexture.  
### Description
Creates a new RenderTexture object.
The render texture is created with `width` by `height` size, with a depth buffer of `depth` bits (depth can be 0, 16, 24 or 32), and in `format` format and with sRGB read / write on or off.  
  
Note that constructing a RenderTexture object does not create the hardware representation immediately. The actual render texture is created upon first use or when [Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Create.html) is called manually. So after constructing the render texture, it is possible to set additional variables, like [format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-graphicsFormat.html), [dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-dimension.html) and so on.  
  
Also note that your graphics device capabilities determine the maximum size of a RenderTexture. To determine the maximum size, use [SystemInfo.maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureSize.html) for 2D and cubemap RenderTextures, [SystemInfo.maxTexture3DSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTexture3DSize.html) for 3D RenderTextures, and [SystemInfo.maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureSize.html) and [SystemInfo.maxTextureArraySlices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureArraySlices.html) for 2D array RenderTextures.  
  
When the requested size exceeds the maximum size, Unity's behavior varies. If the RenderTexture is not a 3D texture, and the requested size is a power of two, Unity automatically scales down the requested size by a factor of 2 until it is below the maximum, and then creates the RenderTexture at that size. Otherwise, Unity fails to create the RenderTexture, and throws an error.  
  
Additional resources: [format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-graphicsFormat.html), [GetTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) rt;  
  
    void  Start()
    {
        rt = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(256, 256, 16, RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
    }
}

```

* * *
