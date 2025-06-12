* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html

#  [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html).PCMReaderCallback
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
public delegate void PCMReaderCallback(float[] data); 
### Parameters
Parameter | Description  
---|---  
data | Array of floats containing data read from the clip.  
### Description
Unity calls this delegate each time [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) reads data.
The AudioClip stores this raw sample data in an array of floats that range from -1 to 1. For non-streamed clips, Unity calls this delegate when it creates the audio clip. If the clip is longer than the callback's maximum amount of samples, Unity calls the delegate multiple times so the engine can get all the clip's samples. Streamed clips call this delegate continuously, and takes various samples at varied intervals. When you use [AudioClip.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html) to create a clip, you can use this delegate as a parameter and define what happens whenever the audio reads data.   
  
Additional resources: [AudioClip.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html).
```
// This script creates an audio clip, sets its data and creates a sinusoid graph when it reads the data and changes positions. 
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
  
// When Unity calls PCMReaderCallback[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMReaderCallback.html), create a graph from the audio clip’s data.  
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
//When Unity calls PCMSetPositionCallback[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.PCMSetPositionCallback.html), update the position variable. 
   void OnAudioSetPosition(int newPosition)
    {
        position = newPosition;
    }
}

```

* * *
