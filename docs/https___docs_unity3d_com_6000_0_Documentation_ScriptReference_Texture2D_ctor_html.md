* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-ctor.html

# Texture2D Constructor
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
## Declaration
public Texture2D(int width, int height); 
### Description
Create a new empty texture.
The texture will be `width` by `height` size, with an RGBA32 [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html), with mipmaps and in sRGB color space.  
  
Usually you will want to set the colors of the texture after creating it, using [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) and [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
```
// Create a new texture and assign it to the renderer's material
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(128, 128);
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        renderer.material.mainTexture = texture;
    }
}

```

Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
* * *
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, bool mipChain); 
### Description
Create a new empty texture.
The texture will be `width` by `height` size, with a given `format`, with mipmaps or without. `width` and `height` must be greater than 0.  
  
Usually you will want to set the colors of the texture after creating it, using [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) and [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.  
  
Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
* * *
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat = TextureFormat.RGBA32, int mipCount = -1, bool linear = false); 
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat = TextureFormat.RGBA32, bool mipChain = true, bool linear = false); 
### Description
Create a new empty texture.
The texture will be `width` by `height` size, with a given `format`, with mipmaps or without, and in either the linear color space or the sRGB color space. `width` and `height` must be greater than 0.  
  
Usually you will want to set the colors of the texture after creating it, using [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) and [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.  
  
Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
* * *
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat = TextureFormat.RGBA32, int mipCount = -1, bool linear = false, bool createUninitialized = false); 
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat = TextureFormat.RGBA32, bool mipChain = true, bool linear = false, bool createUninitialized = false); 
### Description
Create a new empty texture.
The texture will be `width` by `height` size, with a given `format`, with mipmaps or without, and in either the linear color space or the sRGB color space. `width` and `height` must be greater than 0.  
  
Enable `createUninitialized` to make the texture reference uninitialized data (both on the CPU and GPU). When overriding all texels, this can lead to improved performance and reduced memory usage during construction. Note that sampling an uninitialized texture gives unpredictable values.  
  
Usually you will want to set the colors of the texture after creating it, using [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) and [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.  
  
Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
* * *
## Declaration
public Texture2D(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat = TextureFormat.RGBA32, int mipCount = -1, bool linear = false, bool createUninitialized = false, [MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html) mipmapLimitDescriptor); 
### Description
Create a new empty texture.
The texture will be `width` by `height` size, with a given `format`, with mipmaps or without, and in either the linear color space or the sRGB color space. `width` and `height` must be greater than 0.  
  
Enable `createUninitialized` to make the texture reference uninitialized data (both on the CPU and GPU). When overriding all texels, this can lead to improved performance and reduced memory usage during construction. Note that sampling an uninitialized texture gives unpredictable values.  
  
Use a [MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html) to make the texture use the global mipmap limit from the current Quality Settings, or the mipmap limit of a [TextureMipmapLimitGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html). Note that a readable CPU copy is required for the texture to reupload when quality settings change. If the texture is made nonreadable (see [Texture2D.Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html)), the uploaded resolution will no longer adapt to the active quality level.  
  
Usually you will want to set the colors of the texture after creating it, using [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) and [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.  
  
Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) functions.
* * *
