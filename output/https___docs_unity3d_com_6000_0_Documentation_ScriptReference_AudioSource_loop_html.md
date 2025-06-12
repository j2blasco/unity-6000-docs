* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-loop.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).loop
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
loop; 
### Description
Checks if the audio clip is looping
Return or set whether the audio clip replays after it finishes playing. Disable looping on a playing AudioSource to stop the sound after the end of the current loop. Use the checkbox in the AudioSource component to enable or disable looping without code.
```
//Create an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach this script
//Attach an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component. (Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), go to its Inspector and click **Add Component** Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html). Go to **Audio**>**Audio Source**)
//Attach an Audio clip in the AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) field of the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)
//Create a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) (**Create**>**UI**>**Button**) and a Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) (**Create**>**UI**>**Toggle**). Attach these in the Inspector of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
  
//This script allows you to toggle the loop of a sound on or off
using UnityEngine;
using UnityEngine.UI;  
  
public class AudioSourceLoop : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) m_AudioSource;  
  
    public Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) m_Toggle;
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) m_Button;  
  
    void Start()
    {
        //Fetch the AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (make sure there is one in the Inspector)
        m_AudioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        //Stop the Audio playing
        m_AudioSource.Stop();
        //Call the PlayButton function when you click this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        m_Button.onClick.AddListener(PlayButton);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Turn the loop on and off depending on the Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) status
        m_AudioSource.loop = m_Toggle.isOn;
    }  
  
    //This plays the Audio clip when you press the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
    void PlayButton()
    {
        m_AudioSource.Play();
    }
}

```

* * *
