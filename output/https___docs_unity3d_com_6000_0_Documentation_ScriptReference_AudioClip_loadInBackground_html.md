* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadInBackground.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).loadInBackground
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html "Go to AudioClip Component in the Manual")
loadInBackground; 
### Description
Enable this property to load the AudioClip asynchronously in the background instead of on the main thread. Set this property in the Inspector (Read Only).
This property is useful if you have a lot of files or large files to load. If you load them in a separate thread from the main thread, it can help prevent frame rate drops. You can’t change this property during runtime so if you need to set this property, do one of the following before you enter Play mode: 
  * Enable **Load In Background** in the AudioClip’s Inspector.
  * Use [AudioImporter.loadInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-loadInBackground.html).


```
// This script outputs the load status and the loadInBackground setting for each clip. 
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). 
// Fill the **Audio Clips To Preload** array with audio clips. 
// In each audio clip, enable **Preload Asset Data** in the Inspector.   
  
using UnityEngine;
using System.Collections;  
  
public class LoadInBackgroundExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)[] audioClipsToLoad;  
  
    void Start()
    {
        // Preload audio clips. 
        StartCoroutine(LoadAudioClips());
    }  
  
    private IEnumerator LoadAudioClips()
    {
        foreach (AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) clip in audioClipsToLoad)
        {
            // Check if the clip is set to load in the background. 
            if (clip.loadInBackground)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Loading {clip.name} in background.");
            }
            else
            {
                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {clip.name} is NOT set to load in the background.");
            }  
  
            // Check if the audio clip has finished loading. 
            while (clip.loadState == AudioDataLoadState.Loading[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loading.html))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {clip.name} is still loading.");
                yield return null; 
            }
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {clip.name} is fully loaded.");
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Loading complete.");
    }
}

```

* * *
