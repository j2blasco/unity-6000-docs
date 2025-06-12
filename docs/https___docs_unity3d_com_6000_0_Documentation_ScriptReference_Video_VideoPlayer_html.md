* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html

# VideoPlayer
class in UnityEngine.Video
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
Plays video content onto a target.
Content can be either a [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) imported asset or a URL such as `file://` or `http://`. Video content will be projected onto one of the supported targets, such as camera background or [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html). If the video content includes transparency, this transparency will be present in the target, allowing objects behind the video target to be visible. When the data [VideoPlayer.source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-source.html) is set to URL, the audio and video description of what is being played will only be initialized once the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) preparation is completed. You can test this with [VideoPlayer.isPrepared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html).  
  
Refer to [Video file compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html) for more information on supported video file formats.  
  
**The following demonstrates a few features of the VideoPlayer:**
```
// Examples of VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) function  
  
using UnityEngine;
using UnityEngine.Video;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Will attach a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) to the main camera.
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) camera = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)");  
  
        // VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) automatically targets the camera backplane when it is added
        // to a camera object, no need to change videoPlayer.targetCamera.
        var videoPlayer = camera.AddComponent<UnityEngine.Video.VideoPlayer>();  
  
        // Play on awake defaults to true. Set it to false to avoid the url set
        // below to auto-start playback since we're in Start().
        videoPlayer.playOnAwake = false;  
  
        // By default, VideoPlayers added to a camera will use the far plane.
        // Let's target the near plane instead.
        videoPlayer.renderMode = UnityEngine.Video.VideoRenderMode.CameraNearPlane;  
  
        // This will cause our Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to be visible through the video being played.
        videoPlayer.targetCameraAlpha = 0.5F;  
  
        // Set the video to play. URL supports local absolute or relative paths.
        // Here, using absolute.
        videoPlayer.url = "/Users/graham/movie.mov";  
  
        // Skip the first 100 frames.
        videoPlayer.frame = 100;  
  
        // Restart from beginning when done.
        videoPlayer.isLooping = true;  
  
        // Each time we reach the end, we slow down the playback by a factor of 10.
        videoPlayer.loopPointReached += EndReached;  
  
        // Start playback. This means the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) may have to prepare (reserve
        // resources, pre-load a few frames, etc.). To better control the delays
        // associated with this preparation one can use videoPlayer.Prepare() along with
        // its prepareCompleted event.
        videoPlayer.Play();
    }  
  
    void EndReached(UnityEngine.Video.VideoPlayer vp)
    {
        vp.playbackSpeed = vp.playbackSpeed / 10.0F;
    }
}

```

