* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).TryGetGUIDAndLocalFileIdentifier
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
public static bool TryGetGUIDAndLocalFileIdentifier([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, out string guid, out long localId); 
## Declaration
public static bool TryGetGUIDAndLocalFileIdentifier(int instanceID, out string guid, out long localId); 
## Declaration
public static bool TryGetGUIDAndLocalFileIdentifier(LazyLoadReference<T> assetRef, out string guid, out long localId); 
### Parameters
Parameter | Description  
---|---  
instanceID | InstanceID of the object to retrieve information for.  
obj | The object to retrieve GUID and File Id for.  
assetRef | The asset reference to retrieve GUID and File Id for.  
guid | The GUID of an asset.  
localId | The local file identifier of this asset.  
### Returns
**bool** True if the guid and file id were successfully found, false if not. 
### Description
Get the GUID and local file id from an object instance id.
**Warning:** Avoid the obsolete versions of this function, which use `int` for the `localId` parameter instead of `long`. Local Ids can be longer than 32 bits in some cases, such as for Prefabs. When Unity serializes an asset reference it points to two things: the GUID and file ID. GUID is a unique hash, and file ID is a value relative to the asset. Both of these values are used when a serialized asset references another asset.  
  
If working with a text serialized project (see [Editor Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html)) it is possible to manually modify this information. A common use is moving C# script files from a project to a DLL while keeping any GameObjects using these scripts intact. As an example, suppose your project contains a C# MonoBehaviour, a Scene, and a GameObject with this script attached. When serialized the Unity Scene file will contain something that looks like this (reduced to the relevant parts):
```
/* example .unity Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) contents:  
  
--- !u!1 &65078845
GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html):
  m_Component:
  -component: {fileID : 65078850}
--- !u!114 &65078850
MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html):
  m_Script: {fileID : 11500000, guid : 9cbd8cdf99d44b58972fbc7f6f38088f, type : 3}  
  
*/

```

```
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ShowAssetIds
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Assets/Show Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Ids")]
    static void MenuShowIds()
    {
        var stringBuilder = new StringBuilder();  
  
        foreach (var obj in AssetDatabase.LoadAllAssetsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html))))
        {
            string guid;
            long file;  
  
            if (AssetDatabase.TryGetGUIDAndLocalFileIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(obj, out guid, out file))
            {
                stringBuilder.AppendFormat("Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html): " + obj.name +
                    "\n  Instance ID: " + obj.GetInstanceID() +
                    "\n  GUID: " + guid +
                    "\n  File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) ID: " + file);
            }
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(stringBuilder.ToString());
    }
}

```

Additional resources: [GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html)
* * *
