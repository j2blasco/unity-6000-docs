* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.LoadImage.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).LoadImage
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
public static bool LoadImage([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex, byte[] data, bool markNonReadable); 
### Parameters
Parameter | Description  
---|---  
tex | The texture to load the image into.  
data | The byte array containing the image data to load.  
markNonReadable | Set to false by default, pass true to optionally mark the texture as non-readable.  
### Returns
**bool** Returns true if the data can be loaded, false otherwise. 
### Description
Loads PNG, JPG or EXR image byte array into a texture.
The LoadImage function replaces texture contents with new image data. This function can also change texture size and format. JPG files are loaded into [RGB24](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html) format, PNG files are loaded into [ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ARGB32.html) format, and EXR files are loaded into [RGBAFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBAFloat.html). If texture format before calling LoadImage is [DXT1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT1.html) or [DXT5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT5.html), then the loaded image will be DXT5-compressed for JPG and PNG images. EXR images and/or any other compression format will result in an uncompressed image. Unity returns false if your platform cannot use the compressed format on the GPU. Use [SystemInfo.IsFormatSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.IsFormatSupported.html) to check if your platform supports a format.   
  
Loading an EXR image is only supported on PC, Mac and Linux. Unity can load both tiled and untiled EXR images, but doesn't support the following features: 
  * Interpreting channel names and layers. Unity interprets the channels as ABGR if there are four channels, as BGR with full opacity if there are three channels, and as Y (grayscale) if there's one channel. For example, Unity reads an EXR texture with a single channel named "heightmap" as a grayscale image, stores channels named "X", "Y" and "Z" in the blue, green and red channels respectively, interprets "Y-RY-BY" as RGB data instead of as a luminance/chroma image, and doesn't treat layers with channel names like "leftView.R" differently.
  * Embedded mipmaps. Unity generates mipmap levels from the full-resolution image instead.
  * Multipart images.
  * Deep images.
  * Chromaticity coordinates.


Texture will be uploaded to the GPU automatically; there's no need to call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html).  
  
This function loads the texture data without gamma correction. If the texture data uses the sRGB color space, you must use an sRGB [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) object for correct rendering results. Likewise, if the texture data uses the linear color space, then you must use a linear [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) object. (A [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) object is sRGB if its `linear` constructor parameter was `false`, which is the default, and linear if the parameter was set to `true`.)  
  
**Note:** In previous versions of Unity, texture data from all PNG textures containing a gAMA block was returned in gamma 2.0 space. If you want to retain this old behavior, for example when working with older projects that dynamically load textures using LoadImage, set [ImageConversion.EnableLegacyPngGammaRuntimeLoadBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EnableLegacyPngGammaRuntimeLoadBehavior.html) to `true`. 
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Load a .jpg or .png file by adding .bytes extensions to the file
    // and dragging it on the imageAsset variable.
    public TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) imageAsset;
    public void Start()
    {
        // Create a texture. Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) size does not matter, since
        // LoadImage will replace with the size of the incoming image.
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(2, 2);
        ImageConversion.LoadImage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.LoadImage.html)(tex, imageAsset.bytes);
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = tex;
    }
}

