* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).WriteImportSettingsIfDirty
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
public static bool WriteImportSettingsIfDirty(string path); 
### Description
Writes the import settings to disk.
In order to make the cache server import assets.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Set Cookies Import Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)")]
    static void SetCookiesImportSettings()
    {
        for (var i = 0; i < 10; i++)
        {
            var texturePath = $"Assets/Lighting/Cookies/LightingCookie{i}.jpg";
            var textureImporter =
                TextureImporter.GetAtPath(texturePath) as TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html);
            textureImporter.textureType = TextureImporterType.Cookie[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.Cookie.html);
            textureImporter.alphaSource = TextureImporterAlphaSource.FromGrayScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterAlphaSource.FromGrayScale.html);
            //This method saves the Cookies import settings, without it the editor will ask you to apply unapplied settings
            AssetDatabase.WriteImportSettingsIfDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html)(texturePath);
        }
    }
}
```

* * *
