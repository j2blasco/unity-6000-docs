* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone.html

# AudioReverbZone
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html "Go to AudioReverbZone Component in the Manual")
### Description
Reverb Zones are used when you want to create location based ambient effects in the Scene.
As the Audio Listener moves into a Reverb Zone, the ambient effect associated with the zone is gradually applied. At the max distance there is no effect and at the min distance the effect is fully applied. For example you can gradually change your character's footsteps sounds and create the feeling like you where entering into a cavern, going trough a room, swimming underwater, etc.  
  
You can always mix reverb zones to have combined effects. For more info check [Reverb Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html) in the manual.
### Properties
Property | Description  
---|---  
[decayHFRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-decayHFRatio.html) | High-frequency to mid-frequency decay time ratio.  
[decayTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-decayTime.html) | Reverberation decay time at mid frequencies.  
[density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-density.html) | Value that controls the modal density in the late reverberation decay.  
[diffusion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-diffusion.html) | Value that controls the echo density in the late reverberation decay.  
[HFReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone.HFReference.html) | Reference high frequency (hz).  
[LFReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone.LFReference.html) | Reference low frequency (hz).  
[maxDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-maxDistance.html) | The distance from the centerpoint that the reverb will not have any effect. Default = 15.0.  
[minDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-minDistance.html) | The distance from the centerpoint that the reverb will have full effect at. Default = 10.0.  
[reflections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-reflections.html) | Early reflections level relative to room effect.  
[reflectionsDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-reflectionsDelay.html) | Initial reflection delay time.  
[reverb](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-reverb.html) | Late reverberation level relative to room effect.  
[reverbDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-reverbDelay.html) | Late reverberation delay time relative to initial reflection.  
[reverbPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-reverbPreset.html) | Set/Get reverb preset properties.  
[room](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-room.html) | Room effect level (at mid frequencies).  
[roomHF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-roomHF.html) | Relative room effect level at high frequencies.  
[roomLF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone-roomLF.html) | Relative room effect level at low frequencies.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