```

Additional resources: [EncodeToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html), [EncodeToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToJPG.html), [LoadRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.LoadRawTextureData.html) functions.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        // Create a texture. Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) size does not matter, since
        // LoadImage will replace with the size of the incoming image.
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(2, 2);
        // A small 64x64 Unity logo encoded into a PNG.
        byte[] pngBytes = new byte[]
        {
            0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
            0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x40, 0x08, 0x00, 0x00, 0x00, 0x00, 0x8F, 0x02, 0x2E,
            0x02, 0x00, 0x00, 0x01, 0x57, 0x49, 0x44, 0x41, 0x54, 0x78, 0x01, 0xA5, 0x57, 0xD1, 0xAD, 0xC4,
            0x30, 0x08, 0x83, 0x81, 0x32, 0x4A, 0x66, 0xC9, 0x36, 0x99, 0x85, 0x45, 0xBC, 0x4E, 0x74, 0xBD,
            0x8F, 0x9E, 0x5B, 0xD4, 0xE8, 0xF1, 0x6A, 0x7F, 0xDD, 0x29, 0xB2, 0x55, 0x0C, 0x24, 0x60, 0xEB,
            0x0D, 0x30, 0xE7, 0xF9, 0xF3, 0x85, 0x40, 0x74, 0x3F, 0xF0, 0x52, 0x00, 0xC3, 0x0F, 0xBC, 0x14,
            0xC0, 0xF4, 0x0B, 0xF0, 0x3F, 0x01, 0x44, 0xF3, 0x3B, 0x3A, 0x05, 0x8A, 0x41, 0x67, 0x14, 0x05,
            0x18, 0x74, 0x06, 0x4A, 0x02, 0xBE, 0x47, 0x54, 0x04, 0x86, 0xEF, 0xD1, 0x0A, 0x02, 0xF0, 0x84,
            0xD9, 0x9D, 0x28, 0x08, 0xDC, 0x9C, 0x1F, 0x48, 0x21, 0xE1, 0x4F, 0x01, 0xDC, 0xC9, 0x07, 0xC2,
            0x2F, 0x98, 0x49, 0x60, 0xE7, 0x60, 0xC7, 0xCE, 0xD3, 0x9D, 0x00, 0x22, 0x02, 0x07, 0xFA, 0x41,
            0x8E, 0x27, 0x4F, 0x31, 0x37, 0x02, 0xF9, 0xC3, 0xF1, 0x7C, 0xD2, 0x16, 0x2E, 0xE7, 0xB6, 0xE5,
            0xB7, 0x9D, 0xA7, 0xBF, 0x50, 0x06, 0x05, 0x4A, 0x7C, 0xD0, 0x3B, 0x4A, 0x2D, 0x2B, 0xF3, 0x97,
            0x93, 0x35, 0x77, 0x02, 0xB8, 0x3A, 0x9C, 0x30, 0x2F, 0x81, 0x83, 0xD5, 0x6C, 0x55, 0xFE, 0xBA,
            0x7D, 0x19, 0x5B, 0xDA, 0xAA, 0xFC, 0xCE, 0x0F, 0xE0, 0xBF, 0x53, 0xA0, 0xC0, 0x07, 0x8D, 0xFF,
            0x82, 0x89, 0xB4, 0x1A, 0x7F, 0xE5, 0xA3, 0x5F, 0x46, 0xAC, 0xC6, 0x0F, 0xBA, 0x96, 0x1C, 0xB1,
            0x12, 0x7F, 0xE5, 0x33, 0x26, 0xD2, 0x4A, 0xFC, 0x41, 0x07, 0xB3, 0x09, 0x56, 0xE1, 0xE3, 0xA1,
            0xB8, 0xCE, 0x3C, 0x5A, 0x81, 0xBF, 0xDA, 0x43, 0x73, 0x75, 0xA6, 0x71, 0xDB, 0x7F, 0x0F, 0x29,
            0x24, 0x82, 0x95, 0x08, 0xAF, 0x21, 0xC9, 0x9E, 0xBD, 0x50, 0xE6, 0x47, 0x12, 0x38, 0xEF, 0x03,
            0x78, 0x11, 0x2B, 0x61, 0xB4, 0xA5, 0x0B, 0xE8, 0x21, 0xE8, 0x26, 0xEA, 0x69, 0xAC, 0x17, 0x12,
            0x0F, 0x73, 0x21, 0x29, 0xA5, 0x2C, 0x37, 0x93, 0xDE, 0xCE, 0xFA, 0x85, 0xA2, 0x5F, 0x69, 0xFA,
            0xA5, 0xAA, 0x5F, 0xEB, 0xFA, 0xC3, 0xA2, 0x3F, 0x6D, 0xFA, 0xE3, 0xAA, 0x3F, 0xEF, 0xFA, 0x80,
            0xA1, 0x8F, 0x38, 0x04, 0xE2, 0x8B, 0xD7, 0x43, 0x96, 0x3E, 0xE6, 0xE9, 0x83, 0x26, 0xE1, 0xC2,
            0xA8, 0x2B, 0x0C, 0xDB, 0xC2, 0xB8, 0x2F, 0x2C, 0x1C, 0xC2, 0xCA, 0x23, 0x2D, 0x5D, 0xFA, 0xDA,
            0xA7, 0x2F, 0x9E, 0xFA, 0xEA, 0xAB, 0x2F, 0xDF, 0xF2, 0xFA, 0xFF, 0x01, 0x1A, 0x18, 0x53, 0x83,
            0xC1, 0x4E, 0x14, 0x1B, 0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82,
        };
        // Load data into the texture.
        ImageConversion.LoadImage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.LoadImage.html)(tex, pngBytes);  
  
        // Assign texture to renderer's material.
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = tex;
    }
}

```

* * *
