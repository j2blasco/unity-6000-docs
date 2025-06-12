* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsNativeAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsNativeAsset
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
public static bool IsNativeAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static bool IsNativeAsset(int instanceID); 
### Description
Determines whether the Asset is a native Asset.
A native Asset is a file produced directly by Unity's serialization system (for example, a .mat Material file is a native Asset)  
  
Note that scenes, prefabs and assembly definitions are not considered to be native assets.  
  
Additional resources: [AssetDatabase.IsForeignAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsForeignAsset.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/List All Native Files")]
    static void ListNativeFiles()
    {
        //List all native assets in the project
        foreach (var guid in AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("", new []{"Assets"}))
        {
            var path = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);
            var asset = AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(path);
            if(AssetDatabase.IsNativeAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsNativeAsset.html)(asset))
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset);
        }
    }
}
```

* * *