### Static Properties
Property | Description  
---|---  
[controlledAudioTrackMaxCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-controlledAudioTrackMaxCount.html) | Maximum number of audio tracks that can be controlled. (Read Only)  
### Properties
Property | Description  
---|---  
[aspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-aspectRatio.html) | Defines how the video content will be stretched to fill the target area.  
[audioOutputMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-audioOutputMode.html) | Destination for the audio embedded in the video.  
[audioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-audioTrackCount.html) | Number of audio tracks found in the data source currently configured. (Read Only)  
[canSetDirectAudioVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canSetDirectAudioVolume.html) | Whether direct-output volume controls are supported for the current platform and video format. (Read Only)  
[canSetPlaybackSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canSetPlaybackSpeed.html) | Whether you can change the playback speed. (Read Only)  
[canSetSkipOnDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canSetSkipOnDrop.html) | Whether frame-skipping to maintain synchronization can be controlled. (Read Only)  
[canSetTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canSetTime.html) | Whether you can change the current time using the VideoPlayer.time or VideoPlayer.frame properties. (Read Only)  
[canSetTimeUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canSetTimeUpdateMode.html) | Whether you can change the time source followed by the VideoPlayer. (Read Only)  
[canStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-canStep.html) | Returns true if the VideoPlayer can step forward through the video content. (Read Only)  
[clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-clip.html) | The clip being played by the VideoPlayer.  
[clockTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-clockTime.html) | The clock time that the VideoPlayer follows to schedule its samples. The clock time is expressed in seconds. (Read Only)  
[controlledAudioTrackCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-controlledAudioTrackCount.html) | Number of audio tracks that this VideoPlayer will take control of.  
[externalReferenceTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-externalReferenceTime.html) | Reference time of the external clock the VideoPlayer uses to correct its drift.  
[frame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frame.html) | The frame index of the currently available frame in VideoPlayer.texture.  
[frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameCount.html) | Number of frames in the current video content. (Read Only)  
[frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameRate.html) | The frame rate of the clip or URL in frames/second. (Read Only)  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-height.html) | The height of the images in the VideoClip, or URL, in pixels. (Read Only)  
[isLooping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isLooping.html) | Determines whether the VideoPlayer restarts from the beginning when it reaches the end of the clip.  
[isPaused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPaused.html) | Whether playback is paused. (Read Only)  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPlaying.html) | Returns whether the VideoPlayer is currently playing the content.  
[isPrepared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html) | Returns whether the VideoPlayer has successfully prepared the content to be played.   
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-length.html) | The length of the VideoClip, or the URL, in seconds. (Read Only)  
[pixelAspectRatioDenominator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-pixelAspectRatioDenominator.html) | Denominator of the pixel aspect ratio (num:den) for the VideoClip or the URL. (Read Only)  
[pixelAspectRatioNumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-pixelAspectRatioNumerator.html) | Numerator of the pixel aspect ratio (num:den) for the VideoClip or the URL. (Read Only)  
[playbackSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-playbackSpeed.html) | Factor by which the basic playback rate will be multiplied.  
[playOnAwake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-playOnAwake.html) | Whether the content will start playing back as soon as the component awakes.  
[renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-renderMode.html) | Where the video content will be drawn.  
[sendFrameReadyEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-sendFrameReadyEvents.html) | Enables the frameReady events.  
[skipOnDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-skipOnDrop.html) | Whether the VideoPlayer is allowed to skip frames to catch up with current time.  
[source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-source.html) | The source that the VideoPlayer uses for playback.  
[targetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetCamera.html) |  Camera component to draw to when VideoPlayer.renderMode is set to either VideoRenderMode.CameraFarPlane or VideoRenderMode.CameraNearPlane.  
[targetCamera3DLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetCamera3DLayout.html) | Type of 3D content contained in the source video media.  
[targetCameraAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetCameraAlpha.html) | Overall transparency level of the target camera plane video.  
[targetMaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetMaterialProperty.html) |  Material texture property which is targeted when VideoPlayer.renderMode is set to Video.VideoTarget.MaterialOverride.  
[targetMaterialRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetMaterialRenderer.html) |  Renderer which is targeted when VideoPlayer.renderMode is set to Video.VideoTarget.MaterialOverride  
[targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetTexture.html) |  RenderTexture to draw to when VideoPlayer.renderMode is set to Video.VideoTarget.RenderTexture.  
[texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-texture.html) | Internal texture in which video content is placed. (Read Only)  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-time.html) | The presentation time of the currently available frame in VideoPlayer.texture in seconds.  
[timeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-timeReference.html) | The clock that the VideoPlayer observes to detect and correct drift.  
[timeUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-timeUpdateMode.html) | The clock source used by the VideoPlayer to derive its current time.  
[url](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-url.html) | The file URL or web URL that the VideoPlayer reads content from.  
[waitForFirstFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-waitForFirstFrame.html) | Determines whether the VideoPlayer will wait for the first frame to be loaded into the texture before starting playback when VideoPlayer.playOnAwake is on.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-width.html) | The width of the images in the VideoClip, or URL, in pixels. (Read Only)  
### Public Methods
Method | Description  
---|---  
[EnableAudioTrack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EnableAudioTrack.html) | Enable/disable audio track decoding. Only effective when the VideoPlayer is not currently playing.  
[GetAudioChannelCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioChannelCount.html) | The number of audio channels in the specified audio track.  
[GetAudioLanguageCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioLanguageCode.html) | Returns the language code, if any, for the specified track.  
[GetAudioSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioSampleRate.html) | Gets the audio track sampling rate in Hertz.  
[GetDirectAudioMute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetDirectAudioMute.html) | Gets the direct-output audio mute status for the specified track.  
[GetDirectAudioVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetDirectAudioVolume.html) | Return the direct-output volume for specified track.  
[GetTargetAudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetTargetAudioSource.html) | Gets the AudioSource that will receive audio samples for the specified track if VideoPlayer.audioOutputMode is set to VideoAudioOutputMode.AudioSource.  
[IsAudioTrackEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.IsAudioTrackEnabled.html) | Whether decoding for the specified audio track is enabled. See VideoPlayer.EnableAudioTrack for distinction with mute.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Pause.html) | Pauses the playback and leaves the current time intact.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Play.html) | Starts or resumes the playback of a video.  
[Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html) | Prepares the playback engine so that it's ready for playback.  
[SetDirectAudioMute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.SetDirectAudioMute.html) | Set the direct-output audio mute status for the specified track.  
[SetDirectAudioVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.SetDirectAudioVolume.html) | Set the direct-output audio volume for the specified track.  
[SetTargetAudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.SetTargetAudioSource.html) | Sets the AudioSource that will receive audio samples for the specified track if this audio target is selected with VideoPlayer.audioOutputMode.  
[StepForward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.StepForward.html) | Immediately advance the current time by one frame.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Stop.html) | Stops the playback and sets the current time to 0.  
### Events
Event | Description  
---|---  
[clockResyncOccurred](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-clockResyncOccurred.html) | Invoked when the VideoPlayer clock is synced back to its VideoTimeReference.  
[errorReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-errorReceived.html) | The VideoPlayer uses this callback to report various types of errors.  
[frameDropped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameDropped.html) | Invoked when the video decoder does not produce a frame as per the time source during playback.  
[frameReady](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameReady.html) | The VideoPlayer invokes this event when a new frame is ready to be displayed.  
[loopPointReached](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-loopPointReached.html) | The VideoPlayer emits this event when the video reaches the end of its playback.  
[prepareCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-prepareCompleted.html) | The VideoPlayer invokes this event when the video is ready for playback.  
[seekCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-seekCompleted.html) | Invoke after a seek operation completes.  
[started](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-started.html) | The VideoPlayer emits this event when the video starts to play.  
### Delegates
Delegate | Description  
---|---  
[ErrorEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.ErrorEventHandler.html) | Delegate type for VideoPlayer events that contain an error message.  
[EventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) | Delegate type for all events without parameters emitted by VideoPlayers.  
[FrameReadyEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.FrameReadyEventHandler.html) | Delegate type for VideoPlayer events that carry a frame number.  
[TimeEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.TimeEventHandler.html) | Delegate type for VideoPlayer events that carry a time position.  
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
