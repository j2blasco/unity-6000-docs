* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertObjectOverride.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertObjectOverride
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
public static void RevertObjectOverride([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) instanceComponentOrGameObject, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
action | The interaction mode for this action.  
instanceComponentOrGameObject | The object on the Prefab instance to revert.  
### Description
Reverts all overridden properties on a Prefab instance component or GameObject.
If the specified object is a GameObject, only the overrides on the GameObject itself are reverted; not its components or child GameObjects.  
  
After the apply action, the properties on the object on the Prefab instance are no longer marked as overrides and now reflect the values of the Prefab Asset.  
  
The Transform position and rotation of a root GameObject in a Prefab instance cannot be reverted, nor can other [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) properties.
* * *
