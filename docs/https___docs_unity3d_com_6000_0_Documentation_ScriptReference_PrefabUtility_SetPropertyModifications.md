* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).SetPropertyModifications
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
public static void SetPropertyModifications([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetPrefab, PropertyModification[] modifications); 
### Parameters
Parameter | Description  
---|---  
targetPrefab | A reference to the Prefab instance to be modified. Although the type and name imply an asset, it is the outermost instance as a GameObject that should be provided.  
modifications | A set of PropertyModification objects that define the changes to the target Prefab instance.  
### Description
Assigns a set of [PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) objects to a target Prefab instance relative to its source Prefab Asset.
It's important to provide this method with the top-level object in the target instance's branch of the hierarchy to avoid unexpected results. Use [GetOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html) for this purpose.  
  
[PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) fields for Prefab overrides:
  * **target** : A persistent Prefab asset object reference
  * **propertyPath** : The path of the property to be modified
  * **value** : The value of the property as a string
  * **objectReference** : Set this field if the modification is an object reference, otherwise set the `value` field


The PropertyModification members always expected to have been set are the `target` object the modification applies to (i.e. a persistent Prefab asset object reference), the `propertyPath` of the property to be modified and its new `value` or `objectReference`, as shown in the following example:
```
void MakePrefabModifications(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject)
{
    // Get the outermost root from the target object
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabInstanceRoot = PrefabUtility.GetOutermostPrefabInstanceRoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html)(gameObject);
    if (prefabInstanceRoot == null)
        return;  
  
    // Get the corresponding prefab asset
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot = PrefabUtility.GetCorrespondingObjectFromSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html)(prefabInstanceRoot);  
  
    // Create modifications for m_Name and m_LocalScale.x
    var mods = new[]
    {
        new UnityEditor.PropertyModification { value = "NewName", propertyPath = "m_Name", target = prefabAssetRoot },
        new UnityEditor.PropertyModification { value = "3", propertyPath = "m_LocalScale.x", target = prefabAssetRoot.transform }
    };  
  
    PrefabUtility.SetPropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html)(prefabInstanceRoot, mods);
}

```

The following example shows an example of `PropertyModification.objectReference` usage on a Prefab which has a MeshRenderer:
```
void MakePrefabModificationUsingObjectReference(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject)
{
    // Get the outermost root from the target object
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabInstanceRoot = PrefabUtility.GetOutermostPrefabInstanceRoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html)(gameObject);
    if (prefabInstanceRoot == null)
        return;  
  
    // Get the corresponding prefab asset
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot = PrefabUtility.GetCorrespondingObjectFromSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html)(prefabInstanceRoot);  
  
    MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) prefabMeshRenderer = prefabAssetRoot.GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
    
    // Create a material asset to add to the MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Diffuse"));
    AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/MyMaterial.mat");  
  
    var mods = new[]
    {
        new UnityEditor.PropertyModification { target = prefabMeshRenderer, propertyPath = "m_Materials.Array.data[0]", objectReference = material }
    };  
  
    PrefabUtility.SetPropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html)(prefabInstanceRoot, mods);
}

```

Be aware that calls to `SetPropertyModifications` will replace the previous set of modifications. If the intention is to accumulate modifications, then retrieve the current set with [GetPropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPropertyModifications.html) and include them in the new set.  
  
SetPropertyModifications can be used to remove unwanted modifications. To remove only non-default modifications, filter them away and keep the default overrides, as below:
```
List<PropertyModification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html)> defaultMods = new List<PropertyModification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html)>();
PropertyModification[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html)[] mods = PrefabUtility.GetPropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPropertyModifications.html)(prefabInstanceRoot);
foreach (var mod in mods)
{
    if (PrefabUtility.IsDefaultOverride[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html)(mod))
        defaultMods.Add(mod);
}  
  
PrefabUtility.SetPropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html)(prefabInstanceRoot, defaultMods.ToArray());

```

For creating overrides a preferred approach is to use either [RecordPrefabInstancePropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html) for manually changed properties or use [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) and [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) which will automatically generate overrides.  
  
For applying and reverting overrides consider using the following API which provide convenient access to Apply and Revert functionality:  
  
[GetObjectOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetObjectOverrides.html) [GetAddedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedComponents.html) [GetRemovedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedComponents.html) [GetAddedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedGameObjects.html) [GetRemovedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html).
* * *
