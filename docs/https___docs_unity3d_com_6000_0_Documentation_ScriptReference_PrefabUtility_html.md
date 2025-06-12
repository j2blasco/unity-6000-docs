* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html

# PrefabUtility
class in UnityEditor
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
Utility class for any Prefab related operations.
```
// This script creates a new menu item Examples>Create Prefab in the main menu.
// Use it to create Prefab(s) from the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)(s).
// It is placed in the root Assets folder.
using System.IO;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    // Creates a new menu item 'Examples > Create Prefab' in the main menu.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create Prefab")]
    static void CreatePrefab()
    {
        // Keep track of the currently selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)(s)
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objectArray = Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html);  
  
        // Loop through every GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the array above
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject in objectArray)
        {
            // Create folder Prefabs and set the path as within the Prefabs folder,
            // and name it as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name with the .Prefab format
            if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
                AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");
            string localPath = "Assets/Prefabs/" + gameObject.name + ".prefab";  
  
            // Make sure the file name is unique, in case an existing Prefab has the same name.
            localPath = AssetDatabase.GenerateUniqueAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html)(localPath);  
  
            // Create the new Prefab and log whether Prefab was saved successfully.
            bool prefabSuccess;
            PrefabUtility.SaveAsPrefabAssetAndConnect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html)(gameObject, localPath, InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html), out prefabSuccess);
            if (prefabSuccess == true)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Prefab was saved successfully");
            else
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Prefab failed to save" + prefabSuccess);
        }
    }  
  
    // Disable the menu item if no selection is in place.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create Prefab", true)]
    static bool ValidateCreatePrefab()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null && !EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html));
    }
}

```

