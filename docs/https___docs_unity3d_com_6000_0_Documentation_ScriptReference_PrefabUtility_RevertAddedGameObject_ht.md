* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertAddedGameObject.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertAddedGameObject
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
public static void RevertAddedGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
action | The interaction mode for this action.  
gameObject | The added GameObject on the Prefab instance to revert.  
### Description
Removes this added GameObject from a Prefab instance.
After the revert action, the GameObject and its children no longer exist.  
  
This method also works if the added child GameObject is a Prefab instance.
* * *
