* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ApplyObjectOverride
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
public static void ApplyObjectOverride([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) instanceComponentOrGameObject, string assetPath, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
instanceComponentOrGameObject | The object on the Prefab instance to apply.  
assetPath | The path of the Prefab Asset to apply to.  
action | The interaction mode for this action.  
### Description
Applies all overridden properties on a Prefab instance component or GameObject to the Prefab Asset at the given asset path.
This method allows you to apply modified property values to an existing Prefab. It mirrors the functionality in the editor, described in [the user manual here](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html). To use this method, you must first modify one or more property values on an existing Prefab instance.  
  
If you pass a GameObject as the object parameter, only the overrides on the GameObject itself are applied (such as layer, tag, and static flags); not its components or child GameObjects. If you pass a Component as the object parameter, only the overrides on that Component are applied. To apply all overrides of a Prefab, you can use [PrefabUtility.ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html).  
  
Modified property values on a Prefab instance are a type of [Instance Override](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html). The act of applying the modified property values to the Prefab means the modifed values become part of the Prefab Asset, and are no longer overrides.  
  
When applying modified property values to a Prefab Asset, you must supply the asset path as a parameter. This is because there are some situations where there are multiple possible targets to apply the change to. For example, if the property values have been modified on a GameObject that is part of a [nested Prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html), you may have the choice of applying the change to the inner nested Prefab Asset, or to the outer root Prefab Asset. Therefore, by specifying the asset path, you make it clear to Unity which Prefab Asset the change must be applied to.  
  
You can read more in the user manual about the [choice of apply targets](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html).  
  
Additional resources: [PrefabUtility.ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html), [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html), [PrefabUtility.ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html), [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html).
* * *
