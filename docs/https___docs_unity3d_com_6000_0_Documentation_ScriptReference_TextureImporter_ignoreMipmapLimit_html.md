* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-ignoreMipmapLimit.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).ignoreMipmapLimit
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
ignoreMipmapLimit; 
### Description
Enable this flag for textures that should ignore mipmap limit settings.
This has no effect if the [textureShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-textureShape.html) is not `Texture2D` or `Texture2DArray`. Also, this has no effect on textures without mipmaps. For additional information, see [Texture2D.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-ignoreMipmapLimit.html) and [Texture2DArray.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-ignoreMipmapLimit.html). By default, an imported texture asset has mipmap limits enabled, and uses the global mipmap limit. If you imported a Texture2DArray asset in Unity version 2023.1 or earlier, the asset will continue to ignore mipmap limits to ensure consistent behavior when upgrading.  
  
Note that imported textures have mipmap limits enabled by default. This code example demonstrates how to use an AssetPostprocessor to explicitly ignore the mipmap limit.
```
#if UNITY_EDITOR
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleImporter : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessTexture()
    {
        if (assetPath.Contains("_IgnoreMipmapLimit"))
        {
            TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) textureImporter = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))assetImporter;
            textureImporter.ignoreMipmapLimit = true;
        }
    }
}
#endif
```

Additional resources: [Texture2D.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-ignoreMipmapLimit.html), [Texture2DArray.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-ignoreMipmapLimit.html), [mipmapEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapEnabled.html).
* * *
