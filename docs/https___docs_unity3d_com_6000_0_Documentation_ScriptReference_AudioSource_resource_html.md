* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-resource.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).resource
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
[Audio.AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html) resource; 
### Description
The default [AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html) to play.
You can also use this property to set the [AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html) that plays next.
```
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioResource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html) m_Resource;  
  
    public void PlayAudioResource()
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        audioSource.resource = m_Resource;
        audioSource.Play();
    }
}

```

* * *
