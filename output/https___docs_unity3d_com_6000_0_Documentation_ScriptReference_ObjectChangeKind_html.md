* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.html

# ObjectChangeKind
enumeration
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
This enumeration describes the different kind of changes that can be tracked in an [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html). Each event has a corresponding type in [ObjectChangeEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[InitializeOnLoad]
public class ObjectChangeEventsExample
{
    static ObjectChangeEventsExample()
    {
        ObjectChangeEvents.changesPublished[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents-changesPublished.html) += ChangesPublished;
    }  
  
    static void ChangesPublished(ref ObjectChangeEventStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html) stream)
    {
        for (int i = 0; i < stream.length; ++i)
        {
            var type = stream.GetEventType(i);
            switch (type)
            {
                case ObjectChangeKind.ChangeScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeScene.html):
                    stream.GetChangeSceneEvent(i, out var changeSceneEvent);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {changeSceneEvent.scene}");
                    break;  
  
                case ObjectChangeKind.CreateGameObjectHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.CreateGameObjectHierarchy.html):
                    stream.GetCreateGameObjectHierarchyEvent(i, out var createGameObjectHierarchyEvent);
                    var newGameObject = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(createGameObjectHierarchyEvent.instanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {newGameObject} in scene {createGameObjectHierarchyEvent.scene}.");
                    break;  
  
                case ObjectChangeKind.ChangeGameObjectStructureHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectStructureHierarchy.html):
                    stream.GetChangeGameObjectStructureHierarchyEvent(i, out var changeGameObjectStructureHierarchy);
                    var gameObject = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectStructureHierarchy.instanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {gameObject} in scene {changeGameObjectStructureHierarchy.scene}.");
                    break;  
  
                case ObjectChangeKind.ChangeGameObjectStructure[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectStructure.html):
                    stream.GetChangeGameObjectStructureEvent(i, out var changeGameObjectStructure);
                    var gameObjectStructure = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectStructure.instanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {gameObjectStructure} in scene {changeGameObjectStructure.scene}.");
                    break;  
  
                case ObjectChangeKind.ChangeGameObjectParent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectParent.html):
                    stream.GetChangeGameObjectParentEvent(i, out var changeGameObjectParent);
                    var gameObjectChanged = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.instanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    var newParentGo = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.newParentInstanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    var previousParentGo = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectParent.previousParentInstanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {gameObjectChanged} from {previousParentGo} to {newParentGo} from scene {changeGameObjectParent.previousScene} to scene {changeGameObjectParent.newScene}.");
                    break;  
  
                case ObjectChangeKind.ChangeGameObjectOrComponentProperties[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectOrComponentProperties.html):
                    stream.GetChangeGameObjectOrComponentPropertiesEvent(i, out var changeGameObjectOrComponent);
                    var goOrComponent = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeGameObjectOrComponent.instanceId);
                    if (goOrComponent is GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
                    {
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) {go} change properties in scene {changeGameObjectOrComponent.scene}.");
                    }
                    else if (goOrComponent is Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) component)
                    {
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) {component} change properties in scene {changeGameObjectOrComponent.scene}.");
                    }
                    break;  
  
                case ObjectChangeKind.DestroyGameObjectHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.DestroyGameObjectHierarchy.html):
                    stream.GetDestroyGameObjectHierarchyEvent(i, out var destroyGameObjectHierarchyEvent);
                    // The destroyed GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can not be converted with EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html) as it has already been destroyed.
                    var destroyParentGo = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(destroyGameObjectHierarchyEvent.parentInstanceId) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {destroyGameObjectHierarchyEvent.instanceId} with parent {destroyParentGo} in scene {destroyGameObjectHierarchyEvent.scene}.");
                    break;  
  
                case ObjectChangeKind.CreateAssetObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.CreateAssetObject.html):
                    stream.GetCreateAssetObjectEvent(i, out var createAssetObjectEvent);
                    var createdAsset = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(createAssetObjectEvent.instanceId);
                    var createdAssetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(createAssetObjectEvent.guid);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {createdAsset} at {createdAssetPath} in scene {createAssetObjectEvent.scene}.");
                    break;  
  
                case ObjectChangeKind.DestroyAssetObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.DestroyAssetObject.html):
                    stream.GetDestroyAssetObjectEvent(i, out var destroyAssetObjectEvent);
                    // The destroyed asset can not be converted with EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html) as it has already been destroyed.
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: Instance Id {destroyAssetObjectEvent.instanceId} with Guid {destroyAssetObjectEvent.guid} in scene {destroyAssetObjectEvent.scene}.");
                    break;  
  
                case ObjectChangeKind.ChangeAssetObjectProperties[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeAssetObjectProperties.html):
                    stream.GetChangeAssetObjectPropertiesEvent(i, out var changeAssetObjectPropertiesEvent);
                    var changeAsset = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(changeAssetObjectPropertiesEvent.instanceId);
                    var changeAssetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(changeAssetObjectPropertiesEvent.guid);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type}: {changeAsset} at {changeAssetPath} in scene {changeAssetObjectPropertiesEvent.scene}.");
                    break;  
  
                case ObjectChangeKind.UpdatePrefabInstances[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.UpdatePrefabInstances.html):
                    stream.GetUpdatePrefabInstancesEvent(i, out var updatePrefabInstancesEvent);
                    string s = "";
                    s += $"{type}: scene {updatePrefabInstancesEvent.scene}. Instances ({updatePrefabInstancesEvent.instanceIds.Length}):\n";
                    foreach (var prefabId in updatePrefabInstancesEvent.instanceIds)
                    {
                        s += EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(prefabId).ToString() + "\n";
                    }
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(s);
                    break;
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.None.html) | Indicates an uninitialized value.  
[ChangeScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeScene.html) | A change of this type indicates that an open scene has been changed ("dirtied") without any more specific information available. This happens for example when EditorSceneManager.MarkSceneDirty is used.  
[CreateGameObjectHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.CreateGameObjectHierarchy.html) | A change of this type indicates that a GameObject has been created, possibly with additional objects below it in the hierarchy. This happens for example when Undo.RegisterCreatedObjectUndo is used with a GameObject.  
[ChangeGameObjectStructureHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectStructureHierarchy.html) | A change of this type indicates that the structure of a GameObject has changed and any GameObject in the hierarchy below it might have changed. This happens for example when Undo.RegisterFullObjectHierarchyUndo is used.  
[ChangeGameObjectStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectStructure.html) | A change of this type indicates that the structure of a GameObject has changed. This happens when a component is added to or removed from the GameObject using Undo.AddComponent or Undo.DestroyObjectImmediate.  
[ChangeGameObjectParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectParent.html) | A change of this type indicates that the parent of a GameObject has changed. This happens when Undo.SetTransformParent or SceneManager.MoveGameObjectToScene is used.  
[ChangeGameObjectOrComponentProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeGameObjectOrComponentProperties.html) | A change of this type indicates that a property of a GameObject or Component has changed. This happens for example when Undo.RecordObject is used with an instance of a Component.  
[DestroyGameObjectHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.DestroyGameObjectHierarchy.html) | A change of this type indicates that a GameObject and the entire hierarchy below it has been destroyed. This happens for example when Undo.DestroyObjectImmediate is used with an GameObject.  
[CreateAssetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.CreateAssetObject.html) | A change of this type indicates that an asset object has been created. This happens for example when Undo.RegisterCreatedObjectUndo is used with an instance of an asset (e.g. Texture). Note that this only covers creation of asset objects in memory and not creation of new assets in the project on disk.  
[DestroyAssetObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.DestroyAssetObject.html) | A change of this type indicates that an asset object has been destroyed. This happens for example when Undo.DestroyObjectImmediate is used with an instance of an asset (e.g. Texture). Note that this only covers destruction of asset objects in memory and not deletion of assets in the project on disk.  
[ChangeAssetObjectProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeAssetObjectProperties.html) | A change of this type indicates that a property of an asset object in memory has changed. This happens for example when Undo.RecordObject is used with an instance of an asset (e.g. Texture). Note that this only covers changes to asset objects in memory and not changes to assets in the project on disk.  
[UpdatePrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.UpdatePrefabInstances.html) | A change of this type indicates that prefab instances in an open scene have been updated due to a change to the source prefab.  
[ChangeChildrenOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeChildrenOrder.html) | A change of this type indicates that a child has been reordered in the hierarchy under the same parent. This happens when Undo.RegisterChildrenOrderUndo is called or when reordering a child in the hierarchy under the same parent.  
[ChangeRootOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.ChangeRootOrder.html) | A change of this type indicates that a GameObject placed at the scene root has been reordered in the hierarchy. This happens when Undo.SetSiblingIndex is called or when reordering such a GameObject in the hierarchy under the same scene.  
* * *
