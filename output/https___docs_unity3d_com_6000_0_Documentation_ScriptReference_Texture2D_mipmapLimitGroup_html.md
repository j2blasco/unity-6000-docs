* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-mipmapLimitGroup.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).mipmapLimitGroup
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
mipmapLimitGroup; 
### Description
The name of the texture mipmap limit group that this texture is associated with. (Read Only)
If this texture has a mipmap limit group assignment, this texture respects the [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) of that group. If this texture does not have a group assignment, or the indicated group does not exist, this texture takes the [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) instead. If you construct or import this texture, assign it to a mipmap limit group that does not yet exist, then create that mipmap limit group, this texture respects the [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) of that new group.  
  
Set this property in the constructor or in the texture importer, because you cannot set this property after creating the texture. If the texture has no mipmaps, this property has no effect.  
  
This code example demonstrates how to set this property in both the Texture2D constructor and AssetPostprocessor.
```
using UnityEngine;
using UnityEngine.Experimental.Rendering;
#if UNITY_EDITOR
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
#endif  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        const int size = 32;
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) scriptTexture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(size, size, GraphicsFormat.R8G8B8A8_SRGB[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.R8G8B8A8_SRGB.html), Texture.GenerateAllMips[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GenerateAllMips.html), "MyGroup", TextureCreationFlags.MipChain[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.TextureCreationFlags.MipChain.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"mipmapLimitGroup has been set to '{scriptTexture.mipmapLimitGroup}' on the script texture!");
    }
}  
  
#if UNITY_EDITOR
public class ExampleImporter : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessTexture()
    {
        if (assetPath.Contains("_MyGroup"))
        {
            TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) textureImporter = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))assetImporter;
            textureImporter.mipmapLimitGroupName = "MyGroup";
        }
    }
}
#endif

```

Additional resources: [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html), [TextureImporter.mipmapLimitGroupName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapLimitGroupName.html).
* * *
