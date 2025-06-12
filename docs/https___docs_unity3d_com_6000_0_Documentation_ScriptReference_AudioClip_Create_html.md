* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).Create
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
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool stream); 
## Declaration
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool stream, [AudioClip.PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) pcmreadercallback); 
## Declaration
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool stream, [AudioClip.PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) pcmreadercallback, [AudioClip.PCMSetPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMSetPositionCallback.html) pcmsetpositioncallback); 
**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend property of AudioSource instead to morph between 2D and 3D playback.
## Declaration
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool _3D, bool stream); 
**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend property of AudioSource instead to morph between 2D and 3D playback.
## Declaration
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool _3D, bool stream, [AudioClip.PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) pcmreadercallback); 
**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend property of AudioSource instead to morph between 2D and 3D playback.
## Declaration
public static [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) Create(string name, int lengthSamples, int channels, int frequency, bool _3D, bool stream, [AudioClip.PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) pcmreadercallback, [AudioClip.PCMSetPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMSetPositionCallback.html) pcmsetpositioncallback); 
### Parameters
Parameter | Description  
---|---  
name | Name of clip.  
lengthSamples | Number of sample frames.  
channels | Number of channels per frame.  
frequency | Sample frequency of clip.  
_3D | Audio clip is played back in 3D.  
stream | True if clip is streamed, that is if the pcmreadercallback generates data on the fly.  
pcmreadercallback | This callback is invoked to generate a block of sample data. Non-streamed clips call this only once at creation time while streamed clips call this continuously.  
pcmsetpositioncallback | This callback is invoked whenever the clip loops or changes playback position.  
### Returns
**AudioClip** A reference to the created AudioClip. 
### Description
Creates a user AudioClip with a name and with the given length in samples, channels and frequency.
Set your own audio data with [AudioClip.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.SetData.html). Use the [PCMReaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html) and [PCMSetPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMSetPositionCallback.html) delegates to get a callback whenever the clip reads data and changes the position. If `stream` is true, Unity reads in small chunks of data on demand. If it's false, Unity reads all the samples during the creation of the clip.  
  
**Note** : Unity expects you to pass an array with valid audio data (floating-point samples between -1.0 and 1.0) to `PCMReaderCallback`. If no audio data is available, you must fill the array with zeros. Otherwise it will result in unexpected noise or other unwanted sounds during playback.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int position = 0;
    public int samplerate = 44100;
    public float frequency = 440;  
  
    void Start()
    {
        AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) myClip = AudioClip.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html)("MySinusoid", samplerate * 2, 1, samplerate, true, OnAudioRead, OnAudioSetPosition);
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) aud = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        aud.clip = myClip;
        aud.Play();
    }  
  
    void OnAudioRead(float[] data)
    {
        int count = 0;
        while (count < data.Length)
        {
            data[count] = Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(2 * Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) * frequency * position / samplerate);
            position++;
            count++;
        }
    }  
  
    void OnAudioSetPosition(int newPosition)
    {
        position = newPosition;
    }
}

```

* * *
