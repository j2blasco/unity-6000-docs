* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor-assetPath.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).assetPath
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
assetPath; 
### Description
The path name of the asset being imported.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Automatically sets Textures settings upon first import and prints the
// path from  where is being imported  
  
class CustomImportSettings : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessTexture()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Importing texture to: " + assetPath);
        TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) importer  = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))assetImporter;
        importer.textureFormat = TextureImporterFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ARGB32.html);
        importer.isReadable = true;
        importer.mipmapEnabled = false;
    }
}

```

* * *
