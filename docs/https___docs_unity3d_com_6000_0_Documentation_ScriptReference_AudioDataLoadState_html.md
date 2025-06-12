* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.html

# AudioDataLoadState
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
Value describes the current load state of the audio data associated with an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).
This enumeration is useful if you want to: 
  * Only load audio data if the data isn’t already loaded.
  * Perform actions while the audio data loads.
  * Track progress and failures of the load.
  * Make sure certain actions don’t start until the audio starts to load or has finished loading.


Use [AudioClip.LoadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.LoadAudioData.html) and [AudioClip.UnloadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.UnloadAudioData.html) to load and unload the audio data of the AudioClip.   
  
Additional resources: [AudioClip.loadState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadState.html), [AudioClip.UnloadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.UnloadAudioData.html).
```
// If you click the button, it will load and play the sound you attach to this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// If you click the button again, the sound will stop and the audio data will unload. 
// Assign this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and assign a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) and an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) in the Inspector.   
  
using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using TMPro;  
  
public class AudioDataLoadStateExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) playButton;
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) audioClip;
    TextMeshProUGUI buttonText;
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Awake()
    {
        // Create and attach an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to play the audio. 
        audioSource = gameObject.AddComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();  
  
        if (audioClip != null)
        {
            audioSource.clip = audioClip;  
  
            if (playButton != null)
            {
                buttonText = playButton.GetComponentInChildren<TextMeshProUGUI>();
                buttonText.text = "Play";  
  
                playButton.onClick.AddListener(OnPlayStopButtonClicked);
            }
            else Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) not assigned in Inspector.");
        }
        else Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) not assigned in Inspector.");
    }  
  
    void OnPlayStopButtonClicked()
    {
        // Load and play the audio if the audio isn't playing. 
        if (audioSource.isPlaying == false)
        {
            if (!audioClip.preloadAudioData)
            {
                audioClip.LoadAudioData();
            }
            StartCoroutine(CheckLoadAudioClip());
        }
        // Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) clicked in Stop state, so if the audio is playing, stop and unload. 
        else
        {
            audioSource.Stop();
            audioClip.UnloadAudioData();
            // Don't want the audio to be playable again, so remove button. 
            playButton.gameObject.SetActive(false);
        }
    }  
  
    private IEnumerator CheckLoadAudioClip()
    {
        // Check if the audio clip has finished loading.
        while (audioClip.loadState == AudioDataLoadState.Loading[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loading.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {audioClip.name} is still loading...");
            yield return null;
        }  
  
        switch (audioClip.loadState)
        {
            case AudioDataLoadState.Unloaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Unloaded.html): 
            { 
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {audioClip.name} is still unloaded."); 
                break; 
            }
            case AudioDataLoadState.Failed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Failed.html): 
            { 
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {audioClip.name} failed to load."); 
                break; 
            }
            case AudioDataLoadState.Loaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loaded.html): 
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {audioClip.name} is fully loaded.");
                audioSource.Play();
                buttonText.text = "Stop";
                break;
            }
        }
    }
}
```

### Properties
Property | Description  
---|---  
[Unloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Unloaded.html) | Value returned by AudioClip.loadState for an AudioClip that has no audio data loaded and where loading has not been initiated yet.  
[Loading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loading.html) | Value returned by AudioClip.loadState for an AudioClip that is currently loading audio data.  
[Loaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loaded.html) | Value returned by AudioClip.loadState for an AudioClip that has succeeded loading its audio data.  
[Failed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Failed.html) | Value returned by AudioClip.loadState for an AudioClip that has failed loading its audio data.  
* * *
