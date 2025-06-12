* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetBundleDependencies.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAssetBundleDependencies
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
public static string[] GetAssetBundleDependencies(string assetBundleName, bool recursive); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The name of the AssetBundle for which dependencies are required.  
recursive | If false, returns only AssetBundles which are direct dependencies of the input; if true, includes all indirect dependencies of the input.  
### Returns
**string[]** The names of all AssetBundles that the input depends on. 
### Description
Given an **assetBundleName** , returns the list of AssetBundles that it depends on.
```
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Find Bundles With Dependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.html)")]
    static void BundleDependency()
    {
        var allBundleNames = AssetDatabase.GetAllAssetBundleNames[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAllAssetBundleNames.html)();
        foreach (var bundle in allBundleNames)
        {
            var dependencies = AssetDatabase.GetAssetBundleDependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetBundleDependencies.html)(bundle, true);
            if (dependencies.Length == 0)
                continue;
            var dependencyString = new StringBuilder();
            foreach (var dependency in dependencies)
            {
                dependencyString.Append($"\"{dependency}\" ");
            }
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{bundle} depends on {dependencyString}");
        }
    }
}
```

* * *
