* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveAssetBundleName.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).RemoveAssetBundleName
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
public static bool RemoveAssetBundleName(string assetBundleName, bool forceRemove); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The assetBundle name you want to remove.  
forceRemove | Flag to indicate if you want to remove the assetBundle name even it's in use.  
### Description
Remove the assetBundle name from the asset database. The forceRemove flag is used to indicate if you want to remove it even it's in use.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Remove Bundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Bundle.html) Name")]
    static void RemoveAssetBundleNameExample()
    {
        //Remove Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Bundle.html) name that is on Cube.prefab and it's dependencies
        var prefabPath = "Assets/Prefabs/Cube.prefab";
        var assetBundleName = AssetDatabase.GetImplicitAssetBundleName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImplicitAssetBundleName.html)(prefabPath);
        var assetBundleDependencies = AssetDatabase.GetAssetBundleDependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetBundleDependencies.html)(assetBundleName, true);
        AssetDatabase.RemoveAssetBundleName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveAssetBundleName.html)(assetBundleName, true);
        foreach (var bundleName in assetBundleDependencies)
        {
            AssetDatabase.RemoveAssetBundleName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveAssetBundleName.html)(bundleName, true);
        }
    }
}
```

* * *
