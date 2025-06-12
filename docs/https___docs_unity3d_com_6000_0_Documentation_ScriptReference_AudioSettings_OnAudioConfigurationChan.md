* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.OnAudioConfigurationChanged.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).OnAudioConfigurationChanged
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
### Parameters
Parameter | Description  
---|---  
value | This parameter is true if the user changes the audio output device during runtime.  
### Description
Unity calls this event whenever the global audio settings change.
The settings change when you use [AudioSettings.Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html), but an external factor can also change them. For example: 
  * The OS control panel changes the sample rate.
  * The user changes the default output device, for example if they plug in an HDMI monitor or a USB headset.


For a code example with a large range of setting options, refer to [AudioSettings.Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html).
```
// This script creates a row of buttons, one for each AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html). 
// When you press one of the buttons, Unity will play the audio with the new speaker mode. 
// Attach this script and an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component (with an audio clip) to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// If any of the options are not available on your system, it will throw an error.   
  
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
public class AudioConfigurationChangedExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
            config.dspBufferSize = 512;
            if (!AudioSettings.Reset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html)(config))
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Failed to reset AudioConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) after device change.");
            }
        }
        GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>().Play();
    }  
  
    AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html) GUIRow(AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html) value, ref bool modified)
    {
        // Add all the values in the enum to an array. 
        Array audioSpeakerModes = Enum.GetValues(typeof(AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html)));  
  
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Speaker mode = " + value.ToString());  
  
        // Loop through the AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html) enum. 
        foreach (AudioSpeakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html) speakerMode in audioSpeakerModes)
        {
            // Set the button name to the name of the enum value. 
            string s = speakerMode.ToString();  
  
            // Add brackets to the button name to show the current selected button. 
            if (speakerMode == value)
                s = "[" + s + "]";  
  
            // Create a button for each valid speaker mode. 
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(s))
            {
                value = speakerMode;
                modified = true;
            }
        }  
  
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        return value;
    }  
  
    void OnGUI()
    {
        bool modified = false;  
  
        AudioConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html) config = AudioSettings.GetConfiguration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html)();  
  
        config.speakerMode = GUIRow(config.speakerMode, ref modified);  
  
        if (modified)
            AudioSettings.Reset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html)(config);
    }
}

```

* * *
