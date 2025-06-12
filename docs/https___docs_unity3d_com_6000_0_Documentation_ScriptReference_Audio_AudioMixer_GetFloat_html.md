* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.GetFloat.html

#  [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html).GetFloat
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
public bool GetFloat(string name, out float value); 
### Parameters
Parameter | Description  
---|---  
name | Name of exposed parameter.  
value | Return value of exposed parameter.  
### Returns
**bool** Returns false if the exposed parameter specified doesn't exist. 
### Description
Returns the value of the exposed parameter specified. If the parameter doesn't exist the function returns false. Prior to calling SetFloat and after ClearFloat has been called on this parameter the value returned will be that of the current snapshot or snapshot transition.
To see your exposed parameters, 
  1. Double click on your audio mixer. This opens the Audio Mixer window.
  2. At the top right of the **Audio Mixer** window, click on the **Exposed Parameters** button to show the list of exposed parameters. 


To rename or remove a parameter, right click the item in the list.   
  
If the parameter you want to expose isn't in the list, you need to expose the parameter. To expose a parameter, right click the parameter you want to expose in the Audio Mixer Inspector window, and choose **Expose [parameter name] to script**.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Audio;  
  
// 1. Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// 2. Create an Audio Mixer and expose some variables on it.
// 3. Add an Audio Source to your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and assign your Audio Mixer to it.   
  
public class MixerVolumeController : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Make sure to assign your Audio Mixer in the Inspector window of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attach this script to.
    public AudioMixer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html) mixer;
    float volume, exposedParam;  
  
    void Start()
{  
  
    // Gets the exposed parameters "MyExposedParam" and "volume" in the Audio Mixer.
    // "MyExposedParam" is the default name for exposed parameters.
 
    // "Volume is an exposed parameter that has been renamed. 
    // Change these names to what your exposed parameters are called.   
  
    mixer.GetFloat("MyExposedParam", out exposedParam);
    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("My Exposed Param: " + exposedParam);  
  
    mixer.GetFloat("Volume", out volume);
    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Volume: " + volume);
}
}

```

* * *
