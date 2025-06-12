* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).AddObjectToAsset
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
public static void AddObjectToAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToAdd, string path); 
### Parameters
Parameter | Description  
---|---  
objectToAdd | Object to add to the existing asset.  
path | Filesystem path to the destination asset.  
### Description
Adds `objectToAdd` to an existing asset at `path`.
Please note that you should only add objects to '.asset' assets, imported models or texture objects for example will lose their data.  
  
All paths are relative to the project folder.  
  
**Note:** You can not add GameObjects; use [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html) instead.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AddObjectToAssetPathExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/AddObjectToAssetPathExample")]
    static void AddObjectToPathExample()
    {
        // Create a simple material object
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        material.name = "My material";  
  
        // Create an instance of a simple scriptable object
        DummyObject dummyObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<DummyObject>();
        dummyObject.name = "My scriptable asset";  
  
        // Create the scriptable object asset
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(dummyObject, "Assets/dummyObject.asset");  
  
        // Get the path of the scriptable object asset
        string dummyObjectPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(dummyObject);  
  
        // Add the material to the scriptable object asset
        AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(material, dummyObjectPath);  
  
        // Serializing the changes in memory to disk
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        // Print the path of the created asset
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(dummyObject));
    }
}  
  
// The DummyObject class used in the example above
public class DummyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string objectName = "dummy";
}

```

* * *
## Declaration
public static void AddObjectToAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToAdd, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject); 
### Parameters
Parameter | Description  
---|---  
objectToAdd | Object to add to the existing asset.  
assetObject | Destination asset.  
### Description
Adds `objectToAdd` to an existing asset identified by `assetObject`.
**Note:** Having `objectToAdd` on disc before calling AddObjectToAsset will generate an error (ex. trying to add "MyMaterial" to an existing asset): "Couldn't add object to asset file because the Material 'MyMaterial' is already an asset at 'Assets/MyMaterial.mat'!"  
  
**Note:** You have to serialize the changes in memory to disk.   
This is because assets that have been modified in memory, must be saved to disk.   
Failling to do this will produce an inconsistent result warning, as in-memory modifications to the asset will be lost.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AddObjectToAssetExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/AddObjectExample")]
    static void AddObjectExample()
    {
        // Create a simple material object
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        material.name = "My material";  
  
        // Create an instance of a simple scriptable object
        DummyObject dummyObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<DummyObject>();
        dummyObject.name = "My scriptable asset";  
  
        // Create the scriptable object asset
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(dummyObject, "Assets/dummyObject.asset");  
  
        // Add the material to the scriptable object asset
        AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(material, dummyObject);  
  
        // Serializing the changes in memory to disk
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        // Print the path of the created asset
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(dummyObject));
    }
}  
  
// The DummyObject class used in the example above
public class DummyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string objectName = "dummy";
}

```

* * *
