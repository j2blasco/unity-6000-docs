* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressCubemapTexture.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CompressCubemapTexture
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
public static void CompressCubemapTexture([Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) texture, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format, int quality); 
## Declaration
public static void CompressCubemapTexture([Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) texture, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format, [TextureCompressionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionQuality.html) quality); 
### Description
Compress a cubemap texture.
Use this function to explicitly compress a cube map texture into specified format.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CompressCubemapTextureExample : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    // Automatically Compress all imported cube map textures to the project to RGB24
    void OnPostprocessTexture(Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) t)
    {
        EditorUtility.CompressCubemapTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressCubemapTexture.html)(t, TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), TextureCompressionQuality.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionQuality.Normal.html));
    }
}

```

* * *
