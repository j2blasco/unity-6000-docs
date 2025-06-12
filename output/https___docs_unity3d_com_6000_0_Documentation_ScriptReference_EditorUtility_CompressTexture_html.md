* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressTexture.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CompressTexture
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
public static void CompressTexture([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format, int quality); 
## Declaration
public static void CompressTexture([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format, [TextureCompressionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionQuality.html) quality); 
### Description
Compress a texture.
Use this function to explicitly compress a texture into specified format.  
  
If you want to do texture compression in-game, use [Texture2D.Compress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Compress.html) function, which will use faster but lower quality DXT1/DXT5 (also known as BC1/BC3) or ETC/EAC compression.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CompressTextureExample : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    // Automatically Compress all imported textures to the project to RGB24
    void OnPostprocessTexture(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) t)
    {
        EditorUtility.CompressTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressTexture.html)(t, TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), TextureCompressionQuality.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionQuality.Normal.html));
    }
}

```

* * *
