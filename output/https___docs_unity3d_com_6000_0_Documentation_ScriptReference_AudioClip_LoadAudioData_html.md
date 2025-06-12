* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.LoadAudioData.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).LoadAudioData
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
## Declaration
public bool LoadAudioData(); 
### Returns
**bool** Returns true if the clip is loaded into memory. 
### Description
Loads the asset data of an AudioClip into memory, so it will immediately be ready to play.
Use this method when your application can afford an upfront performance overhead, which happens because this method loads resources in ahead-of-time. For example, use AudioClip.LoadAudioData in the Start() method of MonoBehaviour."  
  
If you use [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) to play an unloaded AudioClip, [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) will load that AudioClip. If an AudioClip is already loaded, AudioSource.LoadAudioData will not reload it and return true. This method won't reload AudioClips with preloadAudioData set to true.  
  
This method loads the AudioClip synchronously, unless [AudioClip.loadInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadInBackground.html) is set to `true`.
```
using UnityEngine;  
  
public class LoadClipAtStart : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) m_Clip;
    void Start()
    {
        m_Clip.LoadAudioData();
        //Components that use AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html), for example AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html), are ready to immediately use the audio data, rather
        // than triggering a load themselves.  
  
    }
}

```

Use this method when your application can afford an upfront performance overhead, which happens because this method loads resources in ahead-of-time. For example, use AudioClip.LoadAudioData in the Start() method of MonoBehaviour.  
  
If you use [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) to play an unloaded AudioClip, [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) will load that AudioClip. If an AudioClip is already loaded, AudioSource.LoadAudioData will not reload it and return true. This method won't reload AudioClips with preloadAudioData set to true.  
  
This method loads the AudioClip synchronously.
* * *
