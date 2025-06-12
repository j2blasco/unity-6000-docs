* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.SetFloat.html

#  [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html).SetFloat
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
public bool SetFloat(string name, float value); 
### Parameters
Parameter | Description  
---|---  
name | The name of an exposed Audio Mixer group parameter. To expose a parameter, go to the Audio Mixer group's Inspector window, right click the parameter you want to expose, and choose **Expose [parameter name] to script**.  
value | Use to set the exposed Audio Mixer group parameter to a new value.  
### Returns
**bool** Returns false if the exposed parameter was not found or snapshots are currently being edited. 
### Description
Sets the value of the exposed parameter specified. When a parameter is exposed, it is not controlled by mixer snapshots. You can only change the parameter with this function.
**Note:** Don’t call [AudioMixer.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.SetFloat.html) in the following event functions as it can result in unexpected behavior: 
  * [MonoBehaviour.Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html)
  * [MonoBehaviour.OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnEnable.html)
  * [RuntimeInitializeLoadType.AfterSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.AfterSceneLoad.html)


Instead, call [AudioMixer.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.SetFloat.html) in [MonoBehaviour.Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html) or any event function Unity calls afterwards in [Order of execution for event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html).  
  
To see your exposed parameters, 
  1. Double click on your audio mixer. This opens the **Audio Mixer** window.
  2. At the top right of the Audio Mixer tab, click on the **Exposed Parameters** button to show the list of exposed parameters. 


To rename or remove a parameter, right click the item in the list.   
  
If the parameter you want to expose isn't in the list, you need to expose the parameter. To expose a parameter, right click the parameter you want to expose in the Audio Mixer Inspector window, and choose **Expose [parameter name] to script**.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Audio;  
  
public class MixerVolumeController : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The range of the volume slider on a mixer group
    const float minVolume = -80f;
    const float maxVolume = 20f;  
  
    public AudioMixer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html) mixer;  
  
    [Range(minVolume, maxVolume)]
    public float volume;  
  
    float previousVolume;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {  
  
        // Sets the exposed parameter "volume" in the audio mixer,
        // In this example the parameter is assumed to be the volume of a mixer group.
        // It could be any other exposable mixer parameter.
        if (!Mathf.Approximately[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html)(volume, previousVolume))
        {
            mixer.SetFloat("volume", volume);
        }  
  
        previousVolume = volume;
    }  
  
    void OnGUI()
    {
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Mixer volume");
        var newVolume = GUILayout.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalSlider.html)(volume, minVolume, maxVolume, GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(300));  
  
        if (!Mathf.Approximately[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html)(newVolume, previousVolume))
        {
            volume = newVolume;
            mixer.SetFloat("volume", volume);
        }  
  
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
    }
}
```

* * *
