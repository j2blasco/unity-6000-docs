* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).SetLabels
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
public static void SetLabels([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, string[] labels); 
### Description
Replaces that list of labels on an asset.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Set Vegetation Labels")]
    static void SetVegetationAssetLabels()
    {
        //Search the Assets folder for all assets with "tree" in its name and then add "Vegetation" Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) to every asset that we find
        foreach (var guid in AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("tree", new [] {"Assets"}))
        {
            var path = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);
            var asset = AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(path);
            AssetDatabase.SetLabels[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html)(asset, new []{"Vegetation"});
        }
    }
}
```

* * *
