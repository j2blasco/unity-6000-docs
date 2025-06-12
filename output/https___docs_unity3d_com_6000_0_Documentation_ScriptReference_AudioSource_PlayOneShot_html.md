* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOneShot.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).PlayOneShot
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
public void PlayOneShot([AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) clip, float volumeScale = 1.0F); 
### Parameters
Parameter | Description  
---|---  
clip | The clip being played.  
volumeScale | The scale of the volume. Unity automatically clamps negative scales to zero. Note: Scales larger than one might cause clipping.  
### Description
Plays an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html), and scales the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) volume by volumeScale.
[AudioSource.PlayOneShot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOneShot.html) does not cancel clips that are already being played by [AudioSource.PlayOneShot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOneShot.html) and [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html). For more information on how this method differs from [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html), see [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) impact;
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void OnCollisionEnter()
    {
        audioSource.PlayOneShot(impact, 0.7F);
    }
}

```

Additional resources: [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html).
* * *
