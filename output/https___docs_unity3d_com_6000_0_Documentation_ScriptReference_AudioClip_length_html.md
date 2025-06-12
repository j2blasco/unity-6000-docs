* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-length.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).length
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
length; 
### Description
The length of the audio clip in seconds. (Read Only)
```
//Attach an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) along with this script.
//Click and drag or choose an Audio clip to the **AudioClip** field in the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).
//Click and drag or choose a different Audio clip for the Audio Clip 2 field in the Inspector window.  
  
//This script switches between two Audio clips and outputs each of their lengths in the console
//In Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), press the space key to switch between the Audio clips  
  
using UnityEngine;
using UnityEngine.Audio;  
  
public class AudioClipLengthExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Make sure your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component first
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) m_AudioSource;  
  
    //Make sure to set an Audio Clip in the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component
    AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) m_AudioClip;  
  
    //Make sure you set an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) in the Inspector window
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) m_AudioClip2;  
  
    void Start()
    {
        //Fetch the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_AudioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();  
  
        //Set the original AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) as this clip
        m_AudioClip = m_AudioSource.clip;  
  
        //Output the current clip's length
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Audio clip length : " + m_AudioSource.clip.length);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press this key to switch Audio Clips
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            SwitchAudio();
        }
    }  
  
    void SwitchAudio()
    {
        //If the current Audio clip is the original Audio clip, switch to the second clip
        if (m_AudioSource.clip == m_AudioClip)
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to the second clip
            m_AudioSource.clip = m_AudioClip2;  
  
            //Play the second clip
            m_AudioSource.Play();
        }
        //Otherwise, if the current Audio clip is the second clip, switch back
        else if (m_AudioSource.clip == m_AudioClip2)
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) back to the original Audio clip
            m_AudioSource.clip = m_AudioClip;  
  
            //Play the original clip
            m_AudioSource.Play();
        }  
  
        //Output the length of the current Audio clip
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Audio clip length : " + m_AudioSource.clip.length);
    }
}

```

* * *
