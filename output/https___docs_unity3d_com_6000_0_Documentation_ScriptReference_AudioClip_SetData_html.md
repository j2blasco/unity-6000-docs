* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.SetData.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).SetData
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
public bool SetData(ReadOnlySpan<float> data, int offsetSamples); 
## Declaration
public bool SetData(float[] data, int offsetSamples); 
### Parameters
Parameter | Description  
---|---  
data | Linear buffer of samples to write to the audio clip buffer.  
offsetSamples | Offset from the start of the audio clip at which to begin writing sample data.  
### Returns
**bool** Returns whether all samples were successfully written to the audio clip. This can return `false` if `offsetSamples` isn't a valid offset within the existing AudioClip, or if the data is empty. 
### Description
Fills an audio clip with sample data from an array or Span. Overwrites existing data if necessary.
This is useful if you want to use procedural audio and change audio data during runtime. Only use samples with float values ranging from -1.0f to 1.0f. Don't exceed these limits because it can cause artifacts and undefined behavior.  
  
The length of the ReadOnlySpan or float array determines the sample count.   
  
Use the `offsetSamples` parameter to write into a certain position in the clip. If the length from the offset is longer than the clip length, the write will wrap around and write the remaining samples from the start of the clip.  
  
For compressed audio files, you can only set the sample data if you set **Load Type** to **Decompress on Load** in the [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) importer.  
  
For the best performance, use the Span version because you don't need to allocate managed memory.   
  
**Note:** The buffer provided contains a float value per sample and per channel. If your audio clip is stereo, the buffer contains interleaved float values for left channel, right channel, etc.
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
* * *
