* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioChannelCount.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).GetAudioChannelCount
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
public ushort GetAudioChannelCount(ushort audioTrackIdx); 
### Parameters
Parameter | Description  
---|---  
audioTrackIdx | Use this index to specify which audio track in the video to use.  
### Returns
**ushort** The number of channels. 
### Description
Returns the number of channels in the audio track. For example, if the audio track is a stereo track, this function returns 2.
Video files can have multiple audio tracks for various reasons. For example, they can use different tracks to separate: 
  * different languages.
  * accessibility options.
  * high sampling from low sampling tracks.
  * music from sound effects.
  * sounds with different channel counts.


This function lets you specify an audio track within a video clip to check the channel counts of each one.   
  
The following are further examples of track types and what this function returns for each type: 
  * Mono returns `1`.
  * Stereo returns `2`.
  * Surround sound returns `3` for 2.1, `6` for 5.1, or `8` for 7.1.


This function is useful because you can use the channel count to adapt to different video clips with different audio qualities.  
  
Additional resources: [VideoPlayer.GetAudioChannelCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioChannelCount.html), [VideoPlayer.EnableAudioTrack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EnableAudioTrack.html), [VideoClip.GetAudioLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioLanguage.html), [VideoPlayer.GetAudioSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.GetAudioSampleRate.html).
```
// This script cycles through a video clip's audio tracks, enables tracks that have 2 channels, and deactivates others. 
// Assign this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// Then assign a video to the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) in the Inspector.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class AudioChannelCountExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;
        VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) videoClip;
        // The amount of channels you want your audio track to have. 
        int preferredAudioChannel = 2;  
  
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        if(videoPlayer != null )
        {
            videoClip = videoPlayer.clip;
            
            if (videoClip != null)
            {
                // Get the number of audio tracks in the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).
                int audioTrackCount = videoClip.audioTrackCount;  
  
                // Loop through each audio track and get the number of channels.
                for (ushort i = 0; i < audioTrackCount; i++)
                {
                    ushort channelCount = videoClip.GetAudioChannelCount(i);  
  
                    // Enable the track if it has your preferred audio channel count. 
                    if (channelCount == preferredAudioChannel)
                    {
                        videoPlayer.EnableAudioTrack(i, true);
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Enabled audio track " + i + " because it has " + channelCount + " channels.");
                    }
                    // Otherwise, deactivate the track. 
                    else
                    {
                        videoPlayer.EnableAudioTrack(i, false);
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Deactivated audio track " + i + " because it has " + channelCount + " channels.");
                    }
                }
                videoPlayer.Play();
            }
            else
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) assigned to VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).");
            }  
  
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) assigned to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).");
        }
    }
}
```

* * *
