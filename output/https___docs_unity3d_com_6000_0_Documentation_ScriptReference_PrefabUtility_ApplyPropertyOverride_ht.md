* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ApplyPropertyOverride
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
public static void ApplyPropertyOverride([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) instanceProperty, string assetPath, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
instanceProperty | The SerializedProperty representing the property to apply.  
assetPath | The path of the Prefab Asset to apply to.  
action | The interaction mode for this action.  
### Description
Applies a single overridden property on a Prefab instance to the Prefab Asset at the given asset path.
This method allows you to apply a single modified property value to an existing Prefab Asset. It mirrors the functionality in the editor, described in [the user manual here](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html). To use this method, you must first modify a property value on an existing Prefab instance.  
  
Modified property values on a Prefab instance are a type of [Instance Override](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html). The act of applying a modified property value to the Prefab means the modifed value becomes part of the Prefab Asset, and is no longer an override on the Prefab instance.  
  
When applying a modified property value to a Prefab Asset, you must supply the asset path as a parameter. This is because there are some situations where there are multiple possible targets to apply the change to. For example, if the property value has been modified on a GameObject that is part of a [nested Prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html), you may have the choice of applying the change to the inner nested Prefab Asset, or to the outer root Prefab Asset. Therefore, by specifying the asset path, you make it clear to Unity which Prefab Asset the change must be applied to.  
  
You can read more in the user manual about the [choice of apply targets](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html).  
  
Note that you can apply [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) properties with this method, unlike with other apply methods, which will not apply default override properties.  
  
If a property is an array element and the corresponding array element doesn't exist in the Prefab Asset because the array is shorter there, ApplyPropertyOverride applies the entire array. If the InteractionMode is set to UserAction, Unity shows a dialog box which provides options to proceed or cancel.  
  
Additional resources: [PrefabUtility.ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html), [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html), [PrefabUtility.ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html), [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html).
* * *
