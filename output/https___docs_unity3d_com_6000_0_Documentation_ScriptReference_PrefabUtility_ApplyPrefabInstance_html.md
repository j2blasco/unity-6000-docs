* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ApplyPrefabInstance
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
public static void ApplyPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | The root of the given Prefab instance.  
action | The interaction mode for this action.  
### Description
Applies all overrides on a Prefab instance to its Prefab Asset.
This method allows you to apply the complete modified state of a Prefab instance to its source Prefab Asset, which includes all property overrides, added and removed components, and added child GameObjects (including added child Prefab instances).  
  
It mirrors the functionality of the "Apply All" button in the [overrides menu](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html) in the editor. To use this method, you must first modify an existing Prefab instance in some way, such as modifying properties, or adding or removing GameObjects or components.  
  
Modifications to a Prefab instance that have not been applied are called [instance overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html). The act of applying the modifications means the modifications become part of the Prefab Asset, and are no longer overrides.  
  
When applying all modifications to a Prefab Asset using this method to nested Prefabs or Prefab variants, the changes are always applied to the outermost Prefab. To apply changes to inner Prefabs, you can use the other methods such as [PrefabUtility.ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html), [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html), [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html) and [PrefabUtility.ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html).  
  
The Transform position and rotation of a root GameObject in a Prefab instance cannot be applied, nor can other [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) properties.  
  
You can read more in the user manual about [modifying and applying changes to Prefab instances](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html).  
  
Additional resources: [PrefabUtility.ApplyPrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstances.html), [PrefabUtility.ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html), [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html), [PrefabUtility.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html), [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html).
* * *
