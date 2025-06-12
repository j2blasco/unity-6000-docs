* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html

# AudioClip
class in UnityEngine
/
Inherits from:[Audio.AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html "Go to AudioClip Component in the Manual")
### Description
A container for audio data.
An AudioClip stores the audio file either compressed as ogg vorbis or uncompressed. AudioClips are referenced and used by AudioSources to play sounds.  
  
Additional resources: [AudioClip component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) in the Components Reference.
### Properties
Property | Description  
---|---  
[ambisonic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-ambisonic.html) | Returns true if this audio clip is ambisonic (read-only).  
[channels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-channels.html) | The number of channels in the audio clip. (Read Only)  
[frequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-frequency.html) | The sample frequency of the clip in Hertz. (Read Only)  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-length.html) | The length of the audio clip in seconds. (Read Only)  
[loadInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadInBackground.html) | Enable this property to load the AudioClip asynchronously in the background instead of on the main thread. Set this property in the Inspector (Read Only).  
[loadState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadState.html) | Returns the current load state of the audio data associated with an AudioClip.  
[loadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadType.html) | The load type of the clip (read-only).  
[preloadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-preloadAudioData.html) | Enable this property in the Inspector to preload audio data from the audio clip when loading the clip Asset (Read Only).  
[samples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-samples.html) | The length of the audio clip in samples. (Read Only)  
### Public Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.GetData.html) | Fills an array with sample data from the audio clip.  
[LoadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.LoadAudioData.html) | Loads the asset data of an AudioClip into memory, so it will immediately be ready to play.  
[SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.SetData.html) | Fills an audio clip with sample data from an array or Span. Overwrites existing data if necessary.  
[UnloadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.UnloadAudioData.html) | Unloads the audio data associated with the clip. This works only for AudioClips that are based on actual sound file assets.  
### Static Methods
Method | Description  
---|---  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html) | Creates a user AudioClip with a name and with the given length in samples, channels and frequency.  
### Delegates
Delegate | Description  
---|---  
[PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) | Unity calls this delegate each time AudioClip reads data.  
[PCMSetPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMSetPositionCallback.html) | Unity calls this delegate each time AudioClip changes read position.  
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