### Static Properties
Property | Description  
---|---  
[prefabInstanceUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceUpdated.html) | Unity calls this method automatically when Prefab instances in the Scene have been updated.  
### Static Methods
Method | Description  
---|---  
[ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html) | Applies the added component to the Prefab Asset at the given asset path.  
[ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html) | Applies the added GameObject to the Prefab Asset at the given asset path.  
[ApplyAddedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObjects.html) | Applies the added GameObjects to the Prefab Asset at the given asset path.  
[ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html) | Applies all overridden properties on a Prefab instance component or GameObject to the Prefab Asset at the given asset path.  
[ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html) | Applies all overrides on a Prefab instance to its Prefab Asset.  
[ApplyPrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstances.html) | Applies all overrides from a list of Prefab instances to their Prefab Assets.  
[ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html) | Applies a single overridden property on a Prefab instance to the Prefab Asset at the given asset path.  
[ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html) | Removes the component from the Prefab Asset which has the component on it.  
[ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html) | Removes the GameObject from the source Prefab Asset.  
[ConvertToPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstance.html) | Convert the plain GameObject to a Prefab instance using the provided Prefab Asset root object.  
[ConvertToPrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstances.html) | Convert an array of GameObjects to Prefab instances of the given Prefab Asset.  
[FindAllInstancesOfPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.FindAllInstancesOfPrefab.html) | Retrieves the root GameObjects for all instances of the Prefab asset with root prefabRoot found in all currently loaded scenes. If prefabRoot is not a valid Prefab asset root GameObject, an ArgumentException is thrown.  
[GetAddedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedComponents.html) | Retrieves a list of PrefabUtility.AddedComponent objects which contain information about added component overrides on the Prefab instance.  
[GetAddedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedGameObjects.html) | Retrieves a list of PrefabUtility.AddedGameObject objects which contain information about added GameObjects on the Prefab instance.  
[GetCorrespondingObjectFromOriginalSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromOriginalSource.html) | Retrieves the object of origin for the given object.  
[GetCorrespondingObjectFromSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html) | Retrieves the corresponding asset object of source, or null if it can't be found.  
[GetCorrespondingObjectFromSourceAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSourceAtPath.html) | Retrieves the corresponding object of the given object from a given Prefab Asset path.  
[GetIconForGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetIconForGameObject.html) | Retrieves the icon for the given GameObject.  
[GetNearestPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetNearestPrefabInstanceRoot.html) | Retrieves the GameObject that is the root of the nearest Prefab instance the object is part of.  
[GetObjectOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetObjectOverrides.html) | Retrieves a list of objects with information about object overrides on the Prefab instance.  
[GetOriginalSourceRootWhereGameObjectIsAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOriginalSourceRootWhereGameObjectIsAdded.html) | Use this method to find the Prefab Asset root where a Prefab instance or Prefab Asset object was added originally.  
[GetOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html) | Retrieves the GameObject that is the root of the outermost Prefab instance the object is part of.  
[GetPrefabAssetPathOfNearestInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot.html) | Retrieves the asset path of the nearest Prefab instance root the specified object is part of.  
[GetPrefabAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabAssetType.html) | Retrieves an enum value indicating the type of Prefab Asset, such as Regular Prefab, Model Prefab and Prefab Variant.  
[GetPrefabInstanceHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabInstanceHandle.html) | Retrieves the PrefabInstance object for the outermost Prefab instance the provided object is part of.  
[GetPrefabInstanceStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabInstanceStatus.html) | Determines whether a Prefab instance is properly connected to its asset.  
[GetPropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPropertyModifications.html) | Returns all modifications that have been applied to a particular Prefab instance in a Scene or modifications for a Prefab instance in an Asset.See SetPropertyModifications for details about the fields of the returned PropertyModification objects.An alternative approach to getting property overrides information for a Prefab instance is to use the GetObjectOverrides API which also has Apply and Revert functionality.When using GetPropertyModifications bear in mind that: it will return both default and non-default overridesIt can return overrides for all child GameObjects and their Componentsit can return overrides that are no longer valid.  
[GetRemovedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedComponents.html) | Returns a list of objects with information about removed component overrides on the Prefab instance.  
[GetRemovedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html) | Returns a list of objects with information about removed GameObject overrides on the Prefab instance.  
[HasManagedReferencesWithMissingTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.HasManagedReferencesWithMissingTypes.html) | Determines whether the object Prefab asset contains any MonoBehaviours with missing SerializeReference types.  
[HasPrefabInstanceAnyOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.HasPrefabInstanceAnyOverrides.html) | Returns true if the given Prefab instance has any overrides.  
[InstantiatePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html) | Instantiates the given Prefab in a given Scene.  
[IsAddedComponentOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsAddedComponentOverride.html) | Returns true if the given component is added to a Prefab instance as an override.  
[IsAddedGameObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsAddedGameObjectOverride.html) | Returns true if the given GameObject is added as a child to a Prefab instance as an override.  
[IsAnyPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsAnyPrefabInstanceRoot.html) | Is the GameObject the root of any Prefab instance?  
[IsDefaultOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) | Returns true if the given modification is considered a default override.  
[IsOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsOutermostPrefabInstanceRoot.html) | Returns true if the given GameObject is an outermost Prefab instance root.  
[IsPartOfAnyPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfAnyPrefab.html) | Returns true if the given object is part of a Prefab Asset or Prefab instance.  
[IsPartOfImmutablePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfImmutablePrefab.html) | Returns true if the given object is part of a Prefab that cannot be edited.  
[IsPartOfModelPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfModelPrefab.html) | Returns true if the given object is part of a Model Prefab Asset or Model Prefab instance.  
[IsPartOfNonAssetPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfNonAssetPrefabInstance.html) | Returns true if the given object is part of a Prefab instance that is not part of a Prefab Asset.  
[IsPartOfPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabAsset.html) | Returns true if the given object is part of a Prefab Asset.  
[IsPartOfPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabInstance.html) | Returns true if the given object is part of a Prefab instance.  
[IsPartOfPrefabThatCanBeAppliedTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabThatCanBeAppliedTo.html) | Returns true if the given object is part of a Prefab to which overrides can be applied to.  
[IsPartOfRegularPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfRegularPrefab.html) | Returns true if the given object is part of a regular Prefab instance or Prefab Asset.  
[IsPartOfVariantPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfVariantPrefab.html) | Returns true if the given object is part of a Prefab Variant Asset or Prefab Variant instance.  
[IsPrefabAssetMissing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPrefabAssetMissing.html) | Returns true if the given object is part of a Prefab instance but the source asset is missing.  
[LoadPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.LoadPrefabContents.html) | Loads a Prefab Asset at a given path into an isolated Scene and returns the root GameObject of the Prefab.  
[LoadPrefabContentsIntoPreviewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.LoadPrefabContentsIntoPreviewScene.html) | Loads a Prefab Asset at a given path into a given preview Scene and returns the root GameObject of the Prefab.  
[MergePrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.MergePrefabInstance.html) | Forces a Prefab instance to merge with changes from the Prefab Asset.  
[RecordPrefabInstancePropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html) | Causes modifications made to the Prefab instance to be recorded.  
[RemoveUnusedOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RemoveUnusedOverrides.html) | This method identifies and removes all unused overrides from a list of Prefab Instance roots. See the manual Unused Overides for more detail.  
[ReplacePrefabAssetOfPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html) | Replace the Prefab Asset for a Prefab instance that exists in a Scene or for a nested Prefab instance inside another Prefab.  
[ReplacePrefabAssetOfPrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html) | Replace the Prefab Asset for an array of Prefab instances that exists in Scenes or for nested Prefab instances inside another Prefab.  
[RevertAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertAddedComponent.html) | Removes this added component on a Prefab instance.  
[RevertAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertAddedGameObject.html) | Removes this added GameObject from a Prefab instance.  
[RevertObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertObjectOverride.html) | Reverts all overridden properties on a Prefab instance component or GameObject.  
[RevertPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertPrefabInstance.html) | Reverts all overrides on a Prefab instance.  
[RevertPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertPropertyOverride.html) | Reverts a single property override on a Prefab instance.  
[RevertRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedComponent.html) | Adds this removed component back on the Prefab instance.  
[RevertRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedGameObject.html) | Adds this removed GameObject back on the Prefab instance.  
[SaveAsPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html) | Creates a Prefab Asset at the given path from the given GameObject, including any childen in the Scene without modifying the input objects.  
[SaveAsPrefabAssetAndConnect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html) | Creates a Prefab Asset at the given path from the given GameObject, including any children in the Scene and at the same time make the given GameObject into an instance of the new Prefab.  
[SavePrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SavePrefabAsset.html) | Saves the version of an existing Prefab Asset that exists in memory back to disk.  
[SetPropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html) | Assigns a set of PropertyModification objects to a target Prefab instance relative to its source Prefab Asset.  
[UnloadPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnloadPrefabContents.html) | Releases the content from a Prefab previously loaded with LoadPrefabContents from memory.  
[UnpackAllInstancesOfPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackAllInstancesOfPrefab.html) | Unpacks all instances of a given Prefab Asset root GameObject in all open scenes so that all instances are replaced with the contents of the Prefab Asset while retaining all override values.  
[UnpackPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstance.html) | Unpacks a given Prefab instance so that it is replaced with the contents of the Prefab Asset while retaining all override values.  
[UnpackPrefabInstanceAndReturnNewOutermostRoots](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstanceAndReturnNewOutermostRoots.html) | Unpacks the given Prefab instance using the behaviour specified by unpackMode.  
### Events
Event | Description  
---|---  
[prefabInstanceApplied](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceApplied.html) | Unity calls this method automatically after a Prefab instance has been applied.  
[prefabInstanceApplying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceApplying.html) | Unity calls this method automatically before a Prefab instance is applied.  
[prefabInstanceReverted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceReverted.html) | Unity calls this method automatically after a Prefab instance has been reverted.  
[prefabInstanceReverting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceReverting.html) | Unity calls this method automatically before a Prefab instance is reverted.  
[prefabInstanceUnpacked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceUnpacked.html) | Unity calls this method automatically after a Prefab instance is unpacked.  
[prefabInstanceUnpacking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility-prefabInstanceUnpacking.html) | Unity calls this method automatically before a Prefab instance is unpacked.  
### Delegates
Delegate | Description  
---|---  
[PrefabInstanceUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.PrefabInstanceUpdated.html) | Delegate for method that is called after Prefab instances in the Scene have been updated.  
* * *
