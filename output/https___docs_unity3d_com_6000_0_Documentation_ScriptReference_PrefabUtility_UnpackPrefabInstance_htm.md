* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).UnpackPrefabInstance
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
public static void UnpackPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, [PrefabUnpackMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUnpackMode.html) unpackMode, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | The root of the Prefab instance to unpack.  
unpackMode | Whether to unpack the outermost root or unpack completely.  
action | The interaction mode to use for this action.  
### Description
Unpacks a given Prefab instance so that it is replaced with the contents of the Prefab Asset while retaining all override values.
The given object must be the root of a Prefab instance.  
  
The contents of a Prefab Asset is the objects you see when you open it in Prefab Mode. Unpacking with a PrefabUnpackMode of OutermostRoot will replace the Prefab instance with that content. Unpacking with a PrefabUnpackMode of Completely will furthermore also unpack any Prefab instances that are part of the unpacked content, so that the end result is nothing but regular GameObjects and no Prefab instances.  
  
The contents of a regular Prefab or a Model Prefab always has a regular GameObject at the root, so unpacking one of those will leave a regular GameObject at the root where the Prefab instance was before.  
  
The contents of a Prefab Variant has an instance of the base Prefab at the root, so unpacking a Prefab Variant with a PrefabUnpackMode of OutermostRoot will leave an instance of the base Prefab where the Prefab Variant instance was before.  
  
Unpacking throws an ArgumentException if the given object is not the root of a Prefab instance, or if it’s part of a Prefab Asset. This does not include Prefab contents opened in Prefab Mode.  
  
InteractionMode determines if the action should be undoable.
* * *
