* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html

# Resources
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
The Resources class allows you to find and access Objects including assets.
In the editor, [Resources.FindObjectsOfTypeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html) can be used to locate assets and Scene objects.  
  
All assets that are in a folder named "Resources" anywhere in the Assets folder can be accessed via the [Resources.Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) functions. Multiple "Resources" folders may exist and when loading objects each will be examined.  
  
In Unity you usually don't use path names to access assets, instead you expose a reference to an asset by declaring a member-variable, and then assign it in the inspector. When using this technique Unity can automatically calculate which assets are used when building a player. This radically minimizes the size of your players to the assets that you actually use in the built game. When you place assets in "Resources" folders this can not be done, thus all assets in the "Resources" folders will be included in a build.  
  
Another disadvantage of using path names is that it leads to less reusable code since scripts will have specific hard coded requirements on where the used assets are placed. On the other hand using references that are exposed in the inspector are self-documenting and immediately obvious to the user of your script.  
  
However there are situations where it is more convenient to fetch an asset by its name instead of linking to it in the inspector. Essentially whenever it is inconvenient to assign the reference to the object in the inspector. For example you might want to create a game object procedurally from a script and for example assign a texture to a procedurally generated mesh.  
  
Some loaded assets, most notably textures, can use up memory even when no instance exists in the Scene. To reclaim this memory when the asset is no longer needed, you can use [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).  
  
**Note:** The [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) folder in Assets needs to be created before it is used. It is not created when a new Project is created. 
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = go.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        rend.material.mainTexture = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)("glass") as Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html);
    }
}

```

### Static Methods
Method | Description  
---|---  
[FindObjectsOfTypeAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html) | Returns a list of all objects of Type T.  
[InstanceIDIsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDIsValid.html) | Returns true if the given instance ID corresponds to a valid Object in memory. The Object could have been deleted or not loaded into memory yet.  
[InstanceIDsToValidArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDsToValidArray.html) | Translates an array of instance IDs to an array of bools indicating whether a given instance ID from instanceIDs corresponds to a valid Object in memory. The Object could have been deleted or not loaded into memory yet.  
[InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObject.html) | Translates an instance ID to an object reference.  
[InstanceIDToObjectList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObjectList.html) | Translates an array of instance IDs to a list of Object references.  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) | Loads the asset of the requested type stored at path in a Resources folder.  
[LoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html) | Loads all assets in a folder or file at path in a Resources folder.  
[LoadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAsync.html) | Asynchronously loads an asset stored at path in a Resources folder.  
[UnloadAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadAsset.html) | Unloads assetToUnload from memory.  
[UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) | Unloads assets that are not used.  
* * *
