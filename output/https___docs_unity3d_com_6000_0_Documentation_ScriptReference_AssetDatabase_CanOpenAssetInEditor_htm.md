* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenAssetInEditor.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CanOpenAssetInEditor
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
public static bool CanOpenAssetInEditor(int instanceID); 
### Parameters
Parameter | Description  
---|---  
instanceID | The instance ID of the asset.  
### Returns
**bool** Returns true if Unity can successfully open the asset in the Editor, otherwise returns false. 
### Description
Checks if Unity can open an asset in the Editor.
Checks if Unity can open a given asset instance in the Editor if [AssetDatabase.OpenAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.OpenAsset.html) is executed. Note: The asset must be written to disk, or this function always returns false.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Callbacks;
using UnityEngine;  
  
[CreateAssetMenu(fileName = "MyObject", menuName = "ScriptableObjects/MyObject", order = 1)]
public class MyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string myData;  
  
    [OnOpenAsset]
    public static bool Open(int instanceID)
    {
        if (AssetDatabase.GetMainAssetTypeAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeAtPath.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyObject))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Opening asset");
            return true;
        }
        else  return false; // This method doesn't handle opening of different asset types
    }  
  
    [OnOpenAsset(OnOpenAssetAttributeMode.Validate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.Validate.html))]
    public static bool WillOpen(int instanceID)
    {
        if (AssetDatabase.GetMainAssetTypeAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeAtPath.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyObject))
        {
            // We can open MyObject asset using MyObject opening method
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This asset can be opened by OnOpenAsset marked method");
            return true;
        }
        else  return false; // The passed instance doesn't belong to MyObject type asset so we won't be able to open it using opening method inside MyObject
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/WillOpenInUnity")]
    public static void WillSelectionBeOpenedInUnity()
    {
        AssetDatabase.CanOpenAssetInEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenAssetInEditor.html)(Selection.activeObject.GetInstanceID());
    }
}
```

* * *
