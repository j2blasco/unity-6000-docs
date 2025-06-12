* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.UnloadAudioData.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).UnloadAudioData
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
## Declaration
public bool UnloadAudioData(); 
### Returns
**bool** Returns `true` if the audio data unloads successfully. 
### Description
Unloads the audio data associated with the clip. This works only for AudioClips that are based on actual sound file assets.
This is useful because when you unload the audio data, you free up the memory the audio data uses. You can use this function to optimize memory and not have assets that you aren’t currently using taking up space in memory. If you want to play or process the audio again, you need to use [AudioClip.LoadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.LoadAudioData.html).
```
// If you click the button, it will load and play the sound you attach to this GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// If you click the button again, the sound will stop and the audio data will unload. 
// Assign this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and assign a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) and an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) in the Inspector.   
  
using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using TMPro;  
  
public class AudioUnloadExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
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
        if(audioSource.isPlaying == false)
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
        // When the audio loads, play the clip and change the button's text. 
        if (audioClip.loadState == AudioDataLoadState.Loaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loaded.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) {audioClip.name} is fully loaded.");
            audioSource.Play();
            buttonText.text = "Stop";
        }
    }
}

```

* * *
