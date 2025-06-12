* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).GetOutputArtifactFilePath
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
public string GetOutputArtifactFilePath(string fileName); 
### Parameters
Parameter | Description  
---|---  
fileName | Unique identifier to refer to this Artifact File.  
### Returns
**string** The file path which can be used to create a new Artifact File. 
### Description
Returns the path where to write a new Artifact File with the given fileName.
An Artifact File is part of the result of an importer and can contain any data that are not UnityEngine.Object. For example the 'info' Artifact File is reserved by Unity and stores the preview data of the imported Main Object.  
  
The following example shows how to add an Artifact File for a TextureImporter AssetPostprocessor to save the color of the first pixel of the texture inside an ArtifactFile. See [AssetImportContext.GetArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetArtifactFilePath.html) to see how this information can be used by another importer to depends on this value and not the whole texture.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class SaveFirstPixelColor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    public override uint GetVersion()
    {
        return 1;
    }  
  
    void OnPostprocessTexture(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture)
    {
        if (assetPath.StartsWith("Assets/"))
        {
            string path = context.GetOutputArtifactFilePath("firstpixelcolor");
            if (!string.IsNullOrEmpty(path))
                File.WriteAllText(path, $"#{ColorUtility.ToHtmlStringRGBA[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.ToHtmlStringRGBA.html)(texture.GetPixel(0, 0))}");
        }
    }
}

```

* * *
