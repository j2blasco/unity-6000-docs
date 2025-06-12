* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessCubemap.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessCubemap(Cubemap)
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
Add this function to a subclass to get a notification just before a cubemap texture has completed importing.
Note that you should avoid modifying the TextureImporter settings in this manner as it would have no effect on the texture that is currently being imported but would apply the next time the texture is imported. This behavior is nondeterministic and therefore undesirable. 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Postprocesses all cubemaps that are placed in a folder
// Here we just halve the texels values
public class ProcessCubemap : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPostprocessCubemap(Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) texture)
    {
        string lowerCaseAssetPath = assetPath.ToLower();
        if (lowerCaseAssetPath.IndexOf("/postprocessedcubemaps/") == -1)
            return;  
  
        for (int m = 0; m < texture.mipmapCount; m++)
        {
            for (int face = 0; face < 6; face++)
            {
                CubemapFace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) f = (CubemapFace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html))face;
                Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] c = texture.GetPixels(f, m);  
  
                for (int i = 0; i < c.Length; i++)
                {
                    c[i].r = c[i].r * 0.5f;
                    c[i].g = c[i].g * 0.5f;
                    c[i].b = c[i].b * 0.5f;
                }  
  
                texture.SetPixels(c, f, m);
            }
            // Instead of setting pixels for each mipmap level, you can also
            // modify only the pixels in the highest mip level. And then simply use
            // texture.Apply(true); to generate lower mip levels.
        }
    }
}

```

* * *
