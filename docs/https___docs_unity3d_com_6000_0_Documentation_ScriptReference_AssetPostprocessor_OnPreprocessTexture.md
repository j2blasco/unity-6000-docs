* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessTexture.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPreprocessTexture()
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
Add this function to a subclass to get a notification just before the texture importer is run.
This lets you set up default values for the import settings.  
  
Use this callback if you want to change the compression format of the texture.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Automatically convert any texture file with "_bumpmap"
// in its file name into a normal map.  
  
class MyTexturePostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessTexture()
    {
        if (assetPath.Contains("_bumpmap"))
        {
            TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) textureImporter  = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))assetImporter;
            textureImporter.convertToNormalmap = true;
        }
    }
}

```

* * *
