* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html

# VideoClip
class in UnityEngine.Video
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.VideoModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.VideoModule.html)
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
A container for video data.
A VideoClip stores the video portion of a movie file using a codec that is appropriate for the target platform. VideoClips are referenced by [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)s to play videos.
### Properties
Property | Description  
---|---  
[audioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-audioTrackCount.html) | Gets the number of audio tracks that are embedded in the video clip. (Read Only).  
[frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-frameCount.html) | The length of the video clip in frames. (Read Only).  
[frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-frameRate.html) | The frame rate of the clip in frames per second. (Read Only).  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-height.html) | The height of the images in the video clip in pixels. (Read Only).  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-length.html) | The length of the video clip in seconds. (Read Only).  
[originalPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-originalPath.html) | Gets the original video clip file path as it was imported into Unity. (Read Only).  
[pixelAspectRatioDenominator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-pixelAspectRatioDenominator.html) | Returns the denominator of the pixel aspect ratio (numerator:denominator). (Read Only).  
[pixelAspectRatioNumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-pixelAspectRatioNumerator.html) | Returns the numerator of the pixel aspect ratio (numerator:denominator). (Read Only).  
[sRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-sRGB.html) | Whether the imported clip contains sRGB color data (Read Only).  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-width.html) | The width of the images in the video clip in pixels. (Read Only).  
### Public Methods
Method | Description  
---|---  
[GetAudioChannelCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioChannelCount.html) | Returns the number of channels in the audio track. For example, if the audio track is a stereo track, this function returns 2.  
[GetAudioLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioLanguage.html) | Gets the language of the video clip’s audio tracks, if the audio tracks have an assigned language.  
[GetAudioSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioSampleRate.html) | Get the audio track sampling rate in hertz (Hz).  
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
