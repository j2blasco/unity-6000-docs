* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.AUDIOQUEUE.html

#  [AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html).AUDIOQUEUE
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
The audio file you want to stream uses Apple’s Audio Queue file format.
Use Apple’s Audio Queue audio type to stream an AAC, ALAC or MP3 file on iOS or macOS. Extracodecdata is a pointer to an FMOD_AUDIOQUEUE_EXTRACODECDATA structure. Use this type to stream files with the extension `.acc`, `.m4a`, `.alac`, or `.mp3`.
```
// This script uses the Audio Queue audio type to stream an mp3 audio file from the web. Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). 
// Replace the url in the script with where you host your file.
  
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
        string url = "https://www.example.com/mp3sound.mp3";  
  
        // Stream audio, store it as an audio clip and play it. 
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequestMultimedia.GetAudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html)(url, AudioType.AUDIOQUEUE[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.AUDIOQUEUE.html)))
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
