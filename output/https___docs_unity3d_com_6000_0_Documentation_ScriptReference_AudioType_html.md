* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html

# AudioType
enumeration
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
The format type of the imported (native) data.
Use this enumeration to specify the format type of the audio file you want to play. This is mostly useful if you stream your audio from a server with [UnityWebRequestMultimedia.GetAudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html). For example, if you want to stream a file with the .ogg file extension, use [AudioType.OGGVORBIS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.OGGVORBIS.html).  
  
`UnityWebRequestMultimedia.GetAudioClip(www.example.com/your-file.ogg, AudioType.OGGVORBIS)); `.  
  
If you use the wrong format, the audio might not play correctly and Unity might throw an error.  
  
Additional resources: [UnityWebRequestMultimedia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.html), [DownloadHandlerAudioClip.GetContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.GetContent.html).
```
// This script streams an MP3 audio file from the web. 
// First you have to change the url to a valid link to an MP3 audio file. 
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).   
  

using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html) audioType;
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
  
        // Stream audio, store it as an audio clip and play it. Make sure the file has an MPEG audio format. 
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequestMultimedia.GetAudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html)(url, AudioType.MPEG[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.MPEG.html)))
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
### Properties
Property | Description  
---|---  
[UNKNOWN](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.UNKNOWN.html) | The audio file you want to stream has a file format that is unknown to Unity.  
[ACC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.ACC.html) | The audio file you want to stream has the Advanced Audio Coding (AAC) digital audio file format. Unity doesn’t natively support this format.  
[AIFF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.AIFF.html) | The audio file you want to stream has the Audio Interchange File Format (AIFF) audio file format. Unity doesn’t support this format.  
[IT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.IT.html) | The audio file you want to stream has the Impulse Tracker (IT) audio file format.  
[MOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.MOD.html) | The audio file you want to stream has the Protracker / Fasttracker MOD audio file format.  
[MPEG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.MPEG.html) | The audio file you want to stream has the MPEG (MP2 or MP3) audio file format.  
[OGGVORBIS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.OGGVORBIS.html) | The audio file you want to stream has the Ogg Vorbis audio file format.  
[S3M](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.S3M.html) | The audio file you want to stream has the ScreamTracker 3 audio file format.  
[WAV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.WAV.html) | The audio file you want to stream has the Microsoft WAV audio file format.  
[XM](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.XM.html) | The audio file you want to stream has the FastTracker 2 XM audio file format.  
[VAG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.VAG.html) | The audio file you want to stream has the VAG audio file format for PlayStation.  
[AUDIOQUEUE](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.AUDIOQUEUE.html) | The audio file you want to stream uses Apple’s Audio Queue file format.  
* * *
