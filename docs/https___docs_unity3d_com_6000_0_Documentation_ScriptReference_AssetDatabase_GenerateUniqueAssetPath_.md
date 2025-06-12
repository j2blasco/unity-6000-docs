* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GenerateUniqueAssetPath
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
public static string GenerateUniqueAssetPath(string path); 
### Description
Creates a new unique path for an asset.
When you call this method, Unity checks to see whether an asset already exists with the matching path and filename you supply. If it does not exist, Unity returns the same string you supplied. If there is already an existing asset with the matching path and filename, Unity appends the number 1 to the filename and checks again. It continues incrementing this number and checking again until it finds a filename that does not currently exists, and returns the path with that new unique filename.  
  
All paths generated are relative to the project folder, for example: "Assets/MyTextures/hello.png".
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class GenerateUniqueAssetPathExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/GenerateUniqueAssetPath")]
    static void GenerateUniqueAssetPathForFilesWithSameName()
    {
        for (int i = 0; i < 5; ++i)
        {
            //The file names that this should create are:
            // Assets/Artifacts/material.mat
            // Assets/Artifacts/material 1.mat
            // Assets/Artifacts/material 2.mat
            // Assets/Artifacts/material 3.mat
            // Assets/Artifacts/material 4.mat
            var uniqueFileName = AssetDatabase.GenerateUniqueAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html)("Assets/Artifacts/material.mat");  
  
            Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, uniqueFileName);
        }
    }
}

```

* * *
