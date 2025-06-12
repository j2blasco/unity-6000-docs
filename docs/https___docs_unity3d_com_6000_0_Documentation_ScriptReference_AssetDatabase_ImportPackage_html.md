* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackage.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ImportPackage
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
public static void ImportPackage(string packagePath, bool interactive); 
### Description
Imports package at **packagePath** into the current project.
If **interactive** is true, an import package dialog will be opened, else all assets in the package will be imported into the current project.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Import Package[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Package.html) Example")]
    static void ImportPackageExample()
    {
        var texturePackageNames = new[] {"groundTextures2k.unitypackage", "groundTextures4k.unitypackage"};
        foreach (var package in texturePackageNames)
        {
            AssetDatabase.ImportPackage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackage.html)(package, false);
        }
    }
}
```

* * *
