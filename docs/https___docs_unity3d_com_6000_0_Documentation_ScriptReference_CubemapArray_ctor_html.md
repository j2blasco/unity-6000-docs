* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray-ctor.html

# CubemapArray Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray.html "Go to CubemapArray Component in the Manual")
## Declaration
public CubemapArray(int width, int cubemapCount, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain); 
## Declaration
public CubemapArray(int width, int cubemapCount, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain, bool linear = false, bool createUninitialized = false); 
## Declaration
public CubemapArray(int width, int cubemapCount, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear); 
## Declaration
public CubemapArray(int width, int cubemapCount, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear, bool createUninitialized = false); 
### Parameters
Parameter | Description  
---|---  
cubemapCount | Number of elements in the cubemap array.  
linear | Does the texture contain non-color data (i.e. don't do any color space conversions when sampling)? Default is false.  
width | Width of each cubemap face.  
textureFormat | Format of the cubemaps.  
mipChain | Should mipmaps be generated ?  
mipCount | Amount of mipmaps to generate.  
createUninitialized | Use this flag to create the texture with uninitialized data. When overriding all texels anyway, this can lead to improved performance and reduced memory usage.  
### Description
Create a new cubemap array.
Enable `createUninitialized` to make the texture reference uninitialized data (both on the CPU and GPU). When overriding all texels, this can lead to improved performance and reduced memory usage during construction. Note that sampling an uninitialized texture gives unpredictable values.  
  
Usually you will want to set the colors of the cubemaps after creating it. Use [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels32.html) or [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) functions for that.  
  
Note that this class does not support CubemapArray creation with a Crunch compression [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).
* * *
