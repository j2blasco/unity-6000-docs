* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertPropertyOverride.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertPropertyOverride
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
public static void RevertPropertyOverride([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) instanceProperty, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
action | The interaction mode for this action.  
instanceProperty | The SerializedProperty representing the property to revert.  
### Description
Reverts a single property override on a Prefab instance.
After the apply action, the property on the Prefab instance is no longer marked as an override and now reflects the value of the Prefab Asset.  
  
Note that you can revert [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) properties with this method, unlike with other apply methods, which will not apply default override properties.
* * *
