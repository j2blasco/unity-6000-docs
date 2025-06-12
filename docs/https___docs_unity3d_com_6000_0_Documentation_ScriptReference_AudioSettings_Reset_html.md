* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).Reset
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html "Go to AudioSettings Component in the Manual")
## Declaration
public static bool Reset([AudioConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) config); 
### Parameters
Parameter | Description  
---|---  
config | The new configuration to be used.  
### Returns
**bool** True if all settings could be successfully applied. 
### Description
Changes the device configuration and invokes the [AudioSettings.OnAudioConfigurationChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.OnAudioConfigurationChanged.html) delegate with the argument `deviceWasChanged=false`. There's no guarantee that the exact settings specified are used, but Unity automatically uses the closest match that it supports. **Note:** This can cause main thread stalls if `AudioSettings.Reset` is called when objects are loading asynchronously. 
```
using UnityEngine;
using System.Collections;  
  
public class TestAudioConfiguration : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        AudioSettings.OnAudioConfigurationChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.OnAudioConfigurationChanged.html) += OnAudioConfigurationChanged;
    }  
  
    void OnAudioConfigurationChanged(bool deviceWasChanged)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(deviceWasChanged ? "Device[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Device.html) was changed" : "Reset was called");
        if (deviceWasChanged)
        {
            AudioConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) config = AudioSettings.GetConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html)();
            config.dspBufferSize = 64;
            AudioSettings.Reset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html)(config);
        }
        GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>().Play();
    }  
  
    static int[] validSpeakerModes =
    {
        (int)AudioSpeakerMode.Mono[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Mono.html),
        (int)AudioSpeakerMode.Stereo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Stereo.html),
        (int)AudioSpeakerMode.Quad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Quad.html),
        (int)AudioSpeakerMode.Surround[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Surround.html),
        (int)AudioSpeakerMode.Mode5point1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Mode5point1.html),
        (int)AudioSpeakerMode.Mode7point1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.Mode7point1.html)
    };  
  
    static int[] validDSPBufferSizes =
    {
        32, 64, 128, 256, 340, 480, 512, 1024, 2048, 4096, 8192
    };  
  
    static int[] validSampleRates =
    {
        11025, 22050, 44100, 48000, 88200, 96000,
    };  
  
    static int[] validNumRealVoices =
    {
        1, 2, 4, 8, 16, 32, 50, 64, 100, 128, 256, 512,
    };  
  
    static int[] validNumVirtualVoices =
    {
        1, 2, 4, 8, 16, 32, 50, 64, 100, 128, 256, 512,
    };  
  
    int GUIRow(string name, int[] valid, int value, ref bool modified)
    {
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(name + "=" + value);
        for (int i = 0; i < valid.Length; i++)
        {
            string s = valid[i].ToString();
            if (valid[i] == value)
                s = "[" + s + "]";
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(s))
            {
                value = valid[i];
                modified = true;
            }
        }
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        return value;
    }  
  
    void OnGUI()
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) source = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        bool modified = false;  
  
        AudioConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) config = AudioSettings.GetConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html)();  
  
        config.speakerMode = (AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html))GUIRow("speakerMode", validSpeakerModes, (int)config.speakerMode, ref modified);
        config.dspBufferSize = GUIRow("dspBufferSize", validDSPBufferSizes, config.dspBufferSize, ref modified);
        config.sampleRate = GUIRow("sampleRate", validSampleRates, config.sampleRate, ref modified);
        config.numRealVoices = GUIRow("RealVoices", validNumRealVoices, config.numRealVoices, ref modified);
        config.numVirtualVoices = GUIRow("numVirtualVoices", validNumVirtualVoices, config.numVirtualVoices, ref modified);  
  
        if (modified)
            AudioSettings.Reset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html)(config);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Start"))
            source.Play();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Stop"))
            source.Stop();
    }
}

```

* * *
