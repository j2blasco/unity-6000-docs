* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertPrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertPrefabInstance
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
**Obsolete** Use the overload that takes an InteractionMode parameter.
## Declaration
public static bool RevertPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go); 
## Declaration
public static void RevertPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | The root of the Prefab instance.  
action | The interaction mode for this action.  
### Description
Reverts all overrides on a Prefab instance.
This reverts all property overrides, added and removed components, and added child GameObjects (including added child Prefab instances).  
  
The Transform position and rotation of a root GameObject in a Prefab instance is not cleared, nor are other [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html) properties.
* * *
