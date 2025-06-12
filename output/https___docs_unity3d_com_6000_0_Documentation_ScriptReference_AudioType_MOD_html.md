* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.MOD.html

#  [AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html).MOD
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
The audio file you want to stream has the Protracker / Fasttracker MOD audio file format.
Use this enumeration value to ensure the format type of the audio file has the MOD audio file format. Use this audio type for files with the extension `.mod`. If the audio file has a different format, Unity might not play the audio correctly.
```
// This script streams a MOD audio file from the web. 
// First though you need to switch out the url to a valid url of a MOD audio file hosted on the web. 
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). 
  
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class AudioTypeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        // Add an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). 
        audioSource = gameObject.AddComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        StartCoroutine(GetAudioClip());
    }  
  
    IEnumerator GetAudioClip()
    {
        // Replace the string with where you host your audio file. 
        string url = "https://www.example.com/modsound.mod";  
  
        // Stream audio, store it as an audio clip and play it. Make sure it has the MOD audio format. 
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequestMultimedia.GetAudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html)(url, AudioType.MOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.MOD.html)))
        {
            yield return www.SendWebRequest();  
  
            if (www.result == UnityWebRequest.Result.ConnectionError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ConnectionError.html))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(www.error);
            }
            else
            {
                AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) myClip = DownloadHandlerAudioClip.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.GetContent.html)(www);
                
                audioSource.clip = myClip;  
                audioSource.Play(); 
            }
        }
    }
}
```

* * *
