* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeFromGUID.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetMainAssetTypeFromGUID
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
public static Type GetMainAssetTypeFromGUID(GUID guid); 
### Parameters
Parameter | Description  
---|---  
guid | The guid of the asset.  
### Description
Returns the type of the main asset object with `guid`.
```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Print Type Count")]
    static void GetAllAssetTypeCount()
    {
        var typeCount = new Dictionary<string, uint>();
        //Put all the types that were found in the typeCount dictionary and increment their count
        foreach (var guid in AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("", new []{"Assets"}))
        {
            var typeString = AssetDatabase.GetMainAssetTypeFromGUID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeFromGUID.html)(new GUID(guid)).ToString();
            if (typeCount.ContainsKey(typeString))
                typeCount[typeString]++;
            else
                typeCount.Add(typeString, 1);
        }
        //Print types and their count into the Unity Console
        foreach (var element in typeCount)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(element);
        }
    }
}
```

* * *
