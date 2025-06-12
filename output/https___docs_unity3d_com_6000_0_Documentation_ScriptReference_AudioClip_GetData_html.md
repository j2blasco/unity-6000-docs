* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.GetData.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).GetData
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
public bool GetData(Span<float> data, int offsetSamples); 
## Declaration
public bool GetData(float[] data, int offsetSamples); 
### Parameters
Parameter | Description  
---|---  
data | The array you want to fill with raw data from the audio clip.  
offsetSamples | The index of where to start data extraction from the array of raw data.  
### Returns
**bool** Returns 'true' if [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) retrieves the data successfully. Returns 'false' if the operation was unsuccessful. 
### Description
Fills an array with sample data from the audio clip.
The sample data contains float values within the range -1.0f to 1.0f. The sample count is the length of the Span or float array. Use the `offsetSamples` parameter to start the read from a specific position in the clip. If the read length from the offset is longer than the clip length, the read wraps around and reads the remaining samples from the start of the clip.  
  
For multi-channel audio clips, the data is interleaved, which means the samples in the returned float array alternate between channels. For example, in a stereo audio clip: 
  * Index 0 corresponds to channel 1 (left).
  * Index 1 corresponds to channel 2 (right).
  * Index 2 corresponds to the next sample for channel 1, and so on.


With compressed audio files, you can only retrieve the sample data if you set the **Load Type** to **Decompress on Load** in the AudioClip importer. `GetData` doesn't work with streamed audio clips, including if you stream clips from the disk or use [AudioClip.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html) and set its `stream` parameter to `true`.   
  
If `GetData` can't read the audio clip, the `data` parameter will contain zeroes for all sample values, the console will log an error, and `GetData` will return false.  
  
For the best performance, use the Span version because you don't need to allocate managed memory.
```
using UnityEngine;
using Unity.Collections;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Read all the samples from the clip and halve the gain
    void Start()
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        var numSamples = audioSource.clip.samples * audioSource.clip.channels;
        var samples = new NativeArray<float>(numSamples, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        audioSource.clip.GetData(samples, 0);  
  
        for (int i = 0; i < samples.Length; ++i)
        {
            samples[i] = samples[i] * 0.5f;
        }  
  
        audioSource.clip.SetData(samples, 0);
    }
}

```

**WebGL:** The sample data of audio clips is loaded asynchronously in the WebGL platform. This makes it necessary to check the _loadState_ of an AudioClip before reading the sample data.
```
using UnityEngine;
using Unity.Collections;
using System.Collections;  
  
public class ExampleGetDataCoroutine : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(GetAudioData());
    }  
  
    IEnumerator GetAudioData()
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        // Wait for sample data to be loaded
        while (audioSource.clip.loadState != AudioDataLoadState.Loaded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioDataLoadState.Loaded.html))
        {
            yield return null;
        }  
  
        // Read all the samples from the clip and halve the gain
        var numSamples = audioSource.clip.samples * audioSource.clip.channels;
        var samples = new NativeArray<float>(numSamples, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        audioSource.clip.GetData(samples, 0);  
  
        for (int i = 0; i < samples.Length; ++i)
        {
            samples[i] = samples[i] * 0.5f;
        }  
  
        audioSource.clip.SetData(samples, 0);
    }
}

```

* * *
