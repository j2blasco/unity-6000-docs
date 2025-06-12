* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ApplyAddedComponent
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
public static void ApplyAddedComponent([Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) component, string assetPath, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
action | The interaction mode for this action.  
assetPath | The path of the Prefab Asset to apply to.  
component | The added component on the Prefab instance to apply.  
### Description
Applies the added component to the Prefab Asset at the given asset path.
This method allows you to apply an added component to an existing Prefab. It mirrors the functionality in the editor, described in [the user manual here](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html). To use this method, you must first add a component to an existing Prefab instance.  
  
An added component is a type of [Instance Override](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html). The act of applying the added component to the Prefab means the component becomes part of the Prefab Asset, and is no longer an override on the Prefab instance.  
  
When applying an added component to a Prefab Asset, you must supply the asset path as a parameter. This is because there are some situations where there are multiple possible targets to apply the change to. For example, if the added component has been added to a GameObject that is part of a [nested Prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html), you may have the choice of applying the change to the inner nested Prefab Asset, or to the outer root Prefab Asset. Therefore, by specifying the asset path, you make it clear to Unity which Prefab Asset the change must be applied to.  
  
You can read more in the user manual about the [choice of apply targets](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html).  
  
Additional resources: [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html), [PrefabUtility.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html), [PrefabUtility.ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html), [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html).
* * *
