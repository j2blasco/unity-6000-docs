* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D-ctor.html

# Texture3D Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html "Go to Texture3D Component in the Manual")
## Declaration
public Texture3D(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain, bool createUninitialized = false); 
## Declaration
public Texture3D(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain, IntPtr nativeTex = IntPtr.Zero); 
## Declaration
public Texture3D(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, IntPtr nativeTex = IntPtr.Zero); 
## Declaration
public Texture3D(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, IntPtr nativeTex = IntPtr.Zero, bool createUninitialized = false); 
### Parameters
Parameter | Description  
---|---  
width | Width of texture in pixels.  
height | Height of texture in pixels.  
depth | Depth of texture in pixels.  
textureFormat | Texture data format.  
mipChain | Determines whether the texture has mipmaps or not. A value of 1 (true) means the texture does have mipmaps, and a value of 0 (false) means the texture doesn't have mipmaps.  
nativeTex | External native texture pointer to use. Defaults to generating its own internal native texture.  
mipCount | Amount of mipmaps to allocate for the texture.  
createUninitialized | Use this flag to create the texture with uninitialized data. When overriding all texels anyway, this can lead to improved performance and reduced memory usage.  
### Description
Create a new empty 3D Texture.
3D textures can be thought of as a box of pixels, with width, height and depth. Note that large textures can consume a lot of memory, for example a 1024x512x256 texture with [TextureFormat.ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ARGB32.html) format and no mipmaps will consume 512MB of memory.  
  
Note that this class does not support Texture3D creation with a Crunch compression [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).  
  
Enable `createUninitialized` to make the texture reference uninitialized data (both on the CPU and GPU). When overriding all texels, this can lead to improved performance and reduced memory usage during construction. Note that sampling an uninitialized texture gives unpredictable values.  
  
Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels32.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) functions.
* * *
