* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayClipAtPoint.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).PlayClipAtPoint
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public static void PlayClipAtPoint([AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) clip, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float volume = 1.0F); 
### Parameters
Parameter | Description  
---|---  
clip | Audio data to play.  
position | Position in world space from which sound originates.  
volume | Playback volume (range from 0.0 - 1.0).  
### Description
Plays an AudioClip at a given position in world space.
This function creates an audio source but automatically disposes of it once the clip has finished playing.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) clip; //make sure you assign an actual clip here in the inspector  
  
    void Start()
    {
        AudioSource.PlayClipAtPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayClipAtPoint.html)(clip, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 1, 2));
    }
}

```

* * *
