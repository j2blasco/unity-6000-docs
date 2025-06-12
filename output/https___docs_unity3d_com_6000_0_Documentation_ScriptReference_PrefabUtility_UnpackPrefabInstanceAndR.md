* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstanceAndReturnNewOutermostRoots.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).UnpackPrefabInstanceAndReturnNewOutermostRoots
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
public static GameObject[] UnpackPrefabInstanceAndReturnNewOutermostRoots([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, [PrefabUnpackMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUnpackMode.html) unpackMode); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | Root GameObject of the Prefab instance.  
unpackMode | The unpack mode to use.  
### Returns
**GameObject[]** Array of GameObjects representing roots of unpacked Prefab instances. 
### Description
Unpacks the given Prefab instance using the behaviour specified by unpackMode.
If the PrefabUnpackMode is the PrefabUnpackMode.OutermostRoot this function will return any new Prefab root GameObjects from any nested Prefabs at the first level.  
  
Unlike [UnpackPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstance.html), this function can’t be made undoable. You will have to handle undo yourself.  
  
See [UnpackPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstance.html) for a full description of the unpacking behaviour.
* * *
