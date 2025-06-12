* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html

#  [UnityWebRequestMultimedia](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.html).GetAudioClip
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
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAudioClip(string uri, [AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html) audioType); 
## Declaration
public static [Networking.UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) GetAudioClip(Uri uri, [AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html) audioType); 
### Parameters
Parameter | Description  
---|---  
uri | The URI of the audio clip to download.  
audioType | The type of audio encoding for the downloaded audio clip. See [AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html).  
### Returns
**UnityWebRequest** A [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) properly configured to download an audio clip and convert it to an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html). 
### Description
Create a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) to download an audio clip via HTTP GET and create an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) based on the retrieved data.
This method creates a [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) and sets the target URL to the string `uri` argument. This method sets no other flags or custom headers.  
  
This method attaches a [DownloadHandlerAudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.html) object to the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html). [DownloadHandlerAudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.html) is a specialized [DownloadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandler.html). It is optimized for storing data which is to be used as an audio clip in the Unity Engine. Using this class significantly reduces memory reallocation compared to downloading raw bytes and creating an audio clip manually in script.  
  
This method attaches no [UploadHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UploadHandler.html) to the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class MyBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(GetAudioClip());
    }  
  
    IEnumerator GetAudioClip()
    {
        using (UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) www = UnityWebRequestMultimedia.GetAudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestMultimedia.GetAudioClip.html)("https://www.my-server.com/audio.ogg", AudioType.OGGVORBIS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.OGGVORBIS.html)))
        {
            yield return www.SendWebRequest();  
  
            if (www.result == UnityWebRequest.Result.ConnectionError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.ConnectionError.html))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(www.error);
            }
            else
            {
                AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) myClip = DownloadHandlerAudioClip.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAudioClip.GetContent.html)(www);
            }
        }
    }
}

```

* * *
