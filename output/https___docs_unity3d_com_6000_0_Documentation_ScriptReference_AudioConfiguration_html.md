* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html

# AudioConfiguration
struct in UnityEngine
/
Implemented in:[UnityEngine.AudioModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AudioModule.html)
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
Specifies the current properties or desired properties to be set for the audio system.
Use these properties to change how Unity outputs all audio in your project, including how many sounds can play at one time and what speaker mode to use.   
  
For a longer example, refer to [AudioSettings.Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html).  
  
Additional resources: [AudioSpeakerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html), [AudioSettings.GetConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html). 
```
// This script changes all the settings of the audio configuration programatically. 
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). Also assign an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component in the Inspector and 
// assign an audio clip to the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).   
  
using UnityEngine;  
  
public class AudioConfigurationExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) source = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();  
  
        AudioConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) config = AudioSettings.GetConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html)();  
  
        // Change each configuration to your preferred setting. 
        config.speakerMode = AudioSpeakerMode.Stereo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Stereo.html);
        config.dspBufferSize = 64;
        config.sampleRate = 48000;
        config.numRealVoices = 16;
        config.numVirtualVoices = 128;  
  
        AudioSettings.Reset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html)(config);
        // Play the audio. 
        source.Play();
    }
}

```

### Properties
Property | Description  
---|---  
[dspBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration-dspBufferSize.html) | The length of the DSP buffer in samples determining the latency of sounds by the audio output device.  
[numRealVoices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration-numRealVoices.html) | The current maximum number of simultaneously audible sounds in the game.  
[numVirtualVoices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration-numVirtualVoices.html) | The maximum number of managed sounds in the game. Beyond this limit sounds will simply stop playing.  
[sampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration-sampleRate.html) | The current sample rate of the audio output device used.  
[speakerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration-speakerMode.html) | The current speaker mode used by the audio output device.  
* * *
