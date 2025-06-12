* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsMainAsset
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
public static bool IsMainAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static bool IsMainAsset(int instanceID); 
### Description
Is asset a main asset in the project window?
For example an imported model has a game object as its root and several Meshes and child game objects in expanded state. The root game object is the main asset in this case.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Scriptable : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
}  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Is Main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Example")]
    static void IsMainAssetExample()
    {
        var materialAsset = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));  
  
        //materialAsset is still in memory, therefore this will be False
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsMainAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAsset.html)(materialAsset));  
  
        //Create a Scriptable object
        var scriptableAssetPath = "Assets/ScriptableObjects/NewObject.asset";
        var mainAsset = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Scriptable>();
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(mainAsset, scriptableAssetPath);  
  
        //Add the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) to the Scriptable object, so that the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) becomes a Sub Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) of the Scriptable object
        AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(materialAsset, scriptableAssetPath);
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //This will be false because material asset has been added to the main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) and is now a Sub Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsMainAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAsset.html)(materialAsset));  
  
        //Remove the subAsset from the Scriptable object and create it as an Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)
        AssetDatabase.RemoveObjectFromAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveObjectFromAsset.html)(materialAsset);
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(materialAsset, "Assets/Materials/New Mat0.mat");  
  
        //This will be True because the material is now the main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.IsMainAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAsset.html)(materialAsset));
    }
}
```

* * *
