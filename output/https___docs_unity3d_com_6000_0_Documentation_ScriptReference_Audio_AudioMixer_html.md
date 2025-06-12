* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html

# AudioMixer
class in UnityEngine.Audio
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.AudioModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AudioModule.html)
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
### Description
AudioMixer asset.
This is a singleton representing a specific audio mixer asset in the project.
### Properties
Property | Description  
---|---  
[outputAudioMixerGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer-outputAudioMixerGroup.html) | Routing target.  
[updateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer-updateMode.html) | How time should progress for this AudioMixer. Used during Snapshot transitions.  
### Public Methods
Method | Description  
---|---  
[ClearFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.ClearFloat.html) | Resets an exposed parameter to its initial value.  
[FindMatchingGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.FindMatchingGroups.html) | Connected groups in the mixer form a path from the mixer's master group to the leaves. This path has the format Master Group/Child of Master Group/Grandchild of Master Group, and so on. For example, in the hierarchy below, the group DROPS has the path Master/WATER/DROPS. To return only the group called DROPS, enter DROPS. The substring Master/AMBIENCE returns three groups, AMBIENCE/CROWD, AMBIENCE/ROAD, and AMBIENCE. The substring /R would return both ROAD and RIVER.  
[FindSnapshot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.FindSnapshot.html) | The name must be an exact match.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.GetFloat.html) | Returns the value of the exposed parameter specified. If the parameter doesn't exist the function returns false. Prior to calling SetFloat and after ClearFloat has been called on this parameter the value returned will be that of the current snapshot or snapshot transition.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.SetFloat.html) | Sets the value of the exposed parameter specified. When a parameter is exposed, it is not controlled by mixer snapshots. You can only change the parameter with this function.  
[TransitionToSnapshots](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.TransitionToSnapshots.html) | Transitions to a weighted mixture of the snapshots specified. This can be used for games that specify the game state as a continuum between states or for interpolating snapshots from a triangulated map location.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
