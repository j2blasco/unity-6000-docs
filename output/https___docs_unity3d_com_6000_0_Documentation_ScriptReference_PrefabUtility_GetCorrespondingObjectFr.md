* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetCorrespondingObjectFromSource
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
public static TObject GetCorrespondingObjectFromSource(TObject componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to find the corresponding object from.  
### Returns
**TObject** The corresponding object or null. 
### Description
Retrieves the corresponding asset object of `source`, or null if it can't be found.
Use this method to get a Prefab Asset object the `source` was instantiated from.  
  
For example, in the diagram shown below, prefab asset "A" contains a child nested prefab "B", which contains a child nested prefab "C".  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/nested-prefab-instance-example.png)  
  
When GameObject C (the instance of nested prefab C in the hierarchy) is passed in as the source to this method, this method returns the object "C (Nested Prefab)" from the asset "Prefab A".  
  
The example script below adds a menu item to the editor, which launches a simple wizard that allows you to test the results of this method.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
public class AssetSourceTestWizard : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instance;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Source Test Wizard")]
    static void CreateWizard()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)<AssetSourceTestWizard>("Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Source Test Wizard", "Do Test");
    }  
  
    void OnWizardCreate()
    {
        var o1 = PrefabUtility.GetCorrespondingObjectFromSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html)(instance);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Corresponding object from source: " + o1.name + " from: " + AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(o1));
    }
}

```

See also: [GetCorrespondingObjectFromSourceAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html), [GetOriginalSourceRootWhereGameObjectIsAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html), [GetCorrespondingObjectFromOriginalSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromOriginalSource.html).
* * *
