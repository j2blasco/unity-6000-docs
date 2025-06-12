* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-ctor.html

# Texture2DArray Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html "Go to Texture2DArray Component in the Manual")
## Declaration
public Texture2DArray(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain, bool linear = false); 
## Declaration
public Texture2DArray(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain, bool linear = false, bool createUninitialized = false); 
## Declaration
public Texture2DArray(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear); 
## Declaration
public Texture2DArray(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear, bool createUninitialized); 
## Declaration
public Texture2DArray(int width, int height, int depth, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear, bool createUninitialized, [MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html) mipmapLimitDescriptor); 
### Parameters
Parameter | Description  
---|---  
width | Width of texture array in pixels.  
height | Height of texture array in pixels.  
depth | Number of elements in the texture array.  
linear | Does the texture contain non-color data (i.e. don't do any color space conversions when sampling)? Default is false.  
textureFormat | Format of the texture.  
mipChain | Should mipmaps be created?  
mipCount | Amount of mips to allocate for the texture array.  
createUninitialized | Use this flag to create the texture with uninitialized data. When overriding all texels anyway, this can lead to improved performance and reduced memory usage.  
mipmapLimitDescriptor | Determines whether the texture uses a mipmap limit, and which mipmap limit to use. See [MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html)  
### Description
Create a new texture array.
Enable `createUninitialized` to make the texture reference uninitialized data (both on the CPU and GPU). When overriding all texels, this can lead to improved performance and reduced memory usage during construction. Note that sampling an uninitialized texture gives unpredictable values.  
  
Usually you will want to set the colors of the texture after creating it. Use [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.SetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.SetPixels32.html) or [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) functions for that.  
  
Note that this class does not support Texture2DArray creation with a Crunch compression [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).  
  
When you enable mipmap limits with a `mipmapLimitDescriptor`, a readable CPU copy is required for the texture to reupload when quality settings change. If the texture is made nonreadable (see [Texture2DArray.Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.Apply.html)), the uploaded resolution will no longer adapt to the active quality level.
* * *
