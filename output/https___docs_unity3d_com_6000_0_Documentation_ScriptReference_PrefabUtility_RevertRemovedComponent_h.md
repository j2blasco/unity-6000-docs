* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedComponent.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertRemovedComponent
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
public static void RevertRemovedComponent([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceGameObject, [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) assetComponent, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
assetComponent | The removed component on the Prefab instance to revert.  
action | The interaction mode for this action.  
instanceGameObject | The GameObject on the Prefab instance which the component has been removed from.  
### Description
Adds this removed component back on the Prefab instance.
After the revert action, the component exists on the Prefab instance again.
* * *
