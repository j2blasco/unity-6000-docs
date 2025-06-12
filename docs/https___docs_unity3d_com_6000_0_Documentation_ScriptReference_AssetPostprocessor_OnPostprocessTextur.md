* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessTexture3D.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessTexture(Texture3D)
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
### Description
Add this function to a subclass to get a notification when a texture3D has completed importing just before Unity compresses it.
You can't choose a compression format at this point. If you want to change compression format based on filename or other attributes of the texture, use [AssetPostprocessor.OnPreprocessTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessTexture.html).  
  
However, if you modify the TextureImporter settings in this way, it has no effect on the texture that Unity is currently importing, but it does apply the next time Unity imports this texture. This causes unpredictable results. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Postprocesses all 3D textures that are placed in a folder
// "invert color" to have their colors inverted.
public class InvertColor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPostprocessTexture3D(Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) texture)
    {
        // Only post process 3D textures if they are in a folder
        // "invert color" or a sub folder of it.
        string lowerCaseAssetPath = assetPath.ToLower();
        if (lowerCaseAssetPath.IndexOf("/invert color/") == -1)
            return;  
  
        for (int m = 0; m < texture.mipmapCount; m++)
        {
            Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] c = texture.GetPixels(m);  
  
            for (int i = 0; i < c.Length; i++)
            {
                c[i].r = 1 - c[i].r;
                c[i].g = 1 - c[i].g;
                c[i].b = 1 - c[i].b;
            }
            texture.SetPixels(c, m);
        }
        // Instead of setting pixels for each mipmap level, you can modify
        // the pixels in the highest mipmap then use texture.Apply(true);
        // to generate lower mip levels.
    }
}

```

* * *
