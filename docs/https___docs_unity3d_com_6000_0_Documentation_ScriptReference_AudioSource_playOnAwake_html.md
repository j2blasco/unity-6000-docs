* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-playOnAwake.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).playOnAwake
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
playOnAwake; 
### Description
Enable this property to automatically play the audio source when the component or GameObject becomes active.
If you enable this property and the GameObject isn't active or if the AudioSource component is disabled, the audio won't play until they become active. While this property is enabled, if you disable then enable the GameObject or the audio source, the audio will stop and then play again from the start. If you set this property to `false`, the audio doesn't play. In this case, you need to use [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) to play the audio.
```
// This script creates and attaches an audio source to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and disables playOnAwake. 
// This means the audio won't play on launch, instead you need to press the button this script creates to play the audio.
// Make sure to assign an audio clip in the Inspector.   
  
using UnityEngine;  
  
public class PlayOnAwakeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) audioClip;   
  
    void Awake()
    {
        audioSource = gameObject.AddComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        audioSource.playOnAwake = false;
        audioSource.clip = audioClip; 
    }  
  
    void OnGUI()
    {
        if(GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 30), "Play"))
        {
            audioSource.Play(); 
        }
    }
}
```

```
// This script creates 2 toggles - 1 changes the status of AudioSource.playOnAwake[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-playOnAwake.html), the other activates or deactivates the audio source component. 
// If you deactivate **Enable audio source**, any audio that is currently playing will stop. 
// If you enable **Play on Awake** and activate **Enable audio source**, the audio will play from the start. 
// If you disable **Play on Awake**, the audio will not play when you activate the audio source.   
  
// For this script to work, attach the script and an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). 
// Also assign an audio resource to the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) so it has audio to play.    
  
using UnityEngine;  
  

[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class PlayOnAwakeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Awake()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void OnGUI()
    {
        // Toggles that change the status of AudioSource.playOnAwake[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-playOnAwake.html) and AudioSource.enabled.
        audioSource.playOnAwake = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 0, 150, 30), audioSource.playOnAwake, "Play on Awake");
        audioSource.enabled = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 30), audioSource.enabled, "Enable audio source");
    }
}
```

* * *
