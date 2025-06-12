* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html

# VideoCapture
class in UnityEngine.Windows.WebCam
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Records a video from the web camera directly to disk.
This API is supported in the Windows Players (Standalone and Universal Windows Platform) and in the Windows Editor. The final video recording will be stored on the local file system in the MP4 format. VideoCapture is implemented using the WinRT interface: Windows.Media.Capture.IMediaCapture.   
For more information, see Microsoft documentation on [Windows MediaCapture](https://docs.microsoft.com/en-us/uwp/api/Windows.Media.Capture.MediaCapture).  
  
**Note:** Universal Windows Platform requires both webcam and microphone capabilities.
```
using UnityEngine;
using System.Collections;
using System.Linq;
using UnityEngine.Windows.WebCam;  
  
public class VideoCaptureExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    static readonly float MaxRecordingTime = 5.0f;  
  
    VideoCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) m_VideoCapture = null;
    float m_stopRecordingTimer = float.MaxValue;  
  
    // Use this for initialization
    void Start()
    {
        StartVideoCaptureTest();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (m_VideoCapture == null || !m_VideoCapture.IsRecording)
        {
            return;
        }  
  
        if (Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) > m_stopRecordingTimer)
        {
            m_VideoCapture.StopRecordingAsync(OnStoppedRecordingVideo);
        }
    }  
  
    void StartVideoCaptureTest()
    {
        Resolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) cameraResolution = VideoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(cameraResolution);  
  
        float cameraFramerate = VideoCapture.GetSupportedFrameRatesForResolution[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.GetSupportedFrameRatesForResolution.html)(cameraResolution).OrderByDescending((fps) => fps).First();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(cameraFramerate);  
  
        VideoCapture.CreateAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.CreateAsync.html)(false, delegate(VideoCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) videoCapture)
        {
            if (videoCapture != null)
            {
                m_VideoCapture = videoCapture;
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Created VideoCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) Instance!");  
  
                CameraParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html) cameraParameters = new CameraParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html)();
                cameraParameters.hologramOpacity = 0.0f;
                cameraParameters.frameRate = cameraFramerate;
                cameraParameters.cameraResolutionWidth = cameraResolution.width;
                cameraParameters.cameraResolutionHeight = cameraResolution.height;
                cameraParameters.pixelFormat = CapturePixelFormat.BGRA32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CapturePixelFormat.BGRA32.html);  
  
                m_VideoCapture.StartVideoModeAsync(cameraParameters,
                    VideoCapture.AudioState.ApplicationAndMicAudio[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.AudioState.ApplicationAndMicAudio.html),
                    OnStartedVideoCaptureMode);
            }
            else
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Failed to create VideoCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) Instance!");
            }
        });
    }  
  
    void OnStartedVideoCaptureMode(VideoCapture.VideoCaptureResult result)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Started Video Capture Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)!");
        string timeStamp = Time.time.ToString().Replace(".", "").Replace(":", "");
        string filename = string.Format("TestVideo_{0}.mp4", timeStamp);
        string filepath = System.IO.Path.Combine(Application.persistentDataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html), filename);
        filepath = filepath.Replace("/", @"\");
        m_VideoCapture.StartRecordingAsync(filepath, OnStartedRecordingVideo);
    }  
  
    void OnStoppedVideoCaptureMode(VideoCapture.VideoCaptureResult result)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Stopped Video Capture Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)!");
    }  
  
    void OnStartedRecordingVideo(VideoCapture.VideoCaptureResult result)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Started Recording Video!");
        m_stopRecordingTimer = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + MaxRecordingTime;
    }  
  
    void OnStoppedRecordingVideo(VideoCapture.VideoCaptureResult result)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Stopped Recording Video!");
        m_VideoCapture.StopVideoModeAsync(OnStoppedVideoCaptureMode);
    }
}

```

### Static Properties
Property | Description  
---|---  
[SupportedResolutions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.SupportedResolutions.html) | A list of all the supported device resolutions for recording videos.  
### Properties
Property | Description  
---|---  
[IsRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.IsRecording.html) | Indicates whether or not the VideoCapture instance is currently recording video.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.Dispose.html) | You must call Dispose to shutdown the VideoCapture instance and release the native WinRT objects.  
[GetUnsafePointerToVideoDeviceController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.GetUnsafePointerToVideoDeviceController.html) | Provides a COM pointer to the native IVideoDeviceController.  
[StartRecordingAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StartRecordingAsync.html) | Asynchronously records a video from the web camera to the file system.  
[StartVideoModeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StartVideoModeAsync.html) | Asynchronously starts video mode.  
[StopRecordingAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StopRecordingAsync.html) | Asynchronously stops recording a video from the web camera to the file system.  
[StopVideoModeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.StopVideoModeAsync.html) | Asynchronously stops video mode.  
### Static Methods
Method | Description  
---|---  
[CreateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.CreateAsync.html) | Asynchronously creates an instance of a VideoCapture object that can be used to record videos from the web camera to disk.  
[GetSupportedFrameRatesForResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.GetSupportedFrameRatesForResolution.html) | Returns the supported frame rates at which a video can be recorded given a resolution.  
### Delegates
Delegate | Description  
---|---  
[OnStartedRecordingVideoCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnStartedRecordingVideoCallback.html) | Called when the web camera begins recording the video.  
[OnStoppedRecordingVideoCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnStoppedRecordingVideoCallback.html) | Called when the video recording has been saved to the file system.  
[OnVideoCaptureResourceCreatedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback.html) | Called when a VideoCapture resource has been created.  
[OnVideoModeStartedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoModeStartedCallback.html) | Called when video mode has been started.  
[OnVideoModeStoppedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.OnVideoModeStoppedCallback.html) | Called when video mode has been stopped.  
* * *
